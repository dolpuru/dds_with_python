N, M, K = map(int, input().split(' '))
array = [[0 for i in range(M+1)] for j in range(N+1)]

for i in range(N+1):
  array[i][0]= 1
for i in range(M+1):
  array[0][i]= 1

for i in range(1, N+1):
  for j in range(1, M+1):
    array[i][j] = array[i-1][j] + array[i][j-1]

if array[N][M] < K:
  print(-1)

else:
  i = N
  j = M
  result = ''
  while i != 0 or j != 0:
    if i > 0 and j> 0:
      if K <= array[i-1][j]:
        i -=1
        result += 'a'
      else:
        K -= array[i-1][j]
        j-=1
        result += 'z'
    elif i >0 and j == 0:
      i -=1
      result += 'a'
    elif i == 0 and j > 0:
      j-=1
      result += 'z'

  print(result)
