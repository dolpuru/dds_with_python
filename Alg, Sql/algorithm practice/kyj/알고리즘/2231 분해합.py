N = int(input())
answer = 0

for i in range(N):
    dec = i
    temp = str(i)
    for s in temp:
        dec += int(s)
    if dec == N: 
        answer = i
        break

print(answer)
