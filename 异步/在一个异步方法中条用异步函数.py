import asyncio
import time

async def task1():
    print("我是他task1")
    time.sleep(1)
    await asyncio.sleep(0)
    await task2()


async def task2():

    print("我是他task2")
    time.sleep(1)
    await asyncio.sleep(0)
    await task1()


# 额外的测试
async def main():
    await asyncio.gather(task1(), task2())


#asyncio.run(task1())
if __name__ == "__main__":
    asyncio.run(main())