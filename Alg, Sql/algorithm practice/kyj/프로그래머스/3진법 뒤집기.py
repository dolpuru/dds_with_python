n = 125
answer = ''
result = 0

while n > 0:
    n,r = divmod(n,3)
    answer = answer + str(r)
answer = ''.join(reversed(answer))

temp = 0
for i in answer:
    result = result + (3**temp*int(i))
    temp+=1

print(result)
