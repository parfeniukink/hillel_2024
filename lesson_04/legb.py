# DRY
def error_handler(func):
    some_value = "inside error_handler"

    def inner(value: str):
        nonlocal some_value
        some_value += "some words"
        print(some_value)
        try:
            result = func(value=value)
        except ValueError:
            print("Something went wrong...")
        else:
            return result

    return inner


@error_handler
def make_integer(value: str) -> int:
    return int(value)


# _make_integer = error_handler(make_integer)
# print(_make_integer(value_b))


@error_handler
def make_float(value: str) -> float:
    return float(value)


value_a = "14"
value_b = "12"


print(make_integer(value_b))
print(make_float(value_a))
