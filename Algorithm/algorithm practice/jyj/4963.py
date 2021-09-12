while 1:

  w, h =  map(int, input().split(' '))
  if w == 0 and h == 0 :
    break

  array = []
  for i in range(h):
    array.append(list(map(int, input().split(' '))))

  stack = []
  visited = [[0 for i in range(w)] for j in range(h)]
  count = 0
  for i in range(h):
    for j in range(w):
      if visited[i][j] == 0 and array[i][j] == 1:
        count+=1
        stack.append([i,j])

        while len(stack) > 0:
            [x, y] = stack.pop()
            if y < w and x < h and x >= 0 and y >= 0 and visited[x][y] == 0 and array[x][y] == 1:
              visited[x][y] = 1
              tmp = [
                [x-1,y-1],
                [x-1, y],
                [x-1, y+1],
                
                [x, y-1],
                [x, y+1],

                [x+1, y-1],
                [x+1, y],
                [x+1, y+1],
              ]
              for tmp_ in tmp:
                x_ = tmp_[0]
                y_ = tmp_[1]
                if y_ < w and x_ < h and x_ >= 0 and y_ >= 0 and visited[x_][y_] == 0 and array[x_][y_] == 1 :
                  stack.append([x_,y_])

  print(count)
        
