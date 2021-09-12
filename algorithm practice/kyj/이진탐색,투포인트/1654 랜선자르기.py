''''
import sys
input = sys.stdin.readline
'''

K , N = map(int, input().split())
lan = list(int(input()) for i in range(K))

def get_the_n(mi,lan):
    num = 0
    for i in lan:
        if i >= mi:
            num += i//mi
    return num

fst = 1
end = max(lan)

while fst <= end : 
    mi = (fst + end)//2
    the_n = get_the_n(mi,lan)

    if the_n >= N:
        fst = mi +1

    else :
        end = mi -1


print(end)
