import socket
import argparse
import threading
import queue
import json
import re
from collections import defaultdict
import operator
import requests
from bs4 import BeautifulSoup

URLS_CNT = 0


def create_connection(host="", port=2222):
    sock_recv = socket.socket()
    sock_recv.bind((host, port))
    sock_recv.listen(1)

    sock_send = socket.socket()
    sock_send.bind((host, port + 1))
    sock_send.listen(1)

    conn_send, _ = sock_send.accept()
    conn_recv, _ = sock_recv.accept()

    return conn_recv, conn_send, sock_recv, sock_send


def run_master(conn_recv, que):
    while True:
        urls = conn_recv.recv(4096).decode().split("\n")
        for url in urls:
            if url != "":
                que.put(url)
                if url == "###":
                    return


def get_k_freq(words, k):
    words_dict = defaultdict(int)
    for word in words:
        words_dict[word] += 1
    res = dict(sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)[:k])
    return res


def run_worker(que, conn_send, locker, k):
    global URLS_CNT
    while True:
        url = que.get()
        if url == "###":
            que.put("###")  # dead pill
            conn_send.send(url.encode())
            break
        try:
            clenaed_url = url.replace("#", "")
            if clenaed_url != "":
                url = clenaed_url
            req = requests.get(url, timeout=3)
            soup = BeautifulSoup(req.text, features="html.parser")
            words = re.findall(r"[A-Za-z]+", soup.text)
            freq_dict = get_k_freq(words, k)
            answ = json.dumps({url: freq_dict})
        except:
            answ = json.dumps({url: "error"})
        finally:
            conn_send.send(answ.encode())
            print(answ)
            with locker:
                if "#" not in answ:
                    URLS_CNT += 1
                    print(f"Processed urls: {URLS_CNT}")


def start_server(worker_threads, k):
    que = queue.Queue()
    locker = threading.Lock()

    conn_recv, conn_send, sock_recv, sock_send = create_connection()

    master_thread = threading.Thread(target=run_master, args=(conn_recv, que))
    worker_threads = [
        threading.Thread(target=run_worker, args=(que, conn_send, locker, k))
        for _ in range(worker_threads)
    ]

    for thread in worker_threads:
        thread.start()

    master_thread.start()

    for thread in worker_threads:
        thread.join()

    master_thread.join()

    sock_recv.close()
    sock_send.close()
    print("===Connection closed===")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", type=str, required=True)
    parser.add_argument("-k", type=str, required=True)
    args = parser.parse_args()

    worker_threads = int(args.w)
    k = int(args.k)

    start_server(worker_threads, k)
