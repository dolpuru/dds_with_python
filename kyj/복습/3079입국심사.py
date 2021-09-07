n,m = map(int,input().split())
time = [int(input()) for i in range(n)]

fst = min(time)
end = max(time) * m

while fst <= end:
    mid = (fst + end) //2
    num = 0 

    for  i in time:
        num += mid//i
    
    if num < m : 
        fst = mid + 1
    else :
        end = mid - 1

print(end+1)