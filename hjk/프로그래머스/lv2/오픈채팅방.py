def solution(record): # uid의 수정을 다 마친 다음 포맷팅으로 넣어줄 것. 모든 리스트엔 uid가 들어간다., uid가 무조건 소문자라는 조건은 없었다... 문제를 잘 읽어보자 .... 
    
    
    def find_uid_and_name( record_i, option):
        temp_uid = ""
        temp_name = ""
        first_blank = record_i.find(" ")
        length = len(record_i)
        if option == "F":
            temp_name = record_i[first_blank+1:]
        else:
            first_blank = record_i.find(" ")
            for temp in range(first_blank+1, length):        
                    if record_i[temp] == " ":
                        temp_name = record_i[temp+1:]
                        break
                    else:
                        temp_uid += record_i[temp]
                    
            return temp_uid, temp_name
    
    answer = []
    uid_list = {}
    length = len(record)
    
    for i in range(length):
        
        
        if record[i][0] == "E":
            temp_uid, temp_name = find_uid_and_name(record[i], "E")
            uid_list[temp_uid] = temp_name
        

        elif record[i][0] == "C":
            temp_uid, temp_name = find_uid_and_name(record[i],"C")
            uid_list[temp_uid] = temp_name
    
    for i in range(length):
        
        if record[i][0] == "E":
            temp_uid, temp_name = find_uid_and_name(record[i],"E")
            answer.append(f"{uid_list[temp_uid]}님이 들어왔습니다.")
            
        elif record[i][0] == "L":
            temp_uid, temp_name = find_uid_and_name(record[i],"L")
            answer.append(f"{uid_list[temp_uid]}님이 나갔습니다.")

    return answer
