text = "I'm learing Python. It's interesting!!!"
pattern = "Python"
tn = len(text)
pn = len(pattern)

flg = False

p = 0

while p <= tn-pn:
    c = 0
    for i in range(pn):
        if text[p+i] != pattern[i]:
            break
        c += 1

    if c == pn:
        flg = True
        break
    p += 1

print(text)
if flg == True:
    print(pattern + " is " + str(p+1) + " position" )
else:
    print("nothing") 