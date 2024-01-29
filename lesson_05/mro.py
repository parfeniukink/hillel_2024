# list, dict, tuple, set, str, bytes
# a = '12'
# a = 'asdasdasd'
# t = (1,2,3, 4)
# flat => str, bytes
# container => list[[], ()]

import random
import string


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name: str = name
        self.price: int = price

    def __str__(self) -> str:
        return f"{self.name}: {self.price}$"


class Factory:
    def build(self) -> Product:
        # "".join(['a', 'e', 'w', 'q', ...]) => aewq
        random_name: str = "".join(
            [random.choice(string.ascii_letters) for i in range(10)]
        )
        random_price: int = random.randint(10, 20)
        return Product(name=random_name, price=random_price)


class PdfGenerator:
    def generate_pdf(self, filename):
        print(f"Generating PDF: {filename}.pdf")

    def create_order_documnet(self):
        print("Stub")


class Legals(PdfGenerator):
    def create_order_documnet(self):
        self.generate_pdf(filename="legals")
        super().create_order_documnet()


class Delivery(PdfGenerator):
    def ship(self, product: Product):
        print(f"Shipping the product: {product.name}")

    def create_order_documnet(self):
        self.generate_pdf(filename="delivery")
        super().create_order_documnet()


class TeslaFacility(Factory, Delivery, Legals):
    def create_order_documnet(self):
        return super().create_order_documnet()


class IntelFacility(Factory, Legals, Delivery):
    pass


tesla_in_kyiv = TeslaFacility()
tesla_in_california = TeslaFacility()

intel_in_kyiv = IntelFacility()
intel_in_california = IntelFacility()


tesla_model_x: Product = tesla_in_california.build()
tesla_in_california.create_order_documnet()
# print(TeslaFacility.__mro__)
