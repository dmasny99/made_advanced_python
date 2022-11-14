import socket
import queue
import threading
import argparse

STOP_CNT = 0

def send_url(url_que, locker, sock_send, sock_recv):
    global STOP_CNT
    while True:
        if STOP_CNT <= 1:
            break
        # to avoid broken pipe error 
        try:
            url = url_que.get()
            sock_send.send(url.encode())
            if url == '###':
                url_que.put('###')
        except:
            pass
        
        # to avoid broken pipe error 
        try:
            answ = sock_recv.recv(4096).decode()
            if answ != '' and '#' not in answ:
                print(answ)
                with locker:
                    STOP_CNT -= 1
        except: # crutchy code, did't find another solution
            pass


def create_sockets(addres = '', port = 2222):
    sock_send = socket.socket()
    sock_send.connect((addres, port))
    sock_send.settimeout(1)

    sock_recv = socket.socket()
    sock_recv.connect((addres, port + 1))
    sock_recv.settimeout(1)

    return sock_send, sock_recv

def read_txt(path):
    with open(path, 'r') as file:
        urls = file.readlines()
    return urls, len(urls) - 1
    

def start_client(thread_num, path):

    urls, len_urls = read_txt(path)
    global STOP_CNT
    STOP_CNT = len_urls


    url_que = queue.Queue() 
    locker = threading.Lock()

    sock_send, sock_recv = create_sockets()

    for url in urls:
        url_que.put(url)

    threads = [threading.Thread(target = send_url, args=(url_que, locker, sock_send, sock_recv))\
        for _ in range(thread_num)]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    sock_send.close()
    sock_recv.close()
    print('===Connection closed===')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('positionals', nargs='+')
    args = parser.parse_args()

    path = args.positionals[1]
    thread_num = int(args.positionals[0])
    
    start_client(thread_num, path)
    