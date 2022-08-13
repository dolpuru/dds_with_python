##옛날
# def solution(begin, end):
#     answer = []
#     for i in range(begin,end+1):
#         if i ==1: answer.append(0)
#         else:
#             for j in range(2,int(end**0.5)+1):
#                 if i/j > 10 ** 7:
#                     continue
#                 if i%j ==0: 
#                     answer.append(i/j)
#                     break
#             else:
#                 answer.append(1)
#     return answer


def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        if i==1:    answer.append(0)
        else:
            for d in range(2,i//2+1):
                if i/d > 10 ** 7:   continue
                if i%d==0:   
                    answer.append(i/d)
                    break
            else: answer.append(1)
    return answer
print(solution(1,10))