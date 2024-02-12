import requests
from dataclasses import dataclass

# class Price:
#     def __init__(self, value: int, currency: str):
#         self.value = value
#         self.currency = currency

# EXCHANGE_RATES = {
#     "chf": {
#         "chf": 1,
#         "usd": 0.9,
#         "uah": 0.02,
#     },
#     "usd": {
#         "chf": 1.1,
#         "uah": 0.3,
#     },
#     "uah": {
#         "chf": 3,
#         "usd": 38,
#     },
# }

ALPHAVANTAGE_API_KEY = "V2V43QAQ8RILGBOW"
MIDDLE_CURRENCY = "CHF"


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=(self.value + other.value), currency=self.currency
            )

        left_in_middle: float = convert(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        right_in_middle: float = convert(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )

        return Price(value=total_in_left_currency, currency=self.currency)


def convert(value: float, currency_from: str, currency_to: str) -> float:
    response: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
    )
    result: dict = response.json()
    # Response example
    # {
    #     "Realtime Currency Exchange Rate": {
    #         "1. From_Currency Code": "UAH",
    #         "2. From_Currency Name": "Ukrainian Hryvnia",
    #         "3. To_Currency Code": "USD",
    #         "4. To_Currency Name": "United States Dollar",
    #         "5. Exchange Rate": "0.02648000",
    #         "6. Last Refreshed": "2024-02-12 19:04:02",
    #         "7. Time Zone": "UTC",
    #         "8. Bid Price": "0.02647900",
    #         "9. Ask Price": "0.02648000"
    #     }
    # }
    print(result)
    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )
    return value * coefficient


flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="UAH")

total: Price = flight + hotel
print(total)
