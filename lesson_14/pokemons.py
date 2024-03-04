from typing import Coroutine
import httpx
import asyncio
from time import perf_counter
from pprint import pprint as print
import random
import requests
import sys
from threading import Thread


POKEAPI_BASE_URL: str = "https://pokeapi.co/api/v2/berry"


def fetch_pokemon(id_: int) -> dict:
    """Fetch the pokemon detailed information from the PokeAPI.co"""

    response: requests.Response = requests.get(url=f"{POKEAPI_BASE_URL}/{id_}")

    if response.status_code != 200:
        print(f"Error: {response.status_code} | {response.text}")
        return {}
    else:
        print(response.status_code)
        return response.json()


def main_sync(pokemons_number: int):
    results: list[dict] = []
    for i in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        pokemon: dict = fetch_pokemon(id_=random_id)
        results.append(pokemon)

    return results


def main_threads(pokemons_number: int):
    """Fetch pokemons using threads"""

    threads: list[Thread] = []
    for i in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        threads.append(Thread(target=fetch_pokemon, args=(random_id,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


async def main_async(pokemons_number: int):
    async def get_with_httpx(url: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            print(response.status_code)
            return response.status_code

    tasks: list[Coroutine] = [
        get_with_httpx(url=f"{POKEAPI_BASE_URL}/{random.randint(1, 50)}")
        for i in range(pokemons_number)
    ]
    results = await asyncio.gather(*tasks)

    return results


def main():
    try:
        runtype: str = sys.argv[1]
        pokemons_number: int = int(sys.argv[2])
    except IndexError:
        print("Please enter the number of Pokemons to fetch from PokeAPI.co")
    except ValueError:
        print("The number of pokemons to fetch must be a valid integer number")

    start = perf_counter()
    if runtype == "sync":
        main_sync(pokemons_number)
    elif runtype == "async":
        asyncio.run(main_async(pokemons_number))
    elif runtype == "threads":
        main_threads(pokemons_number)
    else:
        raise SystemExit("Unrecognize run type")

    print(f"Total: {perf_counter() - start}")


if __name__ == "__main__":
    main()
