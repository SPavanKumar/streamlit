import streamlit as st
import yfinance as yf
#import pandas as pd

st.write("""
         # Simple stock price app 
         """)
ts = 'GOOGLE'         
td = yf.Ticker(ts)
tdf = td.history(period = 'id', start = '2010-05-31', end = '2010-05-31')
st.line_chart(tdf.closest(ts))
st.line_chart(tdf.volume)
