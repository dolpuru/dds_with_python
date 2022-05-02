import datetime
m = "A#"
musicinfos = ["12:00,12:01,HELLO,A#"]

answer = {}
for i in musicinfos:
    count = 0
    temp = i.split(',')
    time = datetime.datetime.strptime(temp[1],"%H:%M") - datetime.datetime.strptime(temp[0],"%H:%M")
    h,t,s = str(time).split(":")
    t = int(h)*60 + int(t)
    
    for i in temp[3]:
        if i == "#": continue
        else:   count += 1
    

    if t <= count:
        temp_ = ''
        i = 0
        while i < t: 
            temp_ += temp[3][i])
            try:   
                if temp[3][i+1] == "#":   t += 1
            except: break
            i += 1
        temp[3] = temp_
    else:
        s,d = divmod(t,count)
        temp_ = temp[3] * s

        i = 0
        while i < d:  
            temp_ += temp[3][i]
            try:   
                if temp[3][i+1] == "#":   d += 1
            except: break
            i += 1
        temp[3] = temp_
    print(temp[3])
        
    if m in temp[3]:
        if m+"#" not in temp[3]: answer[temp[2]] = t
        
    
print(answer)

if answer:
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    print(answer[0][0])
else:    print("no")