import random

class linear_search():

    def create_data(range_num):

        data_list:list = []
        
        for _ in range(range_num):
            target_num = random.randint(50, 100)
            data_list.append(target_num)

        # data_list = [random.randint(0, 1000) for _ in range(range_num)]
        
        return data_list
    
    def main():

        range_num:int = 10

        data_list = linear_search.create_data(range_num)
        data_num = len(data_list)
        key = 60

        for i in range(data_num):
            if data_list[i] == key:
                print("data [{0} is {1}]".format(data_list[i], key))
                break
            else:
                print("key{0} is Nothing".format(key))
                continue

    
linear_search.main()