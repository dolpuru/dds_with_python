import sys
input = sys.stdin.readline
m, people = map(int, input().split())
list_port = []
for i in range(m):
    list_port.append(int(input()))

start = 1
end = max(list_port) * people

while start <= end:
    mid = (start + end) // 2

    temp_people = 0
    for port_time in list_port:
        temp_people += mid // port_time

    if temp_people < people:
        start = mid + 1
        
    elif temp_people >= people:
        end = mid -1
        answer = mid

print(answer)