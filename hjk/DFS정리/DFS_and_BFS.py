from collections import deque
# bfs
# 인접리스트
a,b,c = map(int, input().split())
list_ = [[] for _ in range(a+1)]
for i in range(b):
    num1, num2 = map(int,input().split())

    list_[num1].append(num2)
    list_[num2].append(num1)

# list_ => [[], [2,3,4], [1,4], [1,4], [1,2,3]]
vis_bfs = [0 for _ in range(a + 1)]

def bfs(c):
    temp = deque()
    temp.append(c)
    answer = []

    while temp:
        q = temp.popleft()
        if vis_bfs[q] == 0:
            vis_bfs[q] = 1
            answer.append(q)
            for com in list_[q]:
                temp.append(com)
            
    return answer


vis_dfs = [0 for _ in range(a+1)]
def dfs(c):
    temp = []
    temp.append(c)
    answer = []
    for i in list_[c]:
        if not vis_dfs[i]:
            dfs(i)

    return answer

answer_dfs = dfs(c)
for i in answer_dfs:
    print(i, end= " ")
answer_bfs = bfs(c)
print()
for i in answer_bfs:
    print(i, end=" ")