def fact(n):
    answer = 1
    if n >0:    answer =  n * fact(n-1)
    return answer
    
N = int(input())
print(fact(N))
