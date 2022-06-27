def cheak(place):
    x = [-1,1,0,0,-1,1,-1,1,2,-2,0,0]
    y = [0,0,1,-1,1,1,-1,-1,0,0,2,-2]

    for i in range(5):
        for j in range(5):
            if place[i][j] =="P":
                 for c in range(12):
                    if 0 <= i+x[c] <5 and 0 <= j+y[c] < 5:
                        if place[i+x[c]][j+y[c]] == 'P':    
                            if x[c] + y[c] == 0 or abs(x[c] + y[c]) == 2:
                                if x[c] == -1 and y[c] == 1:
                                    if place[i-1][j] != "X" or place[i][j+1] !="X":   return 0
                                elif x[c] == 1 and y[c] == 1:
                                    if place[i][j+1] != "X" or place[i+1][j] !="X":   return 0
                                elif x[c] == -1 and y[c] == -1:
                                    if place[i-1][j] != "X" or place[i][j-1] !="X":   return 0
                                elif x[c] == 1 and y[c] == -1:
                                    if place[i][j-1] != "X" or place[i+1][j] !="X":   return 0
                                elif abs(x[c]) == 2:
                                    if x[c] == 2:   
                                        if place[i+1][j] != "X":    return 0
                                    else:
                                        if place[i-1][j] != "X":    return 0
                                elif abs(y[c]) == 2:
                                    if y[c] == 2:   
                                        if place[i][j+1] != "X":    return 0
                                    else:
                                        if place[i][j-1] != "X":    return 0
                            else: 
                                return 0
    return 1
    
def solution(places):
    answer = []
    for n in range(len(places)):    answer.append(cheak(places[n]))
    return answer