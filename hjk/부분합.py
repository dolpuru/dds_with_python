import sys
input = sys.stdin.readline
n, m = map(int, input().split())
list_ = list(map(int, input().split()))


def two_pointer (lp, rp, n, m):
    answer = 100001
    while rp < n:
        temp = sum(list_[lp : rp+1]) # 이부분에서 시간초과

        if temp > m:
            lp += 1
        elif temp <= m:
            answer = min(answer, rp + 1 - lp)
            rp += 1
    return answer
print(two_pointer(0,0, n, m))