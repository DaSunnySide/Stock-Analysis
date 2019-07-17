import requests

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