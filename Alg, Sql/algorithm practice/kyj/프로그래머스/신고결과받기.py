def solution(id_list, report, k):
    report_dic = {}
    id_dic = {}
    report = list(set(report))
    
    
    for i in id_list:   
        report_dic[i] = []
        id_dic[i] = 0
    
    for re in report:
        temp = re.split()
        report_dic[temp[1]].append(temp[0])
        
    for key, values in report_dic.items():
        if len(values) >= k: 
            for i in values:    id_dic[i] +=1
            
    return list(id_dic.values())