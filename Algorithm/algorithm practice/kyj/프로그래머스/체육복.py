n = 5
lost = [2, 4]
reserve =[1, 3, 5]
answer = 0
dic = {}
for i in range(n):
    i = i +1
    dic[i] = 1
for i in lost:
    dic[i] -= 1
for i in reserve:
    dic[i] += 1
for k,v in dic.items():
    if dic[k] ==2:
        if k == 1:
            if dic[2] ==0:
                dic[2]=1
                dic[1]=1
        elif k ==n:
            if dic[k-1] ==0:
                dic[k-1] = 1
                dic[k] = 1
        else:
            if dic[k-1] ==0:
                dic[k-1] = 1
                dic[k] = 1
            elif dic[k+1] ==0:
                dic[k+1]=1
                dic[k] = 1
            elif dic[k-1] ==0 and dic[k+1] ==0:
                dic[k-1] = 1
                dic[k] = 1

for i in dic.values():
    if i == 1 or i == 2:
        answer += 1
print(answer)