import random

class linear_search():

    def create_data(range_num):

        data_list:list = []
        
        for _ in range(range_num):
            target_num = random.randint(50, 80)
            data_list.append(target_num)

        # data_list = [random.randint(0, 1000) for _ in range(range_num)]
        
        return data_list
    
    def main():

        range_num:int = 10

        data_list = linear_search.create_data(range_num)
        print(data_list)
        data_num = len(data_list)
        key = 60
        
        i = 0
        while i < data_num and  data_list[i] != key:
            i += 1
        if i == data_num:
            print("not found value")
        else:
            print("data_list[{0}] is {1}".format(i, data_list[i]))

linear_search.main()