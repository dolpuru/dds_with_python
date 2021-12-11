import sys

input = sys.stdin.readline

def func(n_array, s_array):
    dp = [0]
    for i in n_array:
        tmp = []
        for d in dp:
            if not i+d in dp:
                tmp.append(i+d)
            if not i-d in dp:
                tmp.append(d-i)
        dp.extend(tmp)

    for i in s_array:
        if i in dp:
            print('Y', end=' ')
        else:
            print('N', end=' ')

if __name__ == '__main__':
    n = int(input())
    n_array = list(map(int, input().split(' ')))
    s = int(input())
    s_array = list(map(int, input().split(' ')))
    func(n_array, s_array)

