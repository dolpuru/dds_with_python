import datetime

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#3시간 이하면 5000
#3시간 넘어서 10분 추가 당 600
answer = []
dic ={}

for i in records:
    time, car_n, bd = i.split(' ')
    
    if car_n in dic:
        temp = dic.get(car_n)
        temp.append(time)
    else:
        dic[car_n] = [time]
        

for k,li_ in dic.items():
    time = datetime.datetime.strptime('00:00',"%H:%M")
    while li_:
        if len(li_) %2 == 1 :
            time_1 = datetime.datetime.strptime('23:59',"%H:%M")
            time_2 = datetime.datetime.strptime(li_.pop(),"%H:%M") 
            time = time_1 - time_2
            
        else:
            time_1 = datetime.datetime.strptime(li_.pop(),"%H:%M")
            time_2 = datetime.datetime.strptime(li_.pop(),"%H:%M") 
            time_temp = time_1 - time_2 
            time = time + time_temp
    
    time= str(time)
    time = time[-8:]
    h,m,s =map(int, time.split(':'))
    base = h*60 + m
    if base <= fees[0]:
        dic[k] = fees[1]
    else:
        time =h*60 + m - fees[0]
        
        if time%fees[2] == 0:
            dic[k] = fees[1] + (time//fees[2])*fees[3]
        else:
            dic[k] = fees[1] + (time//fees[2]+1)*fees[3]

dic_sort = sorted(dic.items())
for i in range(len(dic)):
    a= list(dic_sort[i])
    answer.append(a[1])
print(answer)