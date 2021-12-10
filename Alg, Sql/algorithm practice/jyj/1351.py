import math
N, P, Q = map(int, input().split(' '))

dp= []
index = []
def tree(num):
  global P
  global Q
  if num==0:
    return 1
  
  if index.count(num) == 0:
    val = tree(math.floor(num/P)) + tree(math.floor(num/Q))
    dp.append(val)
    index.append(num)
  else:
    return dp[index.index(num)]

  
  return val

print(tree(N))

