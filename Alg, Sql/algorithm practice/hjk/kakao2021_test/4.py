import heapq
def solution(n, info):
    new_info = info[:]
    answer = [0 for _ in range(len(info))]
    for i in range(len(new_info)):
        new_info[i] += 1
    
    print(new_info)
    # 어피치 점수
    ap_score = 0
    for i in range(len(info)):
        if info[i] > 0:
            ap_score += 10 - i
    
    # print(ap_score)
    # print("info    ", info)
    # print("new_info", new_info)
    # 각 점수별로 효율성을 구해보자
    ef_list = []
    for i in range(len(info)):
        if info[i] >= 1: # 어피치의 점수도 까인다.
            ef_list.append( [ ((10-i) + (10-i)) / new_info[i], new_info[i], i ])
        else:
            ef_list.append( [ (10-i) / new_info[i], new_info[i], i ])

    print(ef_list)
    # 효율성이 높은거 순대로, n을 뺼 수 있다면 뺀다.
    max_heap = []
    for i in ef_list:
        heapq.heappush(max_heap, (-i[0], i[0], i[1], i[2])) # -효율값, 효율값, 화살 갯수, index
    
    ri_score = 0
    temp_max_heap = max_heap
    for i in range(len(info)):
        max_value_list = heapq.heappop(max_heap)
        print("list :", max_value_list)
        
        print("n :", n)
        if n - max_value_list[2] >= 0:
            answer[max_value_list[3]] = max_value_list[2]
            
            n -= max_value_list[2] # 화살 갯수 빼기
            
            if info[max_value_list[3]] >= 1:
                ap_score -= 10 - max_value_list[3]
            ri_score += 10 - max_value_list[3]
            

            
    # 남은 발 수 처리해줘야함 .. # 효율성을 따지기 떄문에 젤 끝에 추가해주는게 아닐 수 가 있다.
    if n > 0 :
        for i in range(len(answer)-1, -1, -1):
            if answer[i] > 0:
                continue
            else:
                answer[i] = n
                break
        
    if  ap_score >= ri_score:
        return [-1]
    
    return answer