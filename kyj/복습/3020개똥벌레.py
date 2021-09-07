n,h = map(int, input().split())
obs_odd = []
obs_even = []
result = []
for i in range(n):
    if i%2 == 0:
        obs_odd.append(int(input()))
    else:
        obs_even.append(int(input()))
obs_odd.sort()
obs_even.sort()

for i in range(1,h+1):
    fst = 0
    end = n//2 -1 
    odd = 0
    while fst <= end :
        mid = (fst + end) //2 
        if obs_odd[mid] < i :
            
            fst = mid + 1
        else :
            odd = n//2 - mid
            end = mid - 1
    

    fst = 0
    end = n//2 -1 
    even = 0
    while fst <= end :
        mid = (fst + end) //2 
        if h- obs_even[mid] >= i :
            
            fst = mid + 1
        else :
            even = n//2 - mid
            end = mid - 1
    

    result.append(odd+even)

print(min(result),' ', result.count(min(result)))