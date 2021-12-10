#투포인터 합
N, S = map(int, input().split())
A = list(map(int, input().split()))


sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]  
    

answer = 1000001
start = 0
end = 1

#알고리즘 실행
while start != N:
    if sum_A[end] - sum_A[start] >= S:
        answer = end - start
        start += 1
        
    else:
        if end != N:
            end += 1
        else:
            start += 1

if answer != 1000001:
    print(answer)
else:
    print(0)
