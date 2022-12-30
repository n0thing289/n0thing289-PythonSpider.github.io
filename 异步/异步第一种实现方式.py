import asyncio


async def task1():
    for i in range(5):
        print("我是task1--111")
        await asyncio.sleep(1)
        print("我是task1---222")


async def task2():
    for i in range(5):
        print("我是task2--111")
        #await asyncio.sleep(1)
        print("我是task2---222")


async def main():
    await asyncio.gather(task1(), task2())


if __name__ == "__main__":
    asyncio.run(main())

# import asyncio
#
# async def nested():
#     return 42
#
# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     nested()
#
#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".
#
# asyncio.run(main())