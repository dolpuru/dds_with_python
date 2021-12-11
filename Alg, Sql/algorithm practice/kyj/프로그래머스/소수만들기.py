nums = [1,2,7,6,4]
answer = 0
li = [True] *3000
li[0] = False
li[1] = False
result = []
#소수 리스트 만들기
int_=int(3000**0.5)
for i in range(2, int_):
    if li[i] == True:
        for j in range(i + i,3000,i):
            li[j] = False
prime = [i for i in range(3000) if li[i] == True]


for i in nums:
    for j in nums:
        if i<j:
            for k in nums:
                if j<k:
                    if i+j+k in prime:
                        answer += 1

print(answer)