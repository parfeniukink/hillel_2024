class Product:
    def __new__(cls, *qweqwe, **asdasdasd):
        # class_ = type(Product, (), {})
        # return class_()
        instance = super().__new__(cls)
        print(f"from new: {instance}")
        return instance

    def __init__(self, name: str, price: int) -> None:
        print(f"from init {self}")
        self.name: str = name
        self.price: int = price


print(Product.__mro__)
phone = Product(name="Table", price=20000)
print(phone)
