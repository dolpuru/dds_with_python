# 시간초과 
# def backt(x, y, word):
#     global result
#     check = 0
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0<= nx < n and 0<= ny < m and words[nx][ny] not in word:
#             backt(nx, ny, word+words[nx][ny])
#         else:
#             check += 1
# 재귀 형식이라 예전 값들까지 다 확인을 해본다.
#     if check == 4:
#         result = max(result, len(word))
#         return

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# n, m = map(int, input().split())
# words = [list(input()) for _ in range(n)]
# result = 0
# backt(0, 0, words[0][0])
# print(result)
import sys

R, C =map(int, sys.stdin.readline().split())
board = [[False for _ in range(C+2)]]
visited = []
max_cnt = -1

# 사방을 False로 만듦
for _ in range(R):
    line = [False]
    line.extend(list(sys.stdin.readline().rstrip()))
    line.append(False)
    board.append(line)
board.append([False for _ in range(C+2)])

def bfs(board, x, y):
    global max_cnt
    queue = set()
    queue.add((x,y, board[x][y]))
    pos_x = [0, -1, 1, 0]
    pos_y = [-1, 0, 0, 1]
    while queue:
        x, y, alpabets = queue.pop()
        if max_cnt < len(alpabets): max_cnt = len(alpabets)

        for i in range(4):
            new_x = x + pos_x[i]
            new_y = y + pos_y[i]
            if board[new_x][new_y] is False or board[new_x][new_y] in alpabets:
                continue
            else:
                queue.add((new_x, new_y, alpabets + board[new_x][new_y]))


bfs(board, 1, 1)
print(max_cnt)