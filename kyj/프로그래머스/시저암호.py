s = "a B z"
n = 4


li = list(s)
for i in range(len(li)):
    if li[i] != " ":
        li[i] = ord(li[i])

for i in range(len(li)):
    if li[i] != " " and 90 <li[i] + n <97:
        li[i] = 65 + n
    elif li[i] + n == 122:
        li[i] = 97 + n
    elif li[i] != " ":
        li[i] += n

for i in range(len(li)):
    if li[i] != " ":
        li[i] = chr(li[i])
    

print(li)