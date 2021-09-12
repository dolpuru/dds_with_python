from collections import deque

m = int(input())
n = int(input())
list_ = [[] for _ in range(0, m+1)]
check_list = [0 for _ in range(0, m+1)]


for i in range(n):
    a, b =map(int, input().split())
    list_[a].append(b)
    list_[b].append(a)

print(list_)







cnt = 0
st = deque()
st.append(1)

while st:
    pop_index = st.popleft()
    if check_list[pop_index] == 0:
        check_list[pop_index] = 1
        cnt += 1
        for j in list_[pop_index]:
            st.append(j)

print(cnt-1) # 1번 제외
 