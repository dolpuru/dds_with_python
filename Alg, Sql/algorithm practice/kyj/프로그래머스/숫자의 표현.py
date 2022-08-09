def solution(n):
    answer,sum_,p2 = 0,0,0
    for p1 in range(1,n//2+1):
        while sum_<n and p2 <n//2+1:
            p2 +=1
            sum_ += p2
        if sum_ == n: answer += 1
        sum_-=p1
    return answer +1 if n>2 else 1

print(solution(15))

def solution(n):
    answer,p1,p2,sum_ = 0,0,0,0
    maxp2 = n//2 + 1
    while p1<=p2 and p2<n:
        if sum_ == n:   
            answer +=1
            if p2 <= maxp2: 
                p2+=1
                sum_ += p2
            p1+=1
            sum_ -= p1
        elif sum_ < n:
            if p2 <= maxp2: 
                p2+=1
                sum_ += p2
            else:
                p1+=1
                sum_ -= p1
        else:
            p1+=1
            sum_ -= p1
    return answer+1

def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum_ = 0
        for j in range(i,n+1):
            if sum_ == n :
                answer += 1
                break
            elif sum_ > n:
                break
            else : 
                sum_ += j             
    return answer + 1