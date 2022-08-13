def convert(n,k):
    q,r = divmod(n,k)
    return convert(q,k) + str(r) if q !=0 else str(r)

def ispri(n):
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:    return 0
    return 1 

def solution(n, k):
    answer = 0
    n = convert(n,k).split('0')
    for p in n:
        if p != '' and p != '1':    answer += ispri(int(p))
    return answer
    

# import math
# def c_convert(num,n):
#     t = '0123456789'
#     q,r = divmod(num,n)
#     return c_convert(q,n) + t[r] if q else t[r]

# def solution(n, k):
#     answer = c_convert(n,k)
#     answer = answer.strip('0').split('0')
#     i = 0
#     while i <len(answer):
#         if answer[i]== '' or answer[i] =='1':  
#             answer.remove(answer[i])
#             i -= 1
#         else:
#             answer[i] = int(answer[i])
#             for j in range(2,int(math.sqrt(answer[i]))+1):
#                 if answer[i] % j == 0: 
#                     answer.remove(answer[i])
#                     i -= 1
#                     break
#         i += 1
#     return len(answer)

# math.ceil(i**0.5)

# import math
# def c_convert(num,n):
#     t = '0123456789'
#     q,r = divmod(num,n)
#     return c_convert(q,n) + t[r] if q else t[r]

# def solution(n, k):
#     answer = c_convert(n,k)
#     answer = answer.strip('0').split('0')
#     for i in answer:
#         if i== '' or i =='1':  answer.remove(i)
#         else:
#             i = int(i)
#             for j in range(2,int(math.sqrt(i))+1):
#                 if i % j == 0: 
#                     answer.remove(str(i))
#                     break
#     return len(answer)
    

print(solution(797161,3))