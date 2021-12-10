K, N = map(int,input().split())
lst = []
for i in range(K):
    lst.append(int(input()))
start = 1
end = max(lst)

while True:

    mid = (start+end)//2
    sum = 0
    for i in lst:
        sum += i // mid
    print(mid, sum)
    if sum < N:  #2541  11
        end = mid - 1
    else:
        end = mid
        break
print(mid)