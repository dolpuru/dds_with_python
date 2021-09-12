n = int(input())

def prime_find(n):
    int_n = int(n**0.5)
    li=[True] * (n+1)
    for i in range(2,int_n+1):
        if li[i] == True:
            for j in range(i+i,n+1,i):
                    li[j] = False
    li[1] = False
    prime = [ i for i in range(n + 1) if li[i] == True]
    return prime

def partial_s():
    global n
    p1 , p2, = 0,0
    ps = [0] * (len(prime))
    for  i in range(len(prime)):
        ps[i] = ps[i- 1]+ prime[i]
    count = 0

    while p1 < len(prime):
        if ps[p2] - ps[p1] == n:
            count += 1
            p1 += 1
        elif ps[p2] - ps[p1] > n:
            p1 += 1
        else:
            if p2 < len(prime) - 1:
                p2 += 1
            else:
                p1 += 1
    return count

prime = prime_find(n)

print(partial_s())
