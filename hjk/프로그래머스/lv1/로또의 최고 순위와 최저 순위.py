def solution(lottos, win_nums):
    same = 0
    cnt = 0
    for i in lottos:
        if i == 0:
            cnt += 1
            continue
        for j in range(len(win_nums)):
            if i == win_nums[j]:
                same += 1
           

    answer = []
    top, bot = same + cnt, same
    if top == 6:
        answer.append(1)
    elif top == 5:
        answer.append(2)
    elif top == 4:
        answer.append(3)
    elif top == 3:
        answer.append(4)
    elif top == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    if bot == 6:
        answer.append(1)
    elif bot == 5:
        answer.append(2)
    elif bot == 4:
        answer.append(3)
    elif bot == 3:
        answer.append(4)
    elif bot == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    return answer

# 매우 깔끔한 코드 .. 
# def solution(lottos, win_nums):
    
#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)  # count로 0의 개수를 셈
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]
