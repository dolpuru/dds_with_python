m = int(input())
n = int(input())
list_ = [x for x in range(1, m+1)]
check_list = [x for x in range(1, m+1)]
for i in range(n):
    a, b =map(int, input().split())
    list_[a].appned(b)

def dfs():

cnt = 2
cnt = 0
for i in range(1,m+1):
    if check_list[i] != 0:
        cnt += 1

print(cnt)
