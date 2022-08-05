#2022.08.02 코드
import copy

def solution(n, info):
    answer = [0 for i in range(11)]
    max_,apeachScore  = 0,0
    
    for i in range(len(info)):
        if info[i] != 0:  apeachScore += 10-i
    
    def dfs(apeachScore,lionScore,arrow,count,li):
        temp = copy.deepcopy(li)
        if count>=11 or arrow==0:  
            nonlocal max_
            nonlocal answer
            if arrow > 0:   temp[-1]=arrow
            if max_ < lionScore - apeachScore : 
                if arrow>0: answer[-1] = arrow
                max_ = lionScore - apeachScore
                answer = temp
            elif max_ == lionScore - apeachScore:
                a,b = 0,0
                for i in range(11):
                    if answer[i]:   a+=i
                    if temp[i]: b+=i
                if b>=a: answer = temp
            return
        else:
            # 넘기기
            dfs(apeachScore,lionScore,arrow,count+1,temp)
            #어피치보다 많이 쏘기
            if arrow-info[count]-1 >=0 and info[count] != 0:
                temp[count] = info[count] + 1
                dfs(apeachScore-(10-count),lionScore+(10-count),arrow-info[count]-1,count+1,temp)
            elif info[count] == 0:    #어피치가 안 쏜것
                lionScore += 10 - count
                temp[count] = 1
                dfs(apeachScore,lionScore,arrow-info[count]-1,count+1,temp)
    dfs(apeachScore,0,n,0,answer)
    return answer if answer != [0,0,0,0,0,0,0,0,0,0,0] and  max_ !=0  else [-1]
    
# import copy            
# def solution(n, info):
#     answer = [0,0,0,0,0,0,0,0,0,0,0]
#     count, a_score, l_score= 0,0,0
#     max_  = 0 
    
#     for i in range(11):
#         if info[i]: a_score += 10-i
    
#     def dfs(a_score,l_score, idx,li):
#         temp = copy.deepcopy(li)
#         if idx >= 11 or sum(temp) >= n:
#             nonlocal max_
#             nonlocal answer
#             if max_ < l_score - a_score:
#                 max_ = l_score - a_score
#                 answer = temp
#             elif max_ == l_score - a_score:
#                 a,b = 0,0
#                 for i in range(11):
#                     if answer[i]:   a+=i
#                     if temp[i]: b+=i
#                 if b>=a: answer = temp
#             return
#         else:
#             #피하고 다른 것
#             dfs(a_score,l_score,idx+1,temp)
#             # 어피치 것 뻇기
#             if sum(temp) + info[idx] +1 <= n and info[idx] != 0:
#                 a_score -= 10- idx
#                 l_score += 10 - idx
#                 temp[idx] = info[idx] + 1
#                 dfs(a_score,l_score,idx+1,temp)
#             elif info[idx] == 0:    #어피치가 안 쏜것
#                 l_score += 10 - idx
#                 temp[idx] = 1
#                 dfs(a_score,l_score,idx+1,temp)
    
#     dfs(a_score,l_score,0,answer)
#     if answer == [0,0,0,0,0,0,0,0,0,0,0] or max_==0:   return [-1]
#     else: 
#         if sum(answer) < n:   answer[-1] = n - sum(answer)
#         return answer

# # 케이스 8, 18 틀리는 경우 ㄱ 아래 조건 미포함
# #"라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요."

# # 위 조건을 넣었더니 케이스 23 오류 
# # max == 0이면 [-1] 반환