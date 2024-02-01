from typing import Generator, Iterator

team: list[str] = ["John", "Marry", "Jack", "Mark"]


iterator: Iterator = iter(team)


# def create_generator() -> Generator:
#     yield 12
#     yield 13
#     yield 14
#     yield 15



def my_range(num: int) -> Generator[int, None, None]:
    returned_value = 0
    while num > returned_value:
        yield returned_value
        returned_value += 1


# for value in my_range(100_1000_000_000_000):
#     print(value)

generator = my_range(1000)
next(generator)
next(generator)
next(generator)
