import socket
import threading
import queue
import requests
from bs4 import BeautifulSoup
import json
import re

def create_connection(host = '', port = 2222):
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
        urls = conn_recv.recv(4096).decode().split('\n')
        for url in urls:
            if url != '':
                que.put(url)
                if url == '###':
                    return

def run_worker(que, conn_send, num_processed_urls, k):
    while True:
        url = que.get()
        if url == '###':
            que.put('###') # dead pill
            conn_send.send(url.encode())
            break
        try:
            req = requests.get(url)
        except:
            answ = json.dumps({url: 'error occured'})
        soup = BeautifulSoup(req.text, features = 'html.parser')
        words = re.findall(r'[A-Za-z]+', soup.text)
        unique_words = dict(zip(words, [words.count(i) for i in words]))
        res = sorted(unique_words.items(), key=lambda x: -x[1])[:k]
        answ = json.dumps({url: {item[0]: item[1] for item in res}})
        conn_send.send(answ.encode())

        n_urls = num_processed_urls.get() + 1
        num_processed_urls.put(n_urls)
        print(f'Processed urls: {n_urls}')


def start_server(w = 3, k = 10):
    que = queue.Queue()
    num_processed_urls = queue.Queue()
    num_processed_urls.put(0)

    conn_recv, conn_send, sock_recv, sock_send = create_connection()

    master_thread = threading.Thread(target = run_master, args=(conn_recv, que))
    worker_threads = [threading.Thread(target=run_worker, 
                                       args=(que, conn_send, num_processed_urls, k)) for _ in range(w)]

    for th in worker_threads:
        th.start()

    master_thread.start()

    for th in worker_threads:
        th.join()
    master_thread.join()
    
    sock_recv.close()
    sock_send.close()
    print('===Connection closed===')

if __name__ == '__main__':
    ## TODO add cmd line parser
    start_server()