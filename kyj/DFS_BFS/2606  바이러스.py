def dfs(li,v,visited):
    visited[v] = True
    global count 
    for i in li[v]:
        if not visited[i]:
            dfs(li,i,visited)
            count += 1
    return count

c = int(input())
n = int(input())

li = [[] for i in range(c+1)]

for i in range(1, n+1):
    num_1,num_2 = map(int, input().split())
    li[num_1].append(num_2)
    li[num_2].append(num_1)

count = 0
visited = [False] * (c + 1)
print(dfs(li,1,visited))