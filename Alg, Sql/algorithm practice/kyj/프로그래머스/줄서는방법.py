import math
def solution(n, k):
    answer = []
    def line(li,n,k):
        nonlocal answer
        if n == 1: 
            answer.append(li[0])
            return 
        else:
            q,r = divmod(k-1,math.factorial(n-1))
            print(q,r)
            answer.append(li[q])
            li.pop(q)
            print(li,n-1,r,answer)
            line(li,n-1,r)
        
        print(answer)
    li = [ i for i in range(1,n+1)]
    print(line(li,n,k))

    return answer

print(solution(3,4))

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