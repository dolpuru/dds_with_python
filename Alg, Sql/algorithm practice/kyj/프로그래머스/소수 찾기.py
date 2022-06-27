from itertools import permutations
numbers = "011"

answer = []
number = [i for i in numbers]
number = list(reversed(sorted(number)))
print(number)

n = int(''.join(number))
pri = [True for i in range(n+1)]
pri[0] = False
pri[1] = False
for i in range(2,(n+1)//2):
    for j in range(2*i,n+1,i):
        if j%i == 0:
            pri[j] = False

for i in range(1,len(number)+1):
    for c in permutations(number,i):
        per = int(''.join(c))
        if pri[per]:    answer.append(per)

print( len(set(answer)))
