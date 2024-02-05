# CRUD (Create Read Update Delete) operations

from . import database_improved as database


# Application source code
def repr_players():
    team: dict[int, dict] = database.get_team()
    for number, player in team.items():
        print(f"\t[Player {number}]: {player['name']},{player['age']}")


def player_add(name: str, age: int, number: int) -> dict:
    player_data: dict = {"name": name, "age": age}
    created_player: dict = database.save(id_=number, instance=player_data)
    return created_player


def player_update(name: str, age: int, number: int) -> dict:
    player_data: dict = {"name": name, "age": age}
    updated_player: dict = database.update(id_=number, instance=player_data)
    return updated_player


def player_delete(number: int) -> None:
    database.delete(id_=number)


# dispatcher / handler
def commands_dispatcher(operation: str):
    operations = ("add", "del", "repr", "update", "exit")

    if operation not in operations:
        raise Exception(f"Operation: '{operation}' is not available\n")

    if operation == "exit":
        raise SystemExit("Bye! Exiting the application")

    elif operation == "repr":
        repr_players()

    elif operation == "add":
        user_data = input("Enter new player information[name,age,number]: ")
        # Input: 'Clark,19,22'
        user_items: list[str] = user_data.split(",")
        # Result: ['Clark', '19', '22']
        name, age, number = user_items
        player_add(name=name, age=int(age), number=int(number))
        print(f"Player [{number}] is added.")

    elif operation == "del":
        number = int(input("Enter player's number[int]: "))
        player_delete(number=number)
        print(f"Player: [{number}] is removed")

    elif operation == "update":
        user_data = input(
            "Enter a new player's information[name,age,number]: "
        )
        # Input: 'Clark,19,22'
        user_items: list[str] = user_data.split(",")
        # Result: ['Clark', '19', '22']
        name, age, number = user_items

        updated_player: dict = player_update(
            name=name, age=int(age), number=int(number)
        )

        print(
            f"Player [{number}] is updated. "
            f"Name: [{updated_player['name']}], "
            f"age: [{updated_player['age']}]"
        )


def main():
    while True:
        operation = input("Please enter the operation: ")
        try:
            commands_dispatcher(operation=operation)
        except database.DatabaseError as error:
            print(error)
        except ValueError:
            print("Age and number of player must be integers\n\n")
        except SystemExit as error:
            raise error
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
