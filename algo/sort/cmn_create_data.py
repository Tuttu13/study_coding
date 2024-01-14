import random

class create_data():

    def randam_data():

        test_data = []

        while len(test_data) != 10:

            num = random.randint(0, 9)

            if num not in test_data:
                test_data.append(num)
        
        return test_data