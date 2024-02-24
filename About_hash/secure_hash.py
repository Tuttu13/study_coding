import hashlib

print("genarate hash with SHA-256")
print("nothing end")

while True:
    s = input("submit strings")
    if s == "":
        print("END")
        break
    h = hashlib.sha256(s.encode()).hexdigest()
    print(h)