import asyncio
import time


async def bar():
    print("I am bar BEFORE")
    await asyncio.sleep(2)
    print("I am bar AFTER")

    return 4


# Coroutine
async def foo():
    print("I am foo BEFORE")
    await asyncio.sleep(1)
    print("I am foo AFTER")

    return 5


async def main():
    print("I am async main")
    tasks = [bar(), foo()]
    # await asyncio.gather(bar(), foo())
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
