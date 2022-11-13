import socket
import queue
import threading

def send_url(que, sock_send, sock_recv):
    while not que.empty():
        url = que.get()
        sock_send.send(url.encode())
        try:
            answ = sock_recv.recv(1024).decode()
            print(answ)
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

def start_client(thread_num = 10, url_path = 'urls.txt'):

    que = queue.Queue() 
    sock_send, sock_recv = create_sockets()

    with open(url_path, 'r') as f:
        urls = f.readlines()
    for url in urls:
        que.put(url)

    threads = [threading.Thread(target = send_url, args=(que, sock_send, sock_recv))\
        for _ in range(thread_num)]
    
    for th in threads:
        th.start()
    
    for th in threads:
        th.join()
    
    sock_send.close()
    sock_recv.close()

if __name__ == '__main__':
    #TODO add cmd line parser
    start_client()
    