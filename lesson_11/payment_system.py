from abc import ABC, abstractmethod
from dataclasses import asdict
from .models import User, Product, Card
from .api import StripeAPI, PayPalAPI

# Stripe & PayPal

STRIPE_ACCESS_TOKEN = "4070b0df-e4f8-4a6f-b5bc-fa8293f8eb89"
PAYPAL_CREDENTIALS = {
    "username": "hillel",
    "password": "hillel123",
}


def catch_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error catched: {error}")

    return inner


class PaymentProvider(ABC):
    def __init__(self, user: User) -> None:
        self.user: User = user

    @abstractmethod
    def authorize(self, **kwargs):
        pass

    @abstractmethod
    def checkout(self, product: Product):
        pass

    @abstractmethod
    def healthcheck(self):
        pass


class StripePaymentProvider(PaymentProvider):
    def authorize(self, **kwargs):
        token = kwargs.get("token", "")
        StripeAPI.authorize(
            token=token,
            user_email=self.user.email,
            card_number=self.user.card.number,
            expire_date=self.user.card.expire_date,
            cvv=self.user.card.cvv,
        )

    def _check_card(self):
        if "444" in str(self.user.card.number):
            raise Exception("card invalid")

    def checkout(self, product: Product):
        self._check_card()
        StripeAPI.checkout(user_email=self.user.email, price=product.price)

    def healthcheck(self):
        if StripeAPI.healthcheck() is False:
            raise Exception("Stripe is NOT AVAILABLE")


class PayPalPaymentProvider(PaymentProvider):
    def authorize(self, **kwargs):
        username = kwargs.get("username", "")
        password = kwargs.get("password", "")

        PayPalAPI.authorize(
            username=username,
            password=password,
            email=self.user.email,
            card_data=asdict(self.user.card),
        )

    def checkout(self, product: Product):
        PayPalAPI.checkout(email=self.user.email, price=product.price)

    def healthcheck(self):
        if PayPalAPI.is_available() is False:
            raise Exception("PayPal is NOT AVAILABLE")


def provider_dispatcher(name: str, user: User) -> PaymentProvider:
    if name == "stripe":
        return StripePaymentProvider(user=user)
    elif name == "paypal":
        return PayPalPaymentProvider(user=user)
    else:
        raise Exception(f"Provider {name} is not supported")


def main():
    john = User(
        id=1,
        email="john@email.com",
        age=30,
        card=Card(
            number=5453010000095539,
            expire_date="12/25",
            cvv=300,
        ),
    )
    marry = User(
        id=2,
        email="marry@email.com",
        age=13,
        card=Card(
            number=5453010000095345,
            expire_date="10/25",
            cvv=312,
        ),
    )

    samsung = Product(name="Samsung", price=30_000)
    iphone = Product(name="iPhone", price=35_000)

    stripe_credentials = {"token": STRIPE_ACCESS_TOKEN}

    payment_provider: PaymentProvider = provider_dispatcher("stripe", john)
    payment_provider.healthcheck()
    payment_provider.authorize(**stripe_credentials)
    payment_provider.checkout(product=samsung)
    # payment_provider._check_card()  # only for Stripe

    payment_provider: PaymentProvider = provider_dispatcher("paypal", marry)
    payment_provider.healthcheck()
    payment_provider.authorize(**PAYPAL_CREDENTIALS)
    payment_provider.checkout(product=iphone)


if __name__ == "__main__":
    main()
