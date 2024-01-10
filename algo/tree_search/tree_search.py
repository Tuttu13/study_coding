import random

class tree_search():


    def create_data(self, range_num):

        start = 1
        end = 10

        node = []

        while len(node) == 8:

            if len(sub_date) != 3:

                sub_date = []
                target_num = random.randint(start, end)
                sub_date.append()

                if None not in sub_date:
                    sub_date.append(None)

            node.append(main_date)

        
    
    def main():

        range_num:int = 10

        data_list = tree_search.create_data(range_num)
        print(data_list)
        data_num = len(data_list)
        key = 60

        for i in range(data_num):
            if data_list[i] == key:
                print("data_list[{0}] is {1}".format(i, key))
                break
            else:
                print("key : {0} is Nothing".format(key))
                continue

    
tree_search.main()