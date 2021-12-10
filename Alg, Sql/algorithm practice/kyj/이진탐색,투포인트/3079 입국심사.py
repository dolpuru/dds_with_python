'''
import sys
input = sys.stdin.readline
'''

N , M = map (int , input().split())
T = [int(input()) for i in range(N)]

fst = min(T)
end = max(T)*M

def temp_find(N,mid,T):
    temp = 0
    for i in range(N):
        temp += mid // T[i]
    return temp

while fst <= end :
    mid = (fst + end) //2 
    temp = temp_find(N,mid,T)

    if temp >= M:
        end = mid - 1
    else :
        fst = mid + 1

print(end + 1)
