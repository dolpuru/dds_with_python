def route(route, i,j):
    if route == 0:   
        j -= 1
        if j < 0:   j = n-1
    elif route == 1:   
        j += 1
        if j > n -1 :    j = 0
    elif route == 2:   
        i -= 1
        if i < 0:   i = m-1
    else: 
        i += 1
        if i > m -1 :    i = 0
    return  i, j
    
grid =	["RL", "SR"]
global n,m
n,m = len(grid[0]), len(grid)
answer = []
visited = [ [[0,0,0,0]for i in range(len(grid[0]))] for i in range(len(grid))]
#l, r ,u , d 
for _ in range(len(grid)):
    grid[_] = list(grid[_])

for c in range(m):
    for r in range(n):
        for k in range(4):
            if visited[c][r][k] != 0:   continue
            count = 0
            i,j,out = c,r,k
            while visited[i][j][out] != 1:
                visited[i][j][out] = count
                count += 1
                #경로설정
                if grid[i][j] == "S": pass
                elif grid[i][j] == "L":
                    if out == 0:   out = 3
                    elif out == 1:   out = 2
                    elif out == 2:   out = 0
                    else:   out = 1
                else:
                    if out == 0:   out = 2
                    elif out == 1:   out = 3
                    elif out == 2:   out = 1
                    else:   out = 0 
                
                i, j = route(out,i,j)
            answer.append(count-1)
            print(visited,answer)
print(answer)