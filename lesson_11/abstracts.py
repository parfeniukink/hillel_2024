import random
from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, hp: int, damage: int) -> None:
        self.hp = hp
        self.damage = damage

    @abstractmethod
    def make_damage(self, unit: "Unit"):
        pass


class GreenUnit(Unit):
    pass


class YellowUnit(Unit):
    def make_damage(self, protector: Unit):
        self.damage *= random.randint(1, 3)
        protector.hp -= self.damage


class Hero(Unit):
    def make_damage(self, protector: Unit):
        protector.hp -= self.damage


def contact(attacker: Unit, protector: Unit):
    attacker.make_damage(protector)


hero = Hero(hp=500, damage=20)
unit_1 = GreenUnit(hp=300, damage=30)
unit_2 = YellowUnit(hp=50, damage=10)

contact(attacker=hero, protector=unit_1)
contact(attacker=unit_2, protector=hero)
