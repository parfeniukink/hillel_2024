TEAM_TYPE = dict[int, dict]

# Database representation
_TEAM: TEAM_TYPE = {
    1: {"name": "John", "age": 20},
    3: {"name": "Mark", "age": 33},
    12: {"name": "Cavin", "age": 31},
}


def get_team() -> TEAM_TYPE:
    return _TEAM


def get(id_) -> dict | None:
    try:
        player = _TEAM[id_]
    except KeyError:
        return None
    else:
        return player


def save(id_: int, instance: dict, debug: bool = False) -> bool:
    try:
        print(_TEAM[id_])
        if debug is True:
            print(f"Instance with id: {id_} already exist")
        return False
    except KeyError:
        _TEAM[id_] = instance
        return True


def update(id_: int, instance: dict, debug: bool = False):
    _TEAM[id_] = instance
    


def delete(id_: int, debug: bool = False) -> bool:
    try:
        del _TEAM[id_]
    except KeyError:
        if debug is True:
            print(f"There is not instance with id: {id_}")
        return False
    else:
        return True
