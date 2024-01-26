import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS="127.0.0.1"
SERVER_PORT=5005
NUM_WORKERS=15
segni={1:'+',2:'-',3:'*',4:'/',5:'%'}

def genera_richieste(address,port):
    start_time_thread=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
        primoNumero=float(random.randint(1,200))
        num_op=random.randint(1,5)
        operazione=segni[num_op]
        secondoNumero=float(random.randint(1,200))
        messaggio={'primoNumero': primoNumero,
                'operazione':operazione,
                'secondoNumero':secondoNumero}
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
        data=sock_service.recv(1024)
        print('Received', data.decode())


    end_time_thread=time.time()
    print(f"{threading.current_thread().name} execution time=", end_time_thread - start_time_thread)




if __name__=='__main__':
    #run your task using threads
    start_time=time.time()
    threads = [threading.Thread(target=genera_richieste,args=(SERVER_ADDRESS,SERVER_PORT,)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads ]
    end_time =time.time()


    print("Total threads time=", end_time - start_time)
