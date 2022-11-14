import io
import unittest
import multiprocessing
import server
import client
import sys
import os
import time

# I tried to do it with subprocess and failed
# https://stackoverflow.com/questions/52435965/what-is-the-difference-between-os-devnull-and-subprocess-pipe
# so I decided to use os.devnull and multiprocessing


class ClientServerTest(unittest.TestCase):
    def redirect_stdout_to_null(
        type=None,
        work_threads=None,
        k=None,
        client_threads=None,
        urls_path=None,
    ):
        with open(os.devnull, "w") as null:
            out = sys.stdout
            sys.stdout = null
            if type == "server":
                server.start_server(work_threads, k)
            elif type == "client":
                client.start_client(client_threads, urls_path)
            sys.stdout = out

    def get_data_from_stdout(
        type=None,
        que=None,
        work_threads=None,
        k=None,
        client_threads=None,
        urls_path=None,
    ):
        tmp_stdout = io.StringIO(initial_value="", newline="\n")
        stdout = sys.stdout
        sys.stdout = tmp_stdout
        if type == "server":
            server.start_server(work_threads, k)
            que.put(tmp_stdout.readlines())

        elif type == "client":
            client.start_client(client_threads, urls_path)
        # tmp = tmp_stdout.getvalue()
        que.put(tmp_stdout.readlines())
        sys.stdout = stdout
        # print(tmp_stdout)
        tmp_stdout.close()

    def test_correct_response_on_client(self):
        que = multiprocessing.Queue()
        server_proc = multiprocessing.Process(
            target=self.redirect_stdout_to_null,
            kwargs={"type": "server", "work_threads": 5, "k": 6},
        )
        client_proc = multiprocessing.Process(
            target=self.get_data_from_stdout,
            kwargs={
                "type": "client",
                "que": que,
                "client_threads": 3,
                "urls_path": "test_urls.txt",
            },
        )

        # proc_1.start()
        server_proc.start()
        time.sleep(1)
        client_proc.start()

        server_proc.join()
        client_proc.join()

        # answ1 = (
        #     '{"https://en.wikipedia.org/wiki/Main_Page": '
        #     '{"the": 50, "of": 39, "a": 25, "in": 22, '
        #     '"and": 21, "Wikipedia": 15, "that": 13}}'
        # )
        # answ2 = (
        #     '{"https://www.open.ru/": '
        #     '{"и": 44, "Открытие": 15, "в": 11, "на": 10, '
        #     '"Банк": 9, "по": 9, "Узнать": 8}}'
        # )
        # answ3 = (
        #     '{"https://www.msu.ru/": '
        #     '{"и": 58, "мая": 48, "в": 47, "МГУ": 46, '
        #     '"по": 38, "Универсиада": 32, "Ломоносов": 28}}'
        # )
        # answ4 = (
        #     '{"https://cs.msu.ru/": '
        #     '{"МГУ": 10, "по": 9, "мая": 7, "апреля": 6, '
        #     '"с": 6, "ВМК": 5, "и": 5}}'
        # )

        # results = sorted([s for s in queue.get().split("\n") if s])
        results = [s for s in que.get() if s]
        print(*results)


if __name__ == "__main__":
    unittest.main()
