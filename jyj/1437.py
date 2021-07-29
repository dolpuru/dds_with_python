import sys

input = sys.stdin.readline

def func(N):
    if N <=4:
        print(N)
        return N
    ans = 0
    if N%3 == 0:
        ans = pow(3, N//3)
    elif N%3 == 1:
        ans = pow(3, (N//3)-1)*4
    elif N%3 == 2:
        ans = pow(3, N//3)*2
    
    print(ans%10007)
 

if __name__ == '__main__':
    N = int(input())
    func(N)

