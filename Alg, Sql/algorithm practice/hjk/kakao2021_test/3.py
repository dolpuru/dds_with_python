import math 

def solution(fees, records):
    # 각 차량에 대한 분을 저장하고, 계산하는 함수를 만든다.
    cardic = {}
    total_car_time = {}
    cardic_in = {}
    cardic_out = {}
    for i in records:
        t, c, s = i.split()
        cardic[c] = []    
        total_car_time[c] = 0
        cardic_in[c] = []
        cardic_out[c] = []
        
    for i in records:
        t, c, s = i.split()
        
        a, b = t.split(":")
        if s == "IN":
            cardic_in[c].append(a+b) # 짝수번째는 in 훌수번째는 out 만약에 나중에 갯수가 홀수개면 23:59에 출차한걸로 간주해야하므로 값을 따로 넣는다.
        else:
            cardic_out[c].append(a+b)
    
    
    for i in records:
        t, c, s = i.split()
        if (len(cardic_out[c]) + len(cardic_in[c])) % 2 == 1: #갯수가 홀수인거 처리
            cardic_out[c].append("2359")
            
    print("cardic: ", cardic)
    
    # 짝수번쨰 다 더하고 홀수번쨰는 다 합친 뒤에 뺴주자 ( 중간에 10진번 변환 해주고
    for i in list(cardic.keys()):
        print(i)
        
        in_cnt = 0
        out_cnt = 0
        for j in range(len(cardic_in[i])):
            in_cnt += int(cardic_in[i][j][:2]) * 60 + int(cardic_in[i][j][2:])
            
        for j in range(len(cardic_out[i])):    
            out_cnt += int(cardic_out[i][j][:2]) * 60 + int(cardic_out[i][j][2:])
        total_car_time[i] = abs(in_cnt - out_cnt)
        
    print("total_car_time : ", total_car_time)
    # for i in range(len(totla_car_time)):
    temp_temp =[]
    temp_temp2 =[]
    for i in total_car_time.keys():
        temp_temp.append(int(i))
        temp_temp2.append(i)
    print(temp_temp)
    print(temp_temp2)
    temp_temp.sort()
    temp_temp2.sort()
    print(temp_temp)
    print(temp_temp2)
    
    # ... 와 너무 좋은 문제였어용
    # 차량번호 적은 순으로 정렬
    sorted_list = sorted(temp_temp2)
    # 요금계산
    print(sorted_list)
    
    answer = []
    for i in sorted_list:
        if total_car_time[i]  <= fees[0]:
            answer.append(fees[1])
            
        else:
            temp_value = math.ceil((total_car_time[i] - fees[0] ) / fees[2])
            
                
            answer.append(fees[1] + ( temp_value * fees[3])  )
    
    return answer