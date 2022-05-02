N = int(input())
li = [0,1]
if N == 0:  print(0)
elif N == 1: print(1)
else:
    for i in range(2,N):
        if i%2 == 0:    li[0] = sum(li)
        else:           li[1] = sum(li)
    print(sum(li))