def solution(n):
    answer = [0,1]
    for i in range(2,n+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-1] % 1234567

# def solution(n):
#     li = [0,1]

#     for i in range(n-1):
#         answer = li[0] + li[1]
#         if i%2 == 0 : li[0] = answer
#         else : li[1] = answer
#     return answer % 1234567