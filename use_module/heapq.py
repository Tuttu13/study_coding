def heapq():
    data = [100, 78, 10, 50, -1, 7, 2, 1]
    print(data, "start_data")

    data.sort()
    print(data, "end_data")


def sort_reverse():
    data = [
        "egg", "cat", "boy", "dog", "apple", "fire"
    ]
    new_data = sorted(data, reverse=True)
    print(data, "start")
    print(new_data, "end_data")

heapq()
sort_reverse()