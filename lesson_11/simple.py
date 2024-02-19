from typing import Generic, TypeVar


class User:
    pass


class Admin(User):
    pass


class Manager(User):
    pass


UserType = TypeVar("UserType", bound=User)


class Something(Generic[UserType]):
    def foo(self, user: UserType) -> None:
        return


john = Admin()

instance = Something[Manager]()
instance.foo(john)

instance_2 = Something[Admin]()
instance_2.foo(john)
