m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


li = [[] for i in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        board[j] = list(board[j])
        li[i].append(board[j][i])

for i in range(n):
    li[i] = li[i][::-1]
    
while 1:
    index = []
    for i in range(n):
        for j in range(len(li[i])):
            try:
                if li[i][j] == li[i+1][j] == li[i+1][j+1] == li[i][j+1]:
                    index.extend([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
            except: continue
    index = list(set(index))
    index.sort()
    for i,j in index[::-1]:
        del li[i][j]
    answer += len(index)
    if  len(index)==0:    break

print(answer)

