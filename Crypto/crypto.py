import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


myApiKey = '6632c734-36fa-4a69-821f-8b7e26e3566f'

params = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '{}'.format(myApiKey)
}


try:
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    mydata = data['data']
    print("Top 10 coins\n")
    for coins in mydata:
        print(f"{coins['name']} | Price: {round(coins['quote']['USD']['price'], 2)} | 24hr change: {round(coins['quote']['USD']['percent_change_24h'], 2)}%" )
 
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

input("Press enter to exit.")


