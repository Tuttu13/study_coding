from cmn_create_data import create_data as cd


class insert_sort():

    def insert_sort_1():

        start_num = input("select start number")
        end_num = input("select end number")

        if 0 == int(start_num):
            len_num = (int(end_num) - int(start_num)) + 1
        else:
            len_num = int(end_num) - int(start_num)

        data_llst = cd.randam_data(int(start_num), int(end_num), len_num)
        print(data_llst, "created data")
        list_num = len(data_llst)

        for i in range(1, list_num):
            tmp = data_llst[i]
            j = i
            while 0 < j and tmp < data_llst[j - 1]:
                data_llst[j] = data_llst[j - 1]
                j = j - 1
            data_llst[j] = tmp

        print(data_llst, "done")
    
insert_sort.insert_sort_1()