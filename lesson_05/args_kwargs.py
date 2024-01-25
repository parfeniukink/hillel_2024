def create_product(*names: str | int, **kwargs):
    print(names)
    print(kwargs)
    # print(price)


create_product("table", 20, 30, price=222)
# create_product(name="table", price=20)
# create_product("table", price=20)
# create_product(name="table", 20)  # error
