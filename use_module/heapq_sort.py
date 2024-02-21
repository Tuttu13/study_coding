import heapq
import random


def heapq_sort():
    n= 10
    data = [0]*n
    for i in range(n):
        data[i] = random.randint(i, 99)
    print(data, "start")

    heapq.heapify(data)
    print(data, "heap_constract_data")

    print("get from heap_constract_data")

    for i in range(n):
        v = heapq.heappop(data)
        print(v, end="→")
    print(data)

heapq_sort()