#이분탐색 응용문제
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
list_ = list(map(int,input().split()))

def tree_sum(slice):
    return_sum = 0

    for i in list_:
        if i >= slice:
            return_sum += i - slice
    
    return return_sum

left = 0
right = max(list_)
result = 0
while left <= right:
    mid = (left + right) // 2

    temp = tree_sum(mid)
    '''합격 ?'''
    if  temp >= m:
        if result < mid:
            result = mid
        left = mid+1
    
    else:
        right = mid-1      

                         
print(result)