TEAM_TYPE = dict[int, dict]


class DatabaseError(Exception):
    pass


# Database representation
_TEAM: TEAM_TYPE = {
    1: {"name": "John", "age": 20},
    3: {"name": "Mark", "age": 33},
    12: {"name": "Cavin", "age": 31},
}


def get_team() -> TEAM_TYPE:
    return _TEAM


def get(id_) -> dict:
    try:
        player = _TEAM[id_]
    except KeyError:
        raise DatabaseError(f"Id: {id_} is not exist")
    else:
        return player


def save(id_: int, instance: dict, debug: bool = False) -> dict:
    if _TEAM.get(id_) is not None:
        # Assume that instance already in the database
        raise DatabaseError(f"Instance with id: {id_} already exist")
    else:
        _TEAM[id_] = instance
        return instance


def update(id_: int, instance: dict, debug: bool = False) -> dict:
    player: dict = get(id_=id_)
    _TEAM[id_] = instance

    return instance


def delete(id_: int, debug: bool = False):
    player: dict = get(id_=id_)  # noqa: F841
    del _TEAM[id_]
