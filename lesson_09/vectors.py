# Functional approach
# a = ((1, 1), (3, 4))
# b = ((4, 1), (6, 2))
#
# Coordinate = tuple[int, int]
# Vector = tuple[Coordinate, Coordinate]
#
#
# def add_vectors(left: Vector, right: Vector) -> Vector:
#     start: Coordinate = (left[0][0] + right[0][0], left[0][1] + right[0][1])
#     end: Coordinate = (left[1][0] + right[1][0], left[1][1] + right[1][1])
#     return (start, end)
#
#
# c = add_vectors(left=a, right=b)
# print(c)

# Class approach
class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other) -> "Point":
        return Point(
            x=self.x + other.x,
            y=self.y + other.y,
        )


class Vector:
    def __init__(self, start: Point, end: Point):
        self.start: Point = start
        self.end: Point = end

    def __str__(self):
        return f"Vector[{self.start}, {self.end}]"

    def __add__(self, other):
        return Vector(
            start=self.start + other.start,
            end=self.end + other.end
        )

    def __getattr__(self, attr: str):
        # print(f"Attribute {attr} is not exist")
        return lambda: print(f"Attribute {attr} is not exist")

    def __call__(self):
        return lambda: print(f"I am callable from __call__")

a = Vector(
    start=Point(x=1, y=1),
    end=Point(x=3, y=4)
)
b = Vector(
    start=Point(x=4, y=1),
    end=Point(x=6, y=2)
)
vector: Vector = a + b
print(vector)

vector['x'] = ...
# 5 + 2 == 7
# [1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
# "Hello " + "world" == "Hello world"
