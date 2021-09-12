'''
실패
'''
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# list_ = list(map(int, input().split()))


# def two_pointer (lp, rp, n, m):
#     answer = sys.maxsize
#     temp = 0
#     while rp < n:

#         if temp >= m:
#             answer = min(answer, rp - lp)
#             temp -= list_[lp]
#             lp += 1
            
#         elif temp < m:
#             temp += list_[rp]
#             rp += 1
            
#     return answer


# answer = two_pointer(0,0, n, m)
# if answer == sys.maxsize:
#     print(0)
# else:
#     print(answer)
# 차이는 while의 조건인데 ..
# 반례 사이트 https://bingorithm.tistory.com/13
'''
통과
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
list_ = list(map(int, input().split()))


def two_pointer (lp, rp, n, m):
    answer = sys.maxsize
    temp = 0
    while True:

        if temp >= m:
            answer = min(answer, rp - lp)
            temp -= list_[lp]
            lp += 1
        elif rp == n:
            break
        elif temp < m:
            temp += list_[rp]
            rp += 1
            
    return answer


answer = two_pointer(0,0, n, m)
if answer == sys.maxsize:
    print(0)
else:
    print(answer)