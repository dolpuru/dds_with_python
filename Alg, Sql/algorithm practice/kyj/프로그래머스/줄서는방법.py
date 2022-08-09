import math
def solution(n, k):
    answer = []
    li = [ i+1 for i in range(n)]
    
    def line(k,li):
        nonlocal answer
        if len(li) == 1 :   
            answer.append(li[0])
        else:
            idx,nk = divmod(k,math.factorial(len(li)-1))
            answer.append(li.pop(idx))
            line(nk,li)            
    
    line(k-1,li)
    return answer
# import math
# def solution(n, k):
#     answer = []
#     li = [i+1 for i in range(n)]

#     def line(k,li):
#         nonlocal answer
#         if k == 0 or len(li) ==0 :    
#             answer = answer + li
#             return
#         else:
#             s,r = divmod(k-1,math.factorial(len(li)-1))
#             answer.append(li.pop(s))
#             line(r+1,li)

#     line(k,li)
#     return answer

print(solution(3,5))

# 1,2,3,4
# (1, 2, 4, 3)
# (1, 3, 2, 4)
# (1, 3, 4, 2)
# (1, 4, 2, 3) 
# (1, 4, 3, 2)

# (2, 1, 3, 4)
# (2, 1, 4, 3)
# (2, 3, 1, 4)
# (2, 3, 4, 1) !
# (2, 4, 1, 3)
# (2, 4, 3, 1)

# (3, 1, 2, 4)
# (3, 1, 4, 2)
# (3, 2, 1, 4)
# (3, 2, 4, 1)
# (3, 4, 1, 2)
# (3, 4, 2, 1)

# (4, 1, 2, 3)
# (4, 1, 3, 2)
# (4, 2, 1, 3)
# (4, 2, 3, 1)
# (4, 3, 1, 2)
# (4, 3, 2, 1)