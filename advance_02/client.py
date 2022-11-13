import socket
import queue
import threading

def send_url(url_que, stop_client_que, sock_send, sock_recv):
    while True:
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
            if stop_client_que.empty():
                break
            stop_client_que.get()
            if answ not in ['', '###']:
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

def start_client(thread_num = 5, url_path = 'urls.txt'):

    url_que = queue.Queue() 
    stop_client_que = queue.Queue()
    sock_send, sock_recv = create_sockets()
    with open(url_path, 'r') as f:
        urls = f.readlines()
    for url in urls:
        url_que.put(url)
        stop_client_que.put(1) # will be used as a flag for a connection close

    threads = [threading.Thread(target = send_url, args=(url_que, stop_client_que, sock_send, sock_recv))\
        for _ in range(thread_num)]
    
    for th in threads:
        th.start()
    
    for th in threads:
        th.join()

    sock_send.close()
    sock_recv.close()
    print('===Connection closed===')

if __name__ == '__main__':
    #TODO add cmd line parser
    start_client()
    