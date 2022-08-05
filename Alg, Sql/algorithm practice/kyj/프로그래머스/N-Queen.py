def solution(n):
    answer = 0
    board = [0 for i in range(n)]
    
    def Queen(count):
        nonlocal answer
        if count == n:
            answer += 1
            return 
        else:
            for x in range(n):
                board[count] = x
                for y in range(count):
                    if board[y] == x or abs((x-board[y])/(count-y)) == 1:
                        break
                else: Queen(count+1)
    Queen(0)
    return answer
    
# def solution(n):
#     answer = 0
#     row = [0] * n

#     def Queen(y):
#         nonlocal answer
#         if y == n:
#             answer +=1
#             return
#         else:
#             for i in range(n):
#                 row[y] = i
#                 # 넣어서 되는지 확인
#                 for j in range(y):
#                     if row[y] == row[j] or abs((row[y] - row[j]) / (y - j)) == 1:
#                         break
#                 else:
#                     Queen(y+1)

#     Queen(0)

#     return answer

print(solution(4))
