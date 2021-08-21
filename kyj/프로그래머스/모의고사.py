answers = [1,2,3,4,5]
n = len(answers)
answer = []
dic = {}
p1 = [1,2,3,4,5] * (n//5+1)
p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (n//8 +1)
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *(n//10 + 1)

for i in range(n):
    if p1[i] == answers[i]:
        p1[i]=0
    if p2[i] == answers[i]:
        p2[i]=0
    if p3[i] == answers[i]:
        p3[i]=0
dic[1] = p1.count(0)
dic[2] = p2.count(0)
dic[3] = p3.count(0)
for k,v in dic.items():
    if max(dic.valuse()) == v:
        answer.append(k)
print(answer)
