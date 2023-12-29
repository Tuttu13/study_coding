import random

class linear_search():

    def create_data(range_num):

        data_list:list = [
            ["佐藤", "121-212-111"],
            ["鈴木", "777-888-999"],
            ["宮下", "444-555-666"],
            ["高橋", "111-222-333"],
            ["豊川", "000-999-999"]
        ]
        
        return data_list
    
    def main():

        range_num:int = 10

        data_list = linear_search.create_data(range_num)
        print(data_list)
        data_num = len(data_list)
        select_name = input("whose name ???")

        i = 0

        while i < data_num and data_list[i][0] != select_name:
            i += 1
        if i == data_num:
            print("nothing")
        else:
            target_data = data_list[i]
            print(target_data[0] + "'s phone number is " + target_data[1])

linear_search.main()