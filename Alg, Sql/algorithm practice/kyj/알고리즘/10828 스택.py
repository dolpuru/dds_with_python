import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    input_ = sys.stdin.readline().split()
    s = input_[0]
    if s == "push":  
        stack.append(input_[1])
    elif s == "pop":  
        if len(stack) > 0:    print(stack.pop())
        else:   print(-1)
    elif s == "size":   print(len(stack))
    elif s == "empty": 
        if len(stack) == 0: print(1)
        else:   print(0)
    elif s == "top":
        if len(stack) == 0: print(-1)
        else:   print(stack[-1])
