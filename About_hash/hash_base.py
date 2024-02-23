HASh = 5
name = [None]*HASh
tel = [None]*HASh

def hash(key):
    h = 0
    for i in key:
        h = h + ord(i)
    return h%HASh

while True:

    n = input("type name")
    if n == "":
        break

    t = input("type tel")
    
    h = hash(n)
    name[h] = n
    tel[h] = t
    print("hash value", h, "completed")

while True:
    n = input("what name is searching ???")

    if n == "":
        break
    h = hash(n)

    if name[h] == n:
        print(n + "'s tel is " + tel[h])
    
    else:
        print("nothing")

