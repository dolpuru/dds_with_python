id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
report_set = list(set(report))


dic= {}    #메일 보낼 수 
mail= {}
for i in id_list:
    dic[i] = 0

pt = {}
for i in report_set:    #불량 이용자 찾기
    reported,name = i.split(' ')
    if reported in dic:
        temp = dic.get(reported)
        temp.append(name)
    else:
        dic[reported] = name


print(dic.items())
