n = int(input())
lq =list(map(int,input().split()))
lq.sort()
p1 = 0
p2 = n-1
result = abs(lq[p1] + lq[p2])
answer = [lq[p1] , lq[p2]]
#-99, -2, -1 ,4, 98 

while p1 < p2 :
    temp = lq[p1]+lq[p2]
    if result > abs(lq[p1]+lq[p2]) :
        result = abs(lq[p1]+lq[p2])
        answer[0] = lq[p1]
        answer[1] = lq[p2]
        if result == 0:
            break
    if temp > 0:
        p2 -= 1
    else : 
        p1 += 1

print(answer[0],answer[1])