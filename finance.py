#stock price app

from tracemalloc import start

import streamlit as st
import yfinance as yf

ticker_symbol = "AAPL"

ticker_data = yf.Ticker(ticker_symbol)

# Get historical market data
ticker_df = ticker_data.history(start="2020-01-01", end="2023-12-31")

st.dataframe(ticker_df)