import sys
input = sys.stdin.readline
n = int(input())
list_ = list(map(int,input().split()))
list_.sort()

left = 0
right = n - 1
pair = []
min_val = 2000000000000

while left < right:
    tmp = list_[left] + list_[right]

    if abs(tmp) < min_val:
        pair = [list_[left], list_[right]]
        min_val = abs(tmp)
    
    if tmp >= 0:
        right -= 1
    else:
        left += 1
        
print(pair[0], pair[1])