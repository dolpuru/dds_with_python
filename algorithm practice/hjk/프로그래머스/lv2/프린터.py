from collections import deque
def solution(priorities, location):

    q = deque(priorities)
    answer = 0
    while q:
        sample = q.popleft()
        location -= 1
        if q:
            if sample < max(q):
                q.append(sample)
                answer -= 1
                if location == -1:
                    location = len(q) - 1
            else:
                if location == -1:
                    answer += 1
                    break
        answer += 1
    return answer