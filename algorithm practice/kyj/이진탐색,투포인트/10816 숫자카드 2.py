'''
import sys
input = sys.stdin.readline
'''

N = int(input())
N_card = list(map(int , input().split()))
M = int(input())
M_list = list(map(int , input().split()))


dic = {}

for i in N_card:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in M_list:
    if i in dic:
        print(dic[i])
    else:
        print('0')
