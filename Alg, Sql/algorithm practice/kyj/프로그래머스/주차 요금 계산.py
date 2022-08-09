import math
from optparse import Values
def timeCal(a,b):
    a= list(map(int, a.split(':')))
    b= list(map(int, b.split(':')))
    
    h = a[0] - b[0]
    if a[1] < b[1]:
        h -= 1
        m = a[1] + 60 - b[1]
    else:   m = a[1] - b[1]
    return  h*60 + m
        
def fee(time,fees):
    if time <= fees[0]: return fees[1]
    else:
        time -= fees[0]
        return fees[1] + math.ceil(time/fees[2]) * fees[-1]

def solution(fees, records):
    answer = []
    recordsDic = {}
    
    for r in records:
        temp = r.split()
        if temp[1] in recordsDic:   recordsDic[temp[1]].append(temp[0])
        else:   recordsDic[temp[1]] = [temp[0]]
    
    recordsDic = sorted(recordsDic.items()) 
    for car,time in recordsDic:
        if len(time) % 2 == 1: time.append('23:59')
        tempTime = 0 
        while time:
            a = time.pop()
            b = time.pop()
            tempTime += timeCal(a,b)
        answer.append(fee(tempTime,fees))
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

# import datetime
# def solution(fees, records):
#     answer = []
#     dic ={}

#     for i in records:
#         time, car_n, bd = i.split(' ')

#         if car_n in dic:
#             temp = dic.get(car_n)
#             temp.append(time)
#         else:
#             dic[car_n] = [time]


#     for k,li_ in dic.items():
#         time = datetime.datetime.strptime('00:00',"%H:%M")
#         while li_:
#             if len(li_) %2 == 1 :
#                 time_1 = datetime.datetime.strptime('23:59',"%H:%M")
#                 time_2 = datetime.datetime.strptime(li_.pop(),"%H:%M") 
#                 time = time_1 - time_2

#             else:
#                 time_1 = datetime.datetime.strptime(li_.pop(),"%H:%M")
#                 time_2 = datetime.datetime.strptime(li_.pop(),"%H:%M") 
#                 time_temp = time_1 - time_2 
#                 time = time + time_temp

#         time= str(time)
#         time = time[-8:]
#         h,m,s =map(int, time.split(':'))
#         base = h*60 + m
#         if base <= fees[0]:
#             dic[k] = fees[1]
#         else:
#             time =h*60 + m - fees[0]

#             if time%fees[2] == 0:
#                 dic[k] = fees[1] + (time//fees[2])*fees[3]
#             else:
#                 dic[k] = fees[1] + (time//fees[2]+1)*fees[3]

#     dic_sort = sorted(dic.items())
#     for i in range(len(dic)):
#         a= list(dic_sort[i])
#         answer.append(a[1])
    
    
        
#     return answer