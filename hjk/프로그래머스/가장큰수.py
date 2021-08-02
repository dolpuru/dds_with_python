def solution(numbers):

    list_ = sorted(list(map(str, numbers)), reverse = True, key=lambda x : x*4 )
    answer = ''.join(list_)
    return str(int(answer))
