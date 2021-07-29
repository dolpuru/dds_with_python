import sys
import collections
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split(' '))
array = collections.deque()
visited = [-1 for i in range(F+1)]
array.append(S)
visited[S] = 0
while len(array) >0:

    target = array.popleft()
    if target == G:
        print(visited[target])
        break

    if target + U <= F and visited[target+U] == -1:
        visited[target+U] = visited[target]+1
        array.append(target+U)
    if target - D >= 1 and visited[target-D] == -1:
        visited[target-D] = visited[target]+1
        array.append(target-D)
else:
    print("use the stairs")
