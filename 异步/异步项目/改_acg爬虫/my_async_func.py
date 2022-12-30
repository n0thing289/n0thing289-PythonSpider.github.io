import asyncio
import aiohttp
from lxml import etree
"""
1.指定url
2.发起请求
3.数据解析
4.数据持久化
"""
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"

    }


async def task1():
    """你现在在分页中，准备点进一个详情页面查看"""
    """先爬取各分页源码中的每个详情页面的url"""
    for page in range(1,3):
        initial_url = 'https://acgdh.org/scy/cosplay/page/%d' % page
        async with aiohttp.ClientSession() as session:
            # 对其中一页发请求并且返回响应数据
            async with session.get(url=initial_url,headers=headers, ssl=False) as response:
                page_data = await response.text()
                # 实例化etree，拿到其中一分页中个详情页的url
                page_tree = etree.HTML(page_data)
                detail_url_list = page_tree.xpath('//div[@class="list-grid list-grid-padding"]/div[@class="list-item card"]/div[@class="media media-3x2 rounded col-4 col-md-4"]')
    return detail_url_list


async def task2(detail_url_list):
    """你现在在某一个详情页面中，准备爬取这个页面下所有的图片url"""
    """拿到某一详情页面源码中，图片的url"""
    await asyncio.sleep(10)
    for a in detail_url_list:
        detail_url = a.xpath('./a/@href')[0]
        title_name = a.xpath('./a/@title')[0]

        if title_name == '动漫磁力搜索引擎':
            continue  # 条件成立时，不执行后面代码，回到循环头继续进行循环
        print(detail_url)
        print(title_name)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=detail_url,headers=headers, ssl=False) as response:
                detail_page_data = await response.text()
                # 现在拿到了某一详情页面的源码，进行数据解析，解析出每张图片的url
                detail_tree = etree.HTML(detail_page_data)
                img_url_list = detail_tree.xpath('//div[@class="panel-body single mt-2"]/p')
    return img_url_list


async def main():
    t1 =  asyncio.create_task(task1())
    print('t1完成了码', t1.done())
    t2 = asyncio.create_task(task2(t1.result()))
    # print('t2完成了码', t2.done())

    # tasks = [t1,t2]
    await t1


    print("完成")


if __name__ == "__main__":
    asyncio.run(main())






