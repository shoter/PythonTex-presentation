import requests
import json

def getSymbolInfo(symbol):
    url = "http://www.bankier.pl/new-charts/get-data?symbol={0}&intraday=true&today=true&type=area".format(symbol)
    r = requests.post(url)
    data = json.loads(r.text)
    prices = data["main"]
    l = len(prices)
    price = prices[l - 1][1]
    return price;