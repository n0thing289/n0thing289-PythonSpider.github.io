import asyncio


def callback_func(x):
    print("我是回调函数，如果你看到我了说明我被它" , x,"\n回调了")



async def task1():
    print("---我是task1---")
    return 100


async def main():
    t1 = asyncio.create_task(task1())
    # 添加回调函数，t1快死之前把自己当作参数传给回调函数，回调函数必须接着，不然会报错说，我给你传值但你没有设置形参
    # 回调函数执行完成后，t1才完全死掉
    t1.add_done_callback(callback_func)
    all_tasks = [t1]
    await asyncio.wait(all_tasks)
    print("task1执行完毕了吗？", t1.done())
    print("task1返回值是：", t1.result())


if __name__ == "__main__":
    asyncio.run(main())