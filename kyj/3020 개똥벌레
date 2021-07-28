import sys
input = sys.stdin.readline

N, H  = map(int, input().split())
top = []
bottom = []
for i in range(N):
    if i%2==0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
bottom.sort()
hurdle = []
def answer(N,H,top,bottom,hurdle):
    for s in range(1,H+1):
        fst = 0
        end = N//2 - 1
        bottom_hurdle = 0
        while fst <= end :
            mid = (fst + end) //2
            if bottom[mid] >= s:
                bottom_hurdle = N//2 - mid
                end = mid - 1
            else :
                fst = mid + 1
        fst = 0
        end = N//2 - 1
        top_hurdle = 0
        while fst <= end :
            mid = (fst + end) //2
            if H - top[mid] < s:
                top_hurdle = N//2 - mid
                end = mid - 1
            else :
                fst = mid + 1

        hurdle.append(top_hurdle + bottom_hurdle)

    result = min(hurdle)
    print(result, hurdle.count(result))

answer(N,H,top,bottom,hurdle)
