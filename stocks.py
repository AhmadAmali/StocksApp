## stocks python file

from datetime import datetime
import yfinance as yf
import os
import pytz
import requests
import math

def query_api(city_ticker):
    city_ticker = city_ticker.upper()
    company = yf.Ticker(city_ticker)

    return company.info
    