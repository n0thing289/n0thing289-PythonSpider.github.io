import asyncio
import time


async def task1():
    for i in range(5):
        print("我是1")
        await asyncio.sleep(3)
        print("12")


async def task2():
    for i in range(5):
        print("我是2")
        await asyncio.sleep(3)
        print("21")


# async def main():
#     await asyncio.gather(task2())  # 为什么这里要用await，run前面不用


if __name__ == "__main__":
    asyncio.run(task2())  #run只能调用启用一个协程对象或者说一个异步函数