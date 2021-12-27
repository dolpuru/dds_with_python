import math

def is_sosu(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i ==0:
            return False
    return True

N = int(input())
sosu = [[] for i in range(N+1)]
sosu[1] = [2, 3, 5, 7]

for num_area in range(2, N+1):
    for i in sosu[num_area-1]:
        for j in range(1, 10, 2):
            if is_sosu(i*10+j):
                sosu[num_area].append(i*10+j)

for i in sosu[-1]:
    print(i)
