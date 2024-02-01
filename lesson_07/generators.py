from typing import Generator


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name


# 40000
team: list[str] = [
    Player(name="John"),
    Player(name="Marry"),
    Player(name="John"),
    Player(name="Marry"),
]


def dedup(team: list[Player]) -> Generator[str, None, None]:
    players_names: set[str] = set()

    for player in team:
        if player.name not in players_names:
            yield player
            players_names.add(player.name)


for player in dedup(team):
    print(player.name)

# With sets
# team_without_duplicates = set(team)
# print(team_without_duplicates)


# Bad approach
# team_without_duplicates = []

# for player in team:
#     if player not in team_without_duplicates:
#         team_without_duplicates.append(player)

# print(team_without_duplicates)
