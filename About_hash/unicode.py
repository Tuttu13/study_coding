print("Unicode of A", ord('A'))
print("Unicode of あ", ord('あ'))
print("Unicode of 33", chr(33))
print("Unicode of 123456", chr(123456))

print("---------------")

while True:
     s = input("submit strings")
     if len(s) != 1:
          break
     print("Unicode of" + s, ord(s))