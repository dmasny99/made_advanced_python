import asyncio
import aiohttp
import aiofiles  # to read a file with urls in a coroutine
import click

DEATH_PILL = "###"


async def read_file(file_path, que):
    async with aiofiles.open(file_path, "r") as file:
        async for url in file:
            url = url.strip("\n")
            await que.put(url)


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        return (f"{url=} {len(data)=}")


async def worker(queue, session):
    while True:
        url = await queue.get()
        if url == DEATH_PILL:
            await queue.put(url)
            return True
        try:
            print(await fetch_url(url, session))
        except Exception:
            print("Something went wrong")
        finally:
            queue.task_done()


async def start_session(file_path, num_reqs):
    urls_q = asyncio.Queue(maxsize=num_reqs)
    read_urls = asyncio.create_task(read_file(file_path, urls_q))
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(urls_q, session))
            for _ in range(num_reqs)
        ]
        await urls_q.join()
        await read_urls
        for task in tasks:
            await task


@click.command()
@click.argument("num_reqs", nargs=1)
@click.argument("file_path", nargs=1)
def main(num_reqs, file_path):
    num_reqs = int(num_reqs)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_session(file_path, num_reqs))


if __name__ == "__main__":
    main()
