import copy            
def solution(n, info):
    answer = [0,0,0,0,0,0,0,0,0,0,0]
    count, a_score, l_score= 0,0,0
    max_  = 0 
    
    for i in range(10):
        if info[i]: a_score += 10-i
    
    def dfs(a_score,l_score, idx,li):
        temp = copy.deepcopy(li)
        if idx >= 11:
            nonlocal max_
            nonlocal answer
            if max_ < l_score - a_score:
                max_ = l_score - a_score
                if sum(temp) < n:   temp[-1] = n - sum(temp)
                answer = temp
            return
        else:
            #피하고 다른 것
            dfs(a_score,l_score,idx+1,temp)
            # 어피치 것 뻇기
            if sum(temp) + info[idx] +1 <= n and info[idx] != 0:
                a_score -= 10- idx
                l_score += 10 - idx
                temp[idx] = info[idx] + 1
                dfs(a_score,l_score,idx+1,temp)
            elif info[idx] == 0:    #어피치가 안 쏜것
                l_score += 10 - idx
                temp[idx] = 1
                dfs(a_score,l_score,idx+1,temp)
    
    dfs(a_score,l_score,0,answer)
    
    return [-1] if answer == [0,0,0,0,0,0,0,0,0,0,0] else answer

print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))