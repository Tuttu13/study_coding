def hash(key):
    h = 0
    for i in key:
        if i != " ":
            h = h + ord(i)
    return(h%1000)

print("convert strings to hash")
print("do nothing")

while True:

    s = input("submit strings")

    if s == "":
        break
    print(s, "→ hash value", hash(s))
