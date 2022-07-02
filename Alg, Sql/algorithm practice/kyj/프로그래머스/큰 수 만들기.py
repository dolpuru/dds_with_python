def solution(number, k):
    answer = []
    count = 0
    for n in number:
        while len(answer) > 0 and int(answer[-1]) < int(n) and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)
    return int(''.join(answer)) if k==0 else int(''.join(answer[:len(answer)-k]))

print(solution("1231234",3))