from cmn_create_data import create_data as cd


class heap_sort():

    def heap_sort():

        test_data = cd.randam_data(1, 99, 12)
        data_num = len(test_data)

        print(test_data, "start data")

        for i in range((data_num-1)//2, -1, -1):
            point = i
            count = (point*2)+1

            while count < data_num:

                if count < data_num-1 and test_data[count] < test_data[count+1]:
                    count += 1
                if test_data[count] <= test_data[point]:
                    break
                test_data[point], test_data[count] = test_data[count], test_data[point]

                point = count
                count = (point*2)+1
            
        print(test_data, "initial heap")

        del_num = data_num - 1

        while 0 < del_num:
            test_data[0], test_data[del_num] = test_data[del_num], test_data[0]

            point = 0
            count = (point*2)+1

            while count < del_num:
                if count < del_num-1 and test_data[count] < test_data[count+1]:
                    count += 1
                if test_data[count] <= test_data[point]:
                    break
                test_data[point], test_data[count] = test_data[count], test_data[point]
                point = count
                count = (point*2)+1

            del_num -= 1
        
        print(test_data, "end heap")

heap_sort.heap_sort()
