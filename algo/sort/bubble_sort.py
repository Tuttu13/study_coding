import random

class bubble_sort_1():

    def create_data():

        test_data = []

        while len(test_data) != 10:

            num = random.randint(0, 9)

            if num not in test_data:
                test_data.append(num)
        
        return test_data


    def bubble_sort():

        test_data = bubble_sort_1.create_data()
        test_num = len(test_data)

        print(test_data, "start")

        for i in range(0, test_num-1):
            for j in range(test_num-1, i, -1):
                if test_data[j] < test_data[j-1]:
                    test_data[j], test_data[j-1] = test_data[j-1], test_data[j]

        print(test_data, "done")
    
bubble_sort_1.bubble_sort()