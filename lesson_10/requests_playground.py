import requests

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=UAH&to_currency=USD&apikey=V2V43QAQ8RILGBOW"
response = requests.get(url)

print(response.json())