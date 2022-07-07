def solution(n):
    answer = [1,2]
    if n == 1 or n == 2:  return answer[i-1]
    for i in range(2,n):
            answer.append((answer[-1]+answer[-2])% 1000000007)
    return answer[-1] % 1000000007


print(solution(4))