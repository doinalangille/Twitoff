import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}"
print(request_url)

response = requests.get(request_url)
print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> <class 'str'>

data = json.loads(response.text)
print(type(data)) #> <class 'dict'>

# data.keys()   # see the keys. HERE: ['Meta Data', 'Time Series (Daily)']
latest_close = data["Time Series (Daily)"]["2020-02-25"]["4. close"] # filter what we are looking for
print("LATEST CLOSING PRICE:", latest_close)

#breakpoint()