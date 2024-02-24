def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

print("choose natural num which b is bigger than a")
a = int(input("a = "))
b = int(input("b = "))
print("the greatest common divisor is ", euclid(a, b))
