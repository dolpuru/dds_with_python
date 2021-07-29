n = int(input())
list_prime = []

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

# n 보다 작은 소수들을 저장한다.
list_prime = prime_list(n+1)

if len(list_prime) == 0:
    print(0)
else:
    lp = 0
    rp = 0
    temp = 0
    cnt = 0
    while True: # 왜 True로 하고 밑에서 따로 조건을 줘야 할 까 ? 
        
        if temp > n :
            temp -= list_prime[lp]
            lp += 1
        elif temp == n:
            cnt += 1
            temp -= list_prime[lp]
            lp += 1
        elif rp == len(list_prime):
            break
        
        else:
            temp += list_prime[rp]
            rp += 1
    print(cnt)