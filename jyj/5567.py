import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
m_list = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    m_list[a].append(b)
    m_list[b].append(a)


friend = set()

for i in m_list[1]:
    friend.add(i)
    for j in m_list[i]:
        friend.add(j)

print(len(friend)-1)
