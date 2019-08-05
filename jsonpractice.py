import plotly.graph_objs as go
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.io.json import json_normalize
import plotly.tools as tools
import dash
import dash_html_components as html
import dash_core_components as dcc

#Initialize App
app = dash.Dash()

#Get user input for stock choice
symbol = input('Stock Symbol: \n')
datatype = 'datatype=csv'


#Define Api call
API_KEY = 'VW506K51LFXGUT1C'
API_QUERY = 'https://www.alphavantage.co/query?function=' + 'TIME_SERIES_DAILY_ADJUSTED' + '&symbol=' + symbol + '&' + 'apikey=' + API_KEY+'&' +datatype

#Print API Call Url for debugging
print(API_QUERY)

#Define Dataframe
df = pd.read_csv(API_QUERY)

app.layout = html.Div(([
    dcc.Graph(id='linegraph',
              figure={
                  'data': [
                      go.Scatter(x=df['timestamp'],y=df['close'],
                                 mode='lines', marker= {
                              'size' : 12
                          })],
                   'layout' : go.Layout(title='Stock prices over time')})
])
)






if __name__ == '__main__':
    app.run_server()
