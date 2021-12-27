s = "a B z"
n = 4


li = list(s)
for i in range(len(li)):
    if li[i] != " ":
        li[i] = ord(li[i])

for i in range(len(li)):
    if li[i] != " " and 65 <= li[i] <= 90:
        li[i] += n
        if li[i] > 90:
            temp = li[i] - 91
            li[i] = 65 + temp
    elif li[i] != " " and 97 <= li[i] <= 122:
        li[i] += n
        if li[i] > 122:
            temp = li[i] - 123
            li[i] = 97 + temp
        
for i in range(len(li)):
    if li[i] != " ":
        li[i] = chr(li[i])
            
print( ''.join(li))