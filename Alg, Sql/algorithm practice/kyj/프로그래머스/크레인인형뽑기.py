board = [[0, 2, 0], [1, 2, 0], [2, 2, 1]]
moves = [1, 2, 2, 2, 1, 3]
li = [-1]
answer = 0
for i in moves:
    i = i-1
    for j in range(len(board)):
        if board[j][i] == 0:
            continue
        else:
            if li[-1] == board[j][i]:
                answer += 2
                board[j][i] = 0
                li.pop()
            else:
                li.append(board[j][i])
                board[j][i] = 0
            break
print(answer)

