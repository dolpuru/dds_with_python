N, M = map(int, input().split(' '))
K = int(input())

k_array = [[0 for i in range(N*2+1)] for j in range(M*2+1)]

for i in range(K):
  a, b, c, d = map(int, input().split(' '))
  k_array[b+d][a+c] = -1

k_array[0][0] = 1

for i in range(2, N*2+1, 2):
  if k_array[0][i-1] == -1:
    break
  k_array[0][i] = 1

for i in range(2, M*2+1, 2):
  if k_array[i-1][0] == -1:
    break
  k_array[i][0] = 1

for i in range(2, M*2+1, 2):
  for j in range(2, N*2+1, 2):
    if k_array[i-1][j] != -1:
      k_array[i][j] += k_array[i-2][j]
    if k_array[i][j-1] != -1:
      k_array[i][j] += k_array[i][j-2]


print(k_array[-1][-1])
