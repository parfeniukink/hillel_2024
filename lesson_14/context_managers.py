import asyncio


class ContextManager:
    async def __aenter__(self):
        print("Entering")
        return self

    async def __aexit__(self, *args, **kwargs):
        print("Exiting")


async def main():
    async with ContextManager() as manager:
        print(manager)


asyncio.run(main())
