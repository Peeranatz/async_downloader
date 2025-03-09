import asyncio
import aiohttp
import time


async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} bytes from {url}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(session, url) for url in sites]
        await asyncio.gather(*tasks)


async def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80  # สร้างลิสต์ URL ซ้ำ 80 ครั้ง

    print("Starting downloads")
    start_time = time.time()

    await download_all_sites(sites)

    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


if __name__ == "__main__":
    asyncio.run(main())
