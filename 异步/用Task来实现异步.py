import asyncio
import time
"""
给task封装后的异步函数传参和拿到返回值，我把知识点合并了
"""


async def task1(num):
    f_time = time.time()
    print("task1-开始时间：", time.time())
    for i in range(num):
        print("---我是task1---")
        await asyncio.sleep(1)
    print("test1-结束时间：", time.time())
    s_time = time.time()
    return s_time - f_time


async def task2(num):
    f_time = time.time()
    print("task2-开始时间：", time.time())
    for i in range(num):
        print("---我是task2---")
        await asyncio.sleep(1)
    print("test2-结束时间：", time.time())
    s_time = time.time()
    return s_time - f_time


async def main():
    t1 = asyncio.create_task(task1(num=10))
    t2 = asyncio.create_task(task2(num=10))
    print("task1结束了吗", t1.done())
    print("task2结束了吗", t1.done())

    all_tasks = [t1, t2]
    await asyncio.wait(all_tasks)  # asyncio.wait() asyncio.gather 前面要有await

    print("task1结束了吗", t1.done())
    print("task2结束了吗", t1.done())

    print("\n" + "task1耗时：", t1.result())
    print("task2耗时：", t2.result(), "\n")

if __name__ == "__main__":
    # 记录时间和调用main（）协程
    start_time = time.time()
    asyncio.run(main())
    stop_time = time.time()
    print("总耗时：", stop_time - start_time)




  # # 显示视频文件的分辨率
  #       for f1 in files:
  #           # f前缀名
  #           video_qianzhui1 = func.get_sep_file(f1)[0]
  #           # f后缀名
  #           video_huozhui1 = func.get_sep_file(f1)[1]
  #
  #           # 判断出是视频文件才输出
  #           if video_huozhui1 == '.mp4':
  #               video_frame_size1 = func.get_video_frame_size(f1)
  #               print("%s--分辨率：%d x %d" % (f, video_frame_size1[0], video_frame_size1[1]))
  #
  #           # 判断
  #           for f2 in files:
  #               # f2
  #               video_qianzhui2 = func.get_sep_file(f2)[0]
  #               # f2
  #               video_huozhui2 = func.get_sep_file(f2)[1]
  #
  #               # 判断出是视频文件才输出
  #               if video_huozhui2 == '.mp4':
  #                   video_frame_size2 = func.get_video_frame_size(f2)
  #                   #print("%s--分辨率：%d x %d" % (f, video_frame_size2[0], video_frame_size2[1]))
  #
  #                   # 先判断分辨率
  #               if video_frame_size1 == video_frame_size2:
  #                   print("%s 和 %s 是相同分辨率文件" % (video_qianzhui1, video_qianzhui2))
  #
  #       break


n = 0

for i in files_list:
    oldname = path + os.sep + files_list[n]

    newname = path + os.sep + input_name

    os.rename(oldname, newname)
    print("%s ===>>> %s" % (oldname, newname))
    n += 1