from cmn_create_data import create_data as cd

len_num = 15
test_data = cd.randam_not_dep_data(len_num)

class merge_sort():

    def merge_sort(left, mid , right):


        c = [0]*(right - left)

        i, j, p = left, mid, 0

        while i < mid and j < right:
            if test_data[i] <= test_data[j]:
                c[p] = test_data[i]
                i += 1
                p += 1
            else:
                c[p] = test_data[j]
                j += 1
                p += 1

        while i < mid:
            c[p] = test_data[i]
            i += 1
            p += 1

        while j < right:
            c[p] = test_data[j]
            j += 1
            p += 1
        
        for n in range(left, right):
            test_data[n] = c[n - left]

        print(c, "done")


print(test_data, "start")
s = 2

while s <= len_num:

    loop = len_num//s
    parts = len_num%s

    for i in range(loop):
        merge_sort.merge_sort(i*s, i*s+(s//2), i*s+s)
    if 0 < parts:
        merge_sort.merge_sort((loop-1)*s, loop*s, len_num)

    s = s * 2

print(test_data, "end")


        

