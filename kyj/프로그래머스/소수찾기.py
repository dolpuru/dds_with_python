n = 10
li = [False] * (n+1)
li[0] = True
li[1] = True
for i in range(2,n//2+1):
    if li[i] == False:
        for j in range(i+i,n+1,i):
            li[j] = True
prime = [i for i in range(n+1) if li[i] == False]
print(prime)