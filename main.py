import requests
import json



API_ROOT = 'https://www.alphavantage.co/'
API_LOCATION = 'query?'
API_KEY = 'VW506K51LFXGUT1C'

function = '=TIME_SERIES_DAILY_ADJUSTED'

symbol = input('Stock Symbol: ')

output_size = '=compact'

datatype = '=json'

apikey = 'VW506K51LFXGUT1C'

def main_script():
    print(main_script)

main_script()

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=' + API_KEY)
if (r.status_code == 200):
    print(r)

    result = r.json()
dataForAllDays = result['Time Series (Daily)']


