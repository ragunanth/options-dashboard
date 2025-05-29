import streamlit as st
import pandas as pd

st.set_page_config(page_title="F&O Top Gainers", layout="wide")

@st.cache_data(ttl=1)
def fetch_fno_gainers():
    # Dummy data fallback — use until live API is integrated
    return pd.DataFrame({
        "Symbol": ["SBIN", "TATASTEEL", "HINDALCO"],
        "LTP": [780.25, 142.60, 513.30],
        "% Change": [3.2, 2.5, 1.8],
        "Volume": [1200000, 850000, 670000],
        "Prev Close": [755, 139, 504]
    })

st.title("📈 F&O Top Gainers (Auto Refresh Every Second)")
data = fetch_fno_gainers()
st.dataframe(data, use_container_width=True)
