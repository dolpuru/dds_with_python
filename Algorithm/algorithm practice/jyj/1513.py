N, M, C = map(int, input().split(' '))

c_array = [list(map(int, input().split(' '))) for i in range(C)]

array = [[0 for j in range(M+1)] for i in range(N+1)]
for idx, c in enumerate(c_array):
    array[c[0]][c[1]] = idx+1


dp =[[[[0 for count in range(C+1)] for max_value in range(C+1)] for j in range(M+1)] for i in range(N+1)]

if array[1][1] == 0:
    dp[1][1][0][0] = 1
else:
    dp[1][1][array[1][1]][1] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        for max_value in range(C+1):
            for count in range(C+1):
                if array[i][j] != 0 and count != C:
                    if max_value <= array[i][j]:
                        dp[i][j][array[i][j]][count+1] += dp[i-1][j][max_value][count] + dp[i][j-1][max_value][count]
                else:
                    dp[i][j][max_value][count] += dp[i-1][j][max_value][count] + dp[i][j-1][max_value][count]


for i in range(C+1):
    hap = 0
    for j in range(C+1):
        hap+= dp[-1][-1][j][i]
    print(hap%1000007, end=' ')

'''

dp 배열 구성

N * M * max_value * count

dp[N][M][max_value][count] -> N x M 좌표에 여태까지의 최대값이 max_value 이면서 오락실을 count개 거친 경로의 개수

'''
