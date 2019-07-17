import requests
import json


API_ROOT = 'https://www.alphavantage.co/'

API_LOCATION = 'query?'

function = '=TIME_SERIES_DAILY_ADJUSTED'

symbol = input('Stock Symbol: ')

output_size = '=compact'

datatype = '=json'

apikey = ''

def main_script():
    print(main_script)

main_script()

API_KEY = 'YOUR_API_KEY'
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=' + API_KEY)
if (r.status_code == 200):
    print(r)

    result = r.json()
dataForAllDays = result['Time Series (Daily)']
dataForSingleDate = dataForAllDays['2017-10-30']
print (dataForSingleDate['1. open'])
print (dataForSingleDate['2. high'])
print (dataForSingleDate['3. low'])
print (dataForSingleDate['4. close'])
print (dataForSingleDate['5. volume'])