left = 13
right = 17
answer = 0
for i in range(left,right+1):
    if i**0.5 == int(i**0.5) :
        answer -= i
    else:
        answer += i
print(answer)
