import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="F&O Top Gainers", layout="wide")

@st.cache_data(ttl=1)  # Refresh every second
def fetch_fno_gainers():
    url = "https://www.nseindia.com/api/live-analysis-variations?index=top_gainers_fno"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)  # Set cookies
    response = session.get(url, headers=headers)
    
    if response.status_code != 200:
        return pd.DataFrame({"Error": ["Failed to fetch data from NSE"]})
    
    data = response.json().get("data", [])
    if not data:
        return pd.DataFrame({"Note": ["No data available at the moment"]})
    
    df = pd.DataFrame(data)
    df = df[["symbol", "ltp", "netPrice", "tradedQuantity", "previousClose"]]
    df.columns = ["Symbol", "LTP", "% Change", "Volume", "Prev Close"]
    df["% Change"] = df["% Change"].astype(float).round(2)
    df.sort_values("% Change", ascending=False, inplace=True)

    return df

st.title("📈 F&O Top Gainers (Auto Refresh Every Second)")
data = fetch_fno_gainers()
st.dataframe(data, use_container_width=True)
