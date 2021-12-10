import time
start = time.time()  # 시작 시간 저장

input_ = [

      ["O", "O", "O", "O"],
      ["O", "O", "#", "O"],
      ["O", "O", "O", "O"],
      ["#", "O", "O", "O"],
      ["O", "O", "O", "#"],
      ["O", "#", "O", "O"],
      ["O", "O", "O", "#"],
      ["O", "#", "O", "O"],

]

'''
input_ = [
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
]
'''

SIZE = len(input_)
ROW_SIZE = len(input_)
COL_SIZE = len(input_[0])
max_value = 0
max_count = 0

array =  [[j for j in i] for i in input_]
visited = []
i=0
j=0
fin = 0

rows = [[]]
pointer = 0
while 1:
  if array[i][j] == "O":
    rows[pointer].append([i,j])
  elif array[i][j] == "#" and rows[-1] != []:
    rows.append([])
    pointer+=1
  
  i+=1
  if i>=ROW_SIZE:
    j+=1
    i=0
    if rows[-1] != []:
      rows.append([])
      pointer+=1

  if j>=COL_SIZE:
    break

rows = rows[:-1]
max_len = len(rows)
lens = []
point = []
count = 0
len_point = max_len-1
for i in rows:
  lens.append(len(i))
  point.append(0)

while_break = 0
while 1:
  j_array = []
  fail = 0
  for i in range(max_len):
    for j in j_array:
      if j[0] == rows[i][point[i]][0]: # 열이 겹치면 검사
        swi = 0
        for k in range(j[1]+1, rows[i][point[i]][1]):
          if array[j[0]][k] == "#":
            swi=1
        if swi == 0:
          fail = 1
    if fail ==1:
      break
    j_array.append(rows[i][point[i]])
  
  if fail == 0:
    count+=1

  for i in range(max_len-1, -1, -1):
    point[i]+=1
    if point[0] >= lens[0]:
      while_break = 1
      break
    elif point[i] >= lens[i]:
      point[i]=0
    else:
      break
  if while_break == 1:
    break
print(len(rows), count)
print("time :", time.time() - start)
