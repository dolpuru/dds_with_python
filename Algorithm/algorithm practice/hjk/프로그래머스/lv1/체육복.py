from collections import deque
def solution(n, lost, reserve):
    lost.sort()                 # 정렬
    reserve.sort()              # 정렬
    temp = lost[:]

    # 제외해주기 겹치는거  아래 주석은 다른사람 코드
    #     _reserve = [r for r in reserve if r not in lost]
    #     _lost = [l for l in lost if l not in reserve]
    #
    for i in range(len(temp)):
        if temp[i] in reserve:
            index = reserve.index(temp[i])
            reserve.pop(index)
            index = lost.index(temp[i])
            lost.pop(index)
            
    lost_q = deque(lost)

    while lost_q:
        q = lost_q.popleft()
        if int(q) in reserve:
            index = reserve.index(int(q))
            reserve.pop(index)
            continue
        if int(q) - 1 in reserve:
            index = reserve.index(int(q) - 1)
            reserve.pop(index)
            continue
        elif int(q) + 1 in reserve:
            index = reserve.index(int(q) + 1)
            reserve.pop(index)

            continue
        else:
            n -= 1

    return n