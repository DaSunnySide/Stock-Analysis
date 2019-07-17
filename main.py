import requests

API_ROOT = 'https://www.alphavantage.co/'

API_LOCATION = 'query?'

function = 'TIME_SERIES_DAILY_ADJUSTED'

symbol = 'input'

output_size = 'compact'

datatype = 'json'

apikey = ''


if __name__ == '__main__':
    while True:
        main_script()
