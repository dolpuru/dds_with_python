N = 4
stages = [4,4,4,4,4]

temp_2 = 0
answer = []
dic = {}
resuly = []
s_p = len(stages)
for i in range(1, N+1):
    temp_1= 0
    
    for j in stages:
        if i >= j:
            temp_1 += 1
    temp_1 = temp_1 - temp_2
    if temp_1 == 0:    
        dic[i] = 0
    else:           
        dic[i] = temp_1/s_p 
    temp_2 += temp_1
    s_p = s_p-temp_1

    print(temp_1, s_p)
print (dic)
result = sorted(dic.items(),key = lambda x:x[1],reverse = True)
for i in result:
    answer.append(i[0])
print(answer)