from pathlib import Path

src_root = Path(__file__).parent.parent

# filename = src_root / "team.txt"
# file = open(file=filename, mode="rt")
# lines = file.read()
# file.close()

# with open(src_root / "team.txt", "rt") as file:
#     lines = file.read()
#     print(lines)


class Factory:
    def __init__(self) -> None:
        print("Initializer")

    def __enter__(self) -> "Factory":
        print("Entering the factory")
        return self

    def __exit__(self, *args, **kwargs):
        print("Closing the factory")

    def build(self):
        print("Bulding...")


with Factory() as tesla:
    tesla.build()
