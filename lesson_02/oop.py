class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Price:
    def __init__(self, currency: str, value: int) -> None:
        self.currency: str = currency
        self.value: int = value

    # TODO: Complete this class


# phone = 1000 USD
# food = 100 UAH
# total = phone + food

# 1000 + (100 / 39) = 1000 + 2.56410256 USD
# 1000 * 39 + 100 = ...
