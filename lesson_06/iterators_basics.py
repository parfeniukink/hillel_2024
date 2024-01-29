team: list[str] = ["John", "Marry", "Jack", "Mark"]


# Pseudo code
# class Iterator:
#     def __new__(cls, collection: list[str]):
#         instance = super().__new__()
#         instance.collection = collection
#         return instance

#     def __init__(self) -> None:
#         self.last_index = -1

#     def find_next(self):
#         if isinstance(self.collection, list):
#             self.last_index += 1
#             return self.collection[self.last_index]
# iterator = Iterator(collection=team)
# iterator.find_next()
# iterator.find_next()
# iterator.find_next()
# iterator.find_next()


# How the iterator is implemented in Python
# iterator = iter(team)
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(next(iterator))


# How for loop is implemented under the hood
# def for_loop(collection):
#     iterator = iter(collection)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break


# for_loop(team)

# for player in team:
#     print(player)
