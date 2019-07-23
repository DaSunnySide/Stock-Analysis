import requests
import json
from tkinter import *
import main

API_KEY = "VW506K51LFXGUT1C"
r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=" + API_KEY)
res = r.json()
formatted = json.dumps(res, indent=4, sort_keys=True)

root = Tk()
title = Label(root, text="Mugger-Chilly", bg="gray", fg="white")
title.grid(row=0)

symbol = Entry(root)
symbol.grid(row=0, column=1)

info = json.load(formatted)
textBox = Text(root, height=50, width=30)
textBox.grid(row=1, column=1)
textBox.insert(side=END, )


def onClick(submitButton):
    pass


submitButton = Button(root, text="Submit", command=onClick)
submitButton.grid(row=1, column=1)

root.mainloop()



