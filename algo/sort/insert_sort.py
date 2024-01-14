from cmn_create_data import create_data as cd


class insert_sort():

    def insert_sort_1():

        data_llst = cd.randam_data()
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