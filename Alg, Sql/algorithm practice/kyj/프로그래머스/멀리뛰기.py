def solution(n):
    answer = 0
    arr = [0,1,2]
    for i in range(n):  arr.append(arr[-1]+ arr[-2])
    return arr[n] % 1234567

# 1 1
# 2 2
# 3 3
# 4 5
# 5 8
# 6 13