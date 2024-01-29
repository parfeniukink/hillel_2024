class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name

    @staticmethod
    def calculate_something(a: int, type_: str) -> float:
        # ...
        return 12.2

    @classmethod
    def say_my_name(cls):
        cls.calculate_something(12, "some_type")
        # Player.calculate_something(...)


john = Player(name="John")
marry = Player(name="Marry")

# __new__
# __init__

john.say_my_name()
john.name = "John"
# Player.say_my_name(Player)

marry.say_my_name()
