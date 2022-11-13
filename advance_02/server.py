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
            # print(url)
            if url:
                que.put(url)
            if url == '###': # the end of correct data
                break

def run_worker(que, conn_send, locker, num_processed_urls, k):
    while True:
        print('worker started')
        url = que.get()
        if url == '###':
            que.put('###') # dead pill
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
        
        locker.acquire()
        num_processed_urls += 1
        print(f'processed urls {num_processed_urls}')
        locker.release()


def start_server(w = 10, k = 4):
    locker = threading.Semaphore(1)
    que = queue.Queue()
    num_processed_urls = 0

    conn_recv, conn_send, sock_recv, sock_send = create_connection()

    master_thread = threading.Thread(target = run_master, args=(conn_recv, que))
    worker_threads = [threading.Thread(target=run_worker, 
                                       args=(que, conn_send, locker, num_processed_urls, k)) for _ in range(w)]
    for th in worker_threads:
        th.start()

    master_thread.start()
    master_thread.join()

    for th in worker_threads:
        th.join()

    master_thread.start()
    master_thread.join()

    sock_recv.close()
    sock_send.close()

if __name__ == '__main__':
    ## TODO add cmd line parser
    start_server()