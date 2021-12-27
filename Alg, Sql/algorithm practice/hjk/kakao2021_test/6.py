def solution(board, skill):
    for i in range(len(skill)):
        s, x1,y1 ,x2, y2, d= skill[i]
        
        for xx in range(x1, len(board)):
            for yy in range(y1, len(board[xx])):
                if s == 1:
                    if xx>= x1 and yy >= y1 and xx <= x2 and yy<= y2:
                        board[xx][yy] -= d
                
                else:
                    if xx>= x1 and yy >= y1 and xx <= x2 and yy<= y2:
                        board[xx][yy] += d
        
    answer = 0    
    for xx in range(len(board)):
            for yy in range(len(board[xx])):
                if board[xx][yy] >= 1:
                    answer += 1

        
    return answer