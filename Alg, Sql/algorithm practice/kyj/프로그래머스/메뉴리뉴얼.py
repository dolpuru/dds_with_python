from itertools import combinations
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
answer = []
dic = {}
for i in range(len(orders)):
    orders[i] = set(orders[i])

for a,b in combinations(orders,2):
    temp = sorted(list(a&b))
    if len(temp) >= course[0]:
        for c in course:
            for m in combinations(temp,c):
                menu = ''.join(list(m))
                if menu in dic:
                    dic[menu] += 1
                else: dic[menu] = 1
dic = sorted(dic.items(), key = lambda x: [len(x[0]),x[1]])

cr = dic[-1]
max_ = dic[-1][1]
while dic:
    menu, n = dic.pop()
    if len(menu) != cr:
        cr = len(menu)
        max_= n
        answer.append(menu)
    elif n==max_: answer.append(menu)
print(sorted(answer))
        