from cmn_create_data import create_data as cd

data_list = cd.randam_not_dep_data(15)

class quick_sort():
    
    def quick_sort(left, right):

        i = left
        j = right
        p = data_list[(left+right)//2]

        while True:
            while data_list[i] < p:
                i = i + 1
            while data_list[j] > p:
                j = j - 1
            if i >= j:
                break
            data_list[i], data_list[j] = data_list[j], data_list[i]

            i = i + 1
            j = j - 1
        
        if left > i-1:
            quick_sort.quick_sort(left, i-1)
        if right > j+1:
            quick_sort.quick_sort(j+1, right)


quick_sort.quick_sort(left=0, right=len(data_list)-1)