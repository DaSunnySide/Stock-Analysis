import requests
import json
from tkinter import *


root = Tk()
root.title('Stock Analysis')
title = Label(root, text="Stock Symbol", bg="gray", fg="white")
title.grid(row=1)
textBox = Text(root, height=2, width=30)
textBox.grid(row=1, column=1)
buttonCommit = Button(root, height=1, width=10, text="Commit",
                     command=lambda: retrieve_input())

buttonCommit.grid(row=1, column=1)
symbol = buttonCommit
symbol.grid(row=2, column=2)
funct = input("Enter the function (TIME_SERIES_DAILY, TIME_SERIES_INTRADAY, \nTIME_SERIES_DAILY_ADJUSTED, TIME_SERIES_WEEKLY, TIME_SERIES_WEEKLY_ADJUSTED, \nTIME_SERIES_MONTHLY, TIME_SERIES_MONTHLY_ADJUSTED)")
API_KEY = "VW506K51LFXGUT1C"
API_ROOT = 'https://www.alphavantage.co/'
API_QUERY = 'query?function=' + funct + '&symbol=' + symbol + '&' + 'apikey=' + API_KEY

r = requests.get(API_ROOT + API_QUERY + API_KEY)
res = r.json()
request_text = r.text

data = json.loads(request_text)
print(data)

data_serialized = json.dumps(('data.json', 'w'), indent=4)
print(data_serialized)

formatted = json.dumps(res, indent=4, sort_keys=True)

info = json.loads(formatted)
def retrieve_input():
    inputValue=textBox.get("1.0", "end")
    print(inputValue)


print(info)


root.mainloop()
