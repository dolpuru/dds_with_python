n = 5
answer = '수박'
q,r = divmod(n,2)
answer = answer * 2
if r == 1:
    answer += '수'

print(answer)