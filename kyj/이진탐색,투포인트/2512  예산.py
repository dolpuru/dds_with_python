N = int(input())
region = list(map(int , input().split()))
money = int(input())

fst = 0
end = max(region)

def find_region(mid , region):
    sum = 0
    for i in region:
        if mid >=  i: 
            sum += i
        else:
            sum += mid
    return sum

while fst <= end:
    mid = (fst + end) //2
    sum = find_region(mid, region)
    if sum > money:
        end = mid - 1
    else:
        fst = mid + 1
    
print(end)
