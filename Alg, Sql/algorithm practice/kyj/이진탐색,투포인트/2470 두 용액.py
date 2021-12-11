N = int(input())
lq = list(map(int,input().split()))
lq.sort()

fst = 0
end = N - 1
answer = abs(lq[fst] + lq[end])
r1 = lq[fst]
r2 = lq[end]

while fst< end :
    temp = lq[fst] + lq[end]
    if answer > abs(lq[fst] + lq[end]):
        answer = abs(lq[fst] + lq[end])
        
        r1 = lq[fst]
        r2 = lq[end]
        if answer == 0:
            break
    if temp > 0:
        end = end -1
    else : 
        fst = fst + 1
print(r1 , r2)
