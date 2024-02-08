input_data = "100 UAH"


# Stripe
# 100 UAH -> CHF

currency_exchange = {

}


class Price:
    value: int
    currency: str


flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="EUR")

total: Price = flight + hotel
# total.currency == USD



class Product:
    def __init__(self, name: str, price: Price):
        self.name = name
        self.price = price


class PaymentProcessor:
    def checkout(self, product: Product, price: Price):
        pass
