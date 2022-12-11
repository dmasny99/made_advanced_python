import unittest
import asyncio
from unittest.mock import patch
import aiohttp
import fetcher


def read_urls_file(path_to_file):
    res = []
    with open(path_to_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            res.append(line)
    return res


class MyTestCase(unittest.IsolatedAsyncioTestCase):

    async def test_read_file(self):

        urls_q = asyncio.Queue(maxsize=10)
        task = asyncio.create_task(fetcher.read_file("urls.txt", urls_q))

        valid_urls = read_urls_file("urls.txt")

        for url in valid_urls:
            self.assertEqual(await urls_q.get(), url)
            urls_q.task_done()

        task.cancel()

    @patch("fetcher.worker", return_value=True)
    async def test_client_session(self, mock_worker):

        urls_q = asyncio.Queue(maxsize=10)
        read_urls = asyncio.create_task(fetcher.read_file("urls.txt", urls_q))

        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(mock_worker(urls_q, session))
                for _ in range(10)
                ]
            for task in tasks:
                self.assertTrue(await task)
            await urls_q.join()
        read_urls.cancel()

    @patch("fetcher.fetch_url")
    async def test_worker(self, mock_fetch_url):
        urls_q = asyncio.Queue(maxsize=10)
        await urls_q.put("valid_url")
        await urls_q.put(fetcher.DEATH_PILL)
        async with aiohttp.ClientSession() as session:
            mock_result = \
                "url='https://en.wikipedia.org/wiki/1799' len(data)=158429"
            mock_fetch_url.return_value = mock_result
            task = asyncio.create_task(fetcher.worker(urls_q, session))
            res = await task
            if isinstance(res, bool):  # got death pill
                self.assertTrue(res)
            else:
                self.assertEqual(res, mock_result)
        task.cancel()


if __name__ == '__main__':
    unittest.main()
