import random

class create_data():

    def randam_data(start_num, end_num, len_num):

        test_data = []

        while len(test_data) != len_num:

            num = random.randint(start_num, end_num)

            if num not in test_data:
                test_data.append(num)
        
        return test_data