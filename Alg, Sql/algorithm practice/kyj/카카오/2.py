def conversion(n, k):
    s = "0123456789ABCDEF"
    q, r = divmod(n, k)
    if q == 0:
        return s[r]
    else:
        return conversion(q, k) + s[r]


def prime_n(x):
    for i in range(2, int( x **0.5) + 1):
        if x % i == 0:
            return False 
    return True
 

n = 110011
k = 10

a = conversion(n,k)
answer = 0

num = list(a.split('0'))

while '1' in num:
    num.remove('1')

while '' in num:
    num.remove('')


for i in num:
    i = int(i)
    if prime_n(i) == True:
        answer += 1
print(answer)