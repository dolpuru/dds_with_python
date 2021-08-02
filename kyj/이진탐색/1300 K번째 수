N = int(input())
k = int(input())

fst = 1
end = k

while fst <= end :
    mid = (fst + end) // 2
    temp = 0
    for i in range(1,N+1):
        if mid //i > N:
            temp += N
        else:
            temp += mid //i

    if temp >= k:
        end = mid - 1
    else : 
        fst = mid + 1

print(end+1)
