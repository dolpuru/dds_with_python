row = 12
col = 6
pattern_x = [1, -1, 0, 0]
pattern_y = [ 0, 0, 1, -1]
from collections import deque
def bfs(x, y, color):
    global array, visited, tmp_array
    if x >= row or x < 0 or y >= col or y <0 or array[x][y] != color or visited[x][y]:
        return 0
    
    tmp_array.append([x, y])
    visited[x][y] = 1
    sum_value = 1
    for i in range(4):
        sum_value += bfs(x + pattern_x[i], y+pattern_y[i], color)

    return sum_value

def func(array_):
    global array, visited, tmp_array
    array = array_
    check = True
    count = 0
    while check:
        check = False
        visited = [[0 for i in range(col)] for i in range(row)]
        for i in range(row-1, -1, -1):
            for j in range(col):
                if not visited[i][j] and array[i][j] != '.':
                    tmp_array = []
                    if bfs(i, j, array[i][j]) >= 4:
                        check=True
                        for k in tmp_array:
                            array[k[0]][k[1]] = '.'

        new_array = [[] for i in range(col)]
        for j in range(col):
            for i in range(row):
                if array[i][j] != '.':
                    new_array[j].append(array[i][j])

        array = [['.' for i in range(col)] for j in range(row)]
        for j in range(col):
            for i in range(row-1, -1, -1):
                if not new_array[j]:
                    break
                array[i][j] = new_array[j].pop()
        if check:
            count += 1
    print(count)

if __name__ == '__main__':
    input_value = []
    for i in range(row):
        input_value.append(list(input()))

    func(input_value)

