from collections import deque
# bfs
# 인접리스트
a,b,c = map(int, input().split())
list_ = [[] for _ in range(a+1)]
for i in range(b):
    num1, num2 = map(int,input().split())
    list_[num1].append(num2)
    list_[num2].append(num1)
    list_[num1].sort()
    list_[num2].sort()

# list_ => [[], [2,3,4], [1,4], [1,4], [1,2,3]]
vis_bfs = [0 for _ in range(a + 1)]

def bfs(c):
    temp = deque()
    temp.append(c)
    answer = []

    while temp:
        q = temp.popleft()
        
        if vis_bfs[q] == 0:
            answer.append(q)
            vis_bfs[q] = 1
            for com in list_[q]:
                    temp.append(com)
            
    return answer


vis_dfs = [0 for _ in range(a+1)]
def dfs(c): # 끝까지 젤 작은 정점만 본 뒤 더이상 볼 게 없으면 pop , 이 방법이면 반복문으로 젤 작은 요소들 처리 가능
    temp = []
    answer = []
    temp.append(c)
    answer.append(c)
    vis_dfs[c] = 1
    while temp:
        flag = 0
        p = temp[-1]

        for i in list_[p]:
            if vis_dfs[i] == 0:
                vis_dfs[i] = 1
                temp.append(i)
                answer.append(i)
                flag = 1
                break
        if flag == 0:
            temp.pop()
    return answer

  
# def dfs(c):   # 이 방식을 하면 전부 다 탐색하지 못 함 

#     temp = []
#     answer = []
#     temp.append(c)
#     answer.append(c)
#     vis_dfs[c] = 1
#     while temp:
#         p = temp.pop() # 이 부분에서 pop 을 시켜버리기 떄문 

#         for i in list_[p]:
#             if vis_dfs[i] == 0:
#                 vis_dfs[i] = 1
#                 temp.append(i)
#                 answer.append(i)
#                 break

#     return answer

# dfs 함수
#   1 def dfs(graph, start_node):
#   2     visit = list()
#   3     stack = list()
#   4
#   5     stack.append(start_node)
#   6
#   7     while stack:
#   8         node = stack.pop()
#   9         if node not in visit:
#  10             visit.append(node)
#  11             stack.extend(graph[node])
#  12
#  13     return visit
# (기존 데이터가 오름차순,  방문할 수 있는 정점이 여러 개인 경우에) 이렇게 짜면 큰 데이터를 기준으로 dfs탐색을 하는 것 같은데
# 이를 재귀함수를 쓰지않고   방문할 수 있는 정점이 여러 개인 경우에 정점 번호가 작은 것을 먼저 방문할 수 있는 방법이 없나? 

answer_dfs = dfs(c)
for i in answer_dfs:
    print(i, end= " ")
    
answer_bfs = bfs(c)
print()
for i in answer_bfs:
    print(i, end=" ")