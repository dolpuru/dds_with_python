def solution(s):
    
    list_ = ["A"]           # 쉽게 비교하기 위해 될 수 없는 값을 넣어 놨다.
    
    for i in s:             # s를 돌면서
        if i == list_[-1]:  # 젤 끝이랑 같으면 pop
            list_.pop()
        else:               # 아니면 append
            list_.append(i)
    
    return (1 if len(list_) == 1 else 0) 