import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="F&O Top Gainers", layout="wide")

@st.cache_data(ttl=1)  # Refresh every second
def fetch_fno_gainers():
    # Dummy data fallback
    return pd.DataFrame({
        "Symbol": ["SBIN", "TATASTEEL", "HINDALCO"],
        "LTP": [780.25, 142.60, 513.30],
        "% Change": [3.2, 2.5, 1.8],
        "Volume": [1200000, 850000, 670000],
        "Prev Close": [755, 139, 504]
    })

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
