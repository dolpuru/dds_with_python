N , C = map(int, input().split())
x = [int(input()) for i in range(N)]

x.sort()

fst = 1
end = x[-1] - x[0]


while fst <= end:
    mid = (fst + end) //2
    flag = 0
    cnt = 1
    
    for i in range(N):
        if x[i] - x[flag] < mid:
            continue
        else :
            flag = i
            cnt += 1

    if cnt >= C : #최대여야하니까 cnt와 C가 같아도 최대 mid를 구하기위해 부등호 >=
        fst = mid + 1
    else :
        end = mid - 1
print(end)
