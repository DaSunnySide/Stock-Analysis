import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo
from pandas.io.json import json_normalize
import plotly.tools as tools
import dash
import dash_html_components as html
import dash_core_components as dcc

symbol = input('Stock Symbol: \n')
datatype = 'datatype=csv'

API_KEY = 'VW506K51LFXGUT1C'
API_QUERY = 'https://www.alphavantage.co/query?function=' + 'TIME_SERIES_DAILY_ADJUSTED' + '&symbol=' + symbol + '&' + 'apikey=' + API_KEY+'&' +datatype

print(API_QUERY)

df = pd.read_csv(API_QUERY)
print(df)
trace = go.Scatter(x=df['timestamp'],y=df['close'],mode='lines', name='stocks')
layout=go.Layout(title="Stock prices over time")
fig = go.Figure(data=trace, layout=layout)
pyo.plot(fig)
