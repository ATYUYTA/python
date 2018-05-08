import threading
import multiprocessing
from queue import Queue
import copy
import time

c=0

def work1():
    global c,lock
    for i in range(10):
        global c
        c+=1
        print('a',c)
    
def work2():
    global c,lock

    for i in range(10):
        c+=10
        print('b',c)


def main():
    c=0
    a=threading.Thread(target=work1)
    b=threading.Thread(target=work2)
    e=multiprocessing.process(target=work1)
    d=multiprocessing.process(target=work2)
    e.start()


if __name__=='__main__':
    main()
