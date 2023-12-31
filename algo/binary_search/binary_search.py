import random

class linear_search():

    def create_data(range_num, start, end):

        data_list:list = []
        
        while range_num != len(data_list):
            target_num = random.randint(start, end)
            if target_num not in data_list:
                data_list.append(target_num)
            else:
                pass

        data_list = sorted(data_list)
        
        return data_list
        # data_list = [random.randint(start, end) for _ in range(range_num)]

    def main():

        range_num:int = 15
        start = 1
        end = 100

        flg = False

        data_list = linear_search.create_data(range_num, start, end)
        data_num = len(data_list)
        target_num_str = input("select in {0} number".format(data_list))
        target_num = int(target_num_str)
        
        left = 0
        right = data_num - 1

        while left <= right:
            mid = (left+right)//2
            print("L={0}, M={1}, M={2}".format(left, mid, right))

            if data_list[mid] == target_num:
                flg = True
                print("data[{0}] is {1}".format(mid, target_num))
                break
            if data_list[mid] < target_num:
                left = mid + 1
            else:
                right = mid - 1
        if flg == False:
            print("Not found target data")
    
linear_search.main()