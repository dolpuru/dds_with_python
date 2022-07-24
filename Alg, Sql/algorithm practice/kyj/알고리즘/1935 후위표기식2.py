n = int(input())
exp = list(input())

number = []
stack = []

for i in range(n):
    number.append(input())

for s in exp:
    if s.isalpha():
        stack.append(number[ord(s)-65])
    else:
        b = stack.pop()
        a = stack.pop()
        temp = a + s + b
        stack.append(str(eval(temp)))

print(format(float(stack[0]),".2f"))