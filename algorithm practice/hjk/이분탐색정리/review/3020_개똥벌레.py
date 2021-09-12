import sys
input = sys.stdin.readline
n, m = map(int, input().split())
list_ = []

answer_list = []
list_top = []
list_down = []
for i in range(n):
    if i%2 == 0:
        list_down.append(int(input()))
    else:
        list_top.append(int(input()))

list_down.sort()
list_top.sort()

minn = 9999999999999

answer_check = 1

answer = []

for i in range(1, m+1):
    find_mid = i

    cnt_1 = 0
    cnt_2 = 0

    left_down = 0
    right_down = n//2 -1
    while left_down <= right_down: # 여기서 이분탐색이 ㅆ ㅡ여야함
        
        mid_index = (left_down + right_down) // 2

        if list_down[mid_index] > find_mid - 0.5:
            right_down = mid_index -1 
            
        elif list_down[mid_index] < find_mid - 0.5:
            left_down = mid_index + 1
    
    cnt1 =  n//2 - left_down

    left_top = 0
    right_top = n//2 -1
    while left_top <= right_top:    
        mid = (left_top + right_top) // 2
    
        if list_top[mid] > m - (i - 0.5):
            right_top = mid - 1

        elif list_top[mid] < m - (i - 0.5):
            left_top = mid + 1

    cnt2 = n//2 - left_top


    if cnt1 + cnt2 <= minn:
        answer_list.append(cnt1 + cnt2)
        minn = cnt1 + cnt2


temp = min(answer_list)
cnt = 0
for i in answer_list:
    if temp == i:
        cnt += 1

print(temp, cnt)