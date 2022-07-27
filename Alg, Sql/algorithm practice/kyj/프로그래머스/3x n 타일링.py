def solution(n):
    answer = 0
    dp = [3,11]
    if n <= 4:  return dp[n//2-1]
    else:
        for i in range(2,n//2):
            dp.append((dp[i-1]*4-dp[i-2])%1000000007)
    return dp[-1]


print(solution(8))