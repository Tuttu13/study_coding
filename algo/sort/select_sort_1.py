import random

class select_sort_1():

    def create_data():

        test_data = []

        while len(test_data) != 10:

            num = random.randint(0, 9)

            if num not in test_data:
                test_data.append(num)
        
        return test_data


    def select_sort():

        test_data = select_sort_1.create_data()

        for i in range(0, 9):
            m = i
            for j in range(i+1, 10):
                if test_data[j] < test_data[m]:
                    m = j
            test_data[i], test_data[m] = test_data[m], test_data[i]
            print(test_data, i+1)

        print(test_data, "done")
    
select_sort_1.select_sort()