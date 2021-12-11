# 1654, 2805, 3020, 3079, 2470
k, n = map(int, input().split())
lan = []

for i in range(k):
    lan.append(int(input()))

fst = 1
end = max(lan)

while fst <= end : 
    mid = (fst + end) // 2 
    count = 0
    for i in lan:
        count += i//mid
    
    if count < n:
        end = mid - 1
    else :
        fst = mid + 1

print(fst -1 )