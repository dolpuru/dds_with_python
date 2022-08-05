#현재
def solution(n):
    answer = []
    def hanoi(n,st,sp,end):
        nonlocal answer
        if n == 1:  answer.append([st,end])
        else:
            hanoi(n-1,st,end,sp)
            answer.append([st,end])
            hanoi(n-1,sp,st,end)
    hanoi(n,1,2,3)
    return answer

# 옛날 코드
#  answer = []
# def hanoi(n,st,sp,end):
#     global answer
#     if n == 1:
#         answer.append([st,end])
#         return
#     else:
#         hanoi(n-1,st,end,sp)
#         answer.append([st,end])
#         hanoi(n-1,sp,st,end)

# def solution(n):
#     hanoi(n,1,2,3)
#     return answer