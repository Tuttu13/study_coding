import queue

MAX_RANGE = 10

def use_queue():

    print("queue")

    p = queue.Queue()
    
    for i in range(MAX_RANGE):
        p.put(i)
    for i in range(MAX_RANGE):
        print(p.get(), end="→")

def use_stack():

    print("stack")

    s = queue.LifoQueue()

    for i in range(MAX_RANGE):
        s.put(i)
    for i in range(MAX_RANGE):
        print(s.get(), end="→")


use_queue()
use_stack()
