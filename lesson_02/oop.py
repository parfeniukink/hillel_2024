class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


class Price:
    def __init__(self, currency, value) -> None:
        self.currency = currency
        self.value = value

    # TODO: Complete this class


# phone = 1000 USD
# food = 100 UAH
# total = phone + food

# 1000 + (100 / 39) = 1000 + 2.56410256 USD
# 1000 * 39 + 100 = ...
