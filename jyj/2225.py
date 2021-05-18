
N, K = map(int, input().split(' '))
dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(1, N+1):
    dp[i][1] = 1

if K > 1:
    for i in range(1, N+1):
        dp[i][2] = i+1

for i in range(K+1):
    dp[1][i] = i



for i in range(2, N+1):
    for j in range(3, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1]%1000000000)
