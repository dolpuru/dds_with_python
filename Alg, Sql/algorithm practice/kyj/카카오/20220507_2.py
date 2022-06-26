def solution(queue1, queue2):
    q1 = queue1
    q2 = queue2
    answer = -1
    goal = (sum(q1)+sum(q2))/2
    if int(goal) != goal:   return -1
    li = queue1 + queue2

    p1,p2 = 0,1
    while p1 <p2 and p2<len(li):
        if sum(li[p1:p2]) < goal:  p2 += 1
        elif sum(li[p1:p2]) == goal:    break 
        else:   p1+=1

    
    if sum(li[:p1]) + sum(li[p2:]) == goal : 
        p2 -= len(q1)
        # print(li,p1,p2)
        if p2 < 0:   return -1
        else: return p1+p2
    else:  return -1
# 주어진 q1 q2이가 졸라 길어지면 시간초과뜸