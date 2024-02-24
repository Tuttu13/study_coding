print("choose natural num which b is bigger than a")
a = int(input("a = "))
b = int(input("b = "))

while True:
    r = a%b
    if r == 0:
        print("its number is the greatest common divisor", b)
        break
    a = b
    b = r
