import collections

n = int(input())

dp = [0 for i in range(n+1)]
complate = [0, ]
origin_complate = [0, ]
condition = [0, ]

for i in range(1, n+1):
    input_ = list(map(int, input().split(' ')))[:-1]
    complate.append(input_[0])
    origin_complate.append(input_[0])
    condition.append(collections.deque(input_[1:]))

while 1:
    swi=0
    for i in range(1, n+1):
        if len(condition[i]) == 0:
            dp[i] = complate[i]
        else:
            swi = 1
            c = condition[i].popleft()
            if dp[c] == 0:
                condition[i].appendleft(c)
            else:
                complate[i] = max(origin_complate[i]+dp[c],complate[i]) 
        
    if(swi==0):
        break

for i in range(1, n+1):
    print(dp[i])
