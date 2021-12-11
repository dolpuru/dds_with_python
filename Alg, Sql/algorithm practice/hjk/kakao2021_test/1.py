def solution(id_list, report, k):
    result = [0 for _ in range(len(id_list))]
    dic_cnt = {} # 신고 당한 횟수
    dic_temp = {} #  신고한 사람들
    dic_answer = {} # 정답
    for i in id_list:
        dic_cnt[i] = 0
        dic_temp[i] = []
        dic_answer[i] = 0
        
        
    report = list(set(report))
    
    for i in report:
        a,b = i.split()
        dic_cnt[b] += 1 #신고 당한 횟수 up
        dic_temp[b].append(a)
    
    
    # print(dic_cnt)
    # print(dic_temp)
    for i in range(len(id_list)):
        if dic_cnt[id_list[i]] >= k: # 아이디 정지
            for j in dic_temp[id_list[i]]:
                dic_answer[j] += 1
            
    # print(list(dic_answer.values()))
    return list(dic_answer.values())