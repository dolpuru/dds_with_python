import math

def is_sosu(num, num_area):
    global sosu
    result = True

    for j in range(1, num_area):
        if not num // 10**(num_area-j) in sosu[j]:
            result = False
            break

    if not result:
        return result 

    for i in range(2, int(math.sqrt(num))+1):
        if num % i ==0:
            result=False
            break
    return result

N = int(input())
sosu = [[] for i in range(N+1)]

for num_area in range(1, N+1):
    if num_area == 1:
        for i in range(2, 10):
            if is_sosu(i, num_area):
                sosu[num_area].append(i)
    else:
        for i in sosu[num_area-1]:
            for j in range(10):
                if is_sosu(i*10+j, num_area):
                    sosu[num_area].append(i*10+j)


for i in sosu[-1]:
    print(i)
