import numpy as np
def count(arr):
    global answer
    if len(arr) == 1: 
        if arr[0] == 1: answer[1] +=1
        else:   answer[0] +=1   
        return 
    else:
        n = len(arr)//2
        lu,ld,ru,rd = arr[0][0],arr[n][0],arr[0][n],arr[n][n]
        #왼쪽 위
        for i in range(n):
            for j in range(n):
                if lu != arr[i][j]:  
                    count(arr[:n,:n])
                    break
            else:   continue
            break
        else:
            answer[lu] += 1
        
        #왼쪽 아래
        for i in range(n,len(arr)):
            for j in range(n):
                if ld != arr[i][j]:  
                    count(arr[n:,:n])
                    break
            else:   continue
            break
        else:
            answer[ld] += 1
        #오른쪽 위
        for i in range(n):
            for j in range(n,len(arr)):
                if ru != arr[i][j]:  
                    count(arr[:n,n:])
                    break
            else:   continue
            break
        else:
            answer[ru] += 1
        #오른쪽 아래
        for i in range(n,len(arr)):
            for j in range(n,len(arr)):
                if rd != arr[i][j]:  
                    count(arr[n:,n:])
                    break
            else:   continue
            break
        else:
            answer[rd] += 1
            
def solution(arr):
    global answer 
    answer= [0,0]
    arr=np.array(arr) 
    if np.sum(arr) == 0:   return [1,0]
    elif np.sum(arr)  == len(arr) * len(arr): return [0,1]
    else:
        count(arr)
        return answer

print(solution(	[[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))