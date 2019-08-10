import plotly.graph_objs as go
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.io.json import json_normalize
import plotly.tools as tools
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

#Initialize App
app = dash.Dash()

#Define Colors for the UI
colors = {
    'dashbg' : '#2F3036',
    'graphbg' : '#151515',
    'increasingline' : '#4dff4d',
    'decreasingline' : '#193EFD',
    'lowcontrasttext' : '#585A65',
    'highcontrasttext' : '#FAFAFF'
}

#Define Alpha Vantage Function Calls
TIME_SERIES_INTRADAY = 'TIME_SERIES_INTRADAY'
TIME_SERIES_DAILY = 'TIME_SERIES_DAILY'
TIME_SERIES_DAILY_ADJUSTED = 'TIME_SERIES_DAILY_ADJUSTED'
TIME_SERIES_WEEKLY = 'TIME_SERIES_WEEKLY'
TIME_SERIES_WEEKLY_ADJUSTED = 'TIME_SERIES_WEEKLY_ADJUSTED'
TIME_SERIES_MONTHLY = 'TIME_SERIES_MONTHLY'
TIME_SERIES_MONTHLY_ADJUSTED = 'TIME_SERIES_MONTHLY_ADJUSTED'

#Get user input for stock choice and function information
symbol = input('Stock Symbol: \n')
datatype = 'datatype=csv'

function = input("Function: \n")
if function== 'TIME_SERIES_INTRADAY' :
    interval = input('Time interval in minutes: \n')
    symbol = symbol + '&interval=' + interval + 'min'

#Define Api call
API_KEY = 'VW506K51LFXGUT1C'
API_QUERY = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + symbol + '&' + 'apikey=' + API_KEY+'&' +datatype

#Define Dataframe and resolve issues with Intraday graph range
if function == 'TIME_SERIES_INTRADAY' :
    df = pd.read_csv(API_QUERY)

else:
    df = pd.read_csv(API_QUERY)

app.layout = html.Div(([
    dcc.Input(id='stocksymbol', value='Enter Stock Symbol', type='text'),
    dcc.Dropdown(id='graph-type',
        options=[
            {'label': 'Time Series Intraday', 'value' : 'TIME_SERIES_INTRADAY'},
            {'label': 'Time Series Daily', 'value' : 'TIME_SERIES_DAILY'},
            {'label': 'Time Series Daily Adjusted', 'value' : 'TIME_SERIES_DAILY_ADJUSTED'},
            {'label': 'Time Series Weekly', 'value' : 'TIME_SERIES_WEEKLY'},
            {'label': 'Time Series Weekly Adjusted', 'value' : 'TIME_SERIES_WEEKLY_ADJUSTED'},
            {'label': 'Time Series Monthly', 'value' : 'TIME_SERIES_MONTHLY'},
            {'label': 'Time Series Monthly Adjusted', 'value' : 'TIME_SERIES_MONTHLY_ADJUSTED'}
        ],
        value='TIME_SERIES_INTRADAY'
    ),
    dcc.Graph(id='linegraph',
              figure={
                  'data': [
                      go.Scatter(x=df['timestamp'],y=df['close'],
                                 mode='lines', marker= {
                              'size' : 12,
                              'color' : '#4dff4d'
                          })],
                   'layout' : go.Layout(title='Stock prices over time')}),
    dcc.Graph(id='candlestick',
              figure={
                  'data': [
                      go.Candlestick(x=df['timestamp'],
                                     open=df['open'],
                                     high=df['high'],
                                     low=df['low'],
                                     close=df['close'],
                                     increasing_line_color='#4DFF4D',
                                     decreasing_line_color='#193EFD'
                                     )
                  ],
                    'layout': go.Layout(title='Candlestick Graph of prices over time')
              })
]
))
@app.callback(Output('linegraph', 'figure')
              [Input('graph-type', 'value')],
              [Input('stocksymbol', 'value')])

def update_figure(graph_type, stocksymbol):
    function = graph_type
    symbol = stocksymbol
    df = pd.read_csv(API_QUERY)
    return {'data': df, 'layout' : go.Layout(title='Stock prices over time')}



if __name__ == '__main__':
    app.run_server()
