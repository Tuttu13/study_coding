class merge_sort():

    def merge_sort():

        a, b = [1, 3, 4, 7, 8, 9], [0, 2, 5, 6]

        a_num, b_num = len(a), len(b)

        c = [0]*(a_num + b_num)

        i, j, p = 0, 0, 0

        print("a data is {0}. b data is {1}.".format(a, b))

        while i < a_num and j < b_num:
            if a[i] <= b[j]:
                c[p] = a[i]
                i += 1
                p += 1
            else:
                c[p] = b[j]
                j += 1
                p += 1

        while i < a_num:
            c[p] = a[i]
            i += 1
            p += 1

        while i < b_num:
            c[p] = b[j]
            j += 1
            p += 1

        print(c, "done")

merge_sort.merge_sort()
        

