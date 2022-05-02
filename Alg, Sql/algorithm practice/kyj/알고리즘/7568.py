N = int(input())
li = []
answer = {}
rank = 1
for i in range(N):
    kg, hei= map(int,input().split())
    li.append([i,kg,hei])

li.sort(key = lambda x : (x[1], x[2]))
li.reverse()

for i in range(len(li)):
    if i == len(li) - 1 :    
        
    if li[i][1] > li[i+1][1] and li[i][2] > li[i+1][2]:
        answer[li[i][0]] = rank
        rank += 1
    else: 
        answer[li[i][0]] = rank

print(li)
print(answer)