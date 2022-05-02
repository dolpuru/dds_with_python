import itertools

N, M = map(int,input().split())
num = list(map(int,input().split()))

answer = 0
dif = 100000

li = list(itertools.combinations(num,3))

for i in li:
    if M - sum(i) < dif and M - sum(i) >= 0:
        dif = M - sum(i) 
        answer = sum(i)
    if dif == 0:    break

print(answer)