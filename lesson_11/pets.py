from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Pet):
    def sound(self):
        print("GAV GAV")


class Cat(Pet):
    def sound(self):
        print("MIAU MIAU")


def foo(pet: Pet):
    pet.sound()


joe = Dog()
tom = Cat()

foo(joe)
foo(tom)
