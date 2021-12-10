import sys
input = sys.stdin.readline
N = int(input())

d_list = [0 for i in range(1001)]
subjects = []
for i in range(N):
    subjects.append(list(map(int, input().split(' '))))

subjects = sorted(subjects, key=lambda subject: subject[1], reverse=True)

for i in subjects:
    
    pointer = i[0]
    while pointer > 0:
        if d_list[pointer] == 0:
            d_list[pointer] = i[1]
            break
        pointer -=1

print(sum(d_list))
