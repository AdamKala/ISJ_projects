import asyncio
import aiohttp

async def download_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response.status, url
    except Exception as e:
        if isinstance(e, aiohttp.ClientError):
            return 'aiohttp.ClientError', url
        return type(e).__name__, url


async def get_urls(urls):
    try:
        tasks = [asyncio.create_task(download_url(url)) for url in urls]
        results = await asyncio.gather(*tasks)
        ordered_results = []
        for url in urls:
            for res in results:
                if res[1] == url:
                    ordered_results.append(res)
                    break
        return ordered_results
    except aiohttp.ClientError as e:
        return type(e).__name__, urls


if __name__ == '__main__':
    urls = ['https://www.fit.vutbr.cz', 'https://www.szn.cz', 'https://www.alza.cz', 'https://office.com', 'https://aukro.cz']
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    res = asyncio.run(get_urls(urls))
    print(res)
    