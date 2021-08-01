def solution(numbers):
    list_ = sorted(list(map(str, numbers)), reverse = True )
    answer = ''.join(list_)
    return str(int(answer))_
