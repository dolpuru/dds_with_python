record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

answer = []
dic = {}

for i in record:
    if len(i.split()) == 3 :
        f, id_, name = i.split()
        dic[id_] = name    

for i in record:
    if len(i.split()) == 3 :
        f, id_, name = i.split()
    else :
        f, id_ = i.split()
    if f == "Enter":
        answer.append(str(dic.get(id_) + "님이 들어왔습니다."))
    elif f == "Leave":
        answer.append(str(dic.get(id_) + "님이 나갔습니다."))

print(answer)