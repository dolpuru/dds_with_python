input2=input().split(' ')
n = int(input2[0])
m=int(input2[1])
o=int(input2[2])

array = [[1 for i in range(15)] for j in range(15)]

for i in range(1, 15):
  for j in range(1, 15):
    array[i][j] = array[i-1][j] + array[i][j-1]
if o != 0:
  o_m = m-1 if o % m == 0 else o % m -1
  o_n = int((o-1) / m)
else:
  o_m = 0
  o_n = 0

f_n = n - o_n -1
f_m = m - o_m - 1

result = array[o_n][o_m] * array[f_n][f_m]
print(result)
