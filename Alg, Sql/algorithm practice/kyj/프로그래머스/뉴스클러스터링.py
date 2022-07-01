def solution(str1, str2):
    answer,inter,union = 0,0,0
    dic1,dic2 = {}, {}
    str1,str2 = str1.lower(), str2.lower()
    
    for i in range(len(str1)-1):
        temp = str1[i] +str1[i+1]
        if not temp.isalpha():    continue
        if temp in dic1:     dic1[temp] += 1
        else:   dic1[temp] = 1

    for i in range(len(str2)-1):
        temp = str2[i] +str2[i+1]
        if not temp.isalpha():    continue
        if temp in dic2:     dic2[temp] += 1
        else:   dic2[temp] = 1

    setInter = set(dic1) & set(dic2)
    for s in setInter:
        inter += min(dic1[s],dic2[s])
        union += max(dic1[s],dic2[s])

    setSD = set(dic1) ^ set(dic2)
    for s in setSD:
        if s in dic1:   union += dic1[s] 
        else:   union += dic2[s] 
    
    return int((inter / union) * 65536) if union != 0 else 65536


print(solution('handshake','shake hands'))
