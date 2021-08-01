def solution(s):
    answer = len(s) # 문자열 자르는 길이가 1일때 , # 어차피 젤 앞에서부터 잘라야한단다. # 더 짧게 풀 수 있을텐데 .. .ㅠㅠㅠㅠ
    
    
    def format_string( slice_len, s):
        check_stack = []
        temp_length = len(s)
        

        check_stack.append(s[:slice_len])
        cnt = 1
        flag = 0
        
        for j in range(slice_len, len(s), slice_len):
            
            temp_str = s[j:j + slice_len]

            if check_stack[-1] == temp_str:
                cnt += 1
                temp_length -= slice_len 
                flag = 1
            else:
                check_stack.append(s[j:j + slice_len])
                if flag == 1:    
                    if 10 > cnt:
                        temp_length += 1
                        cnt = 1
                    if 100> cnt >= 10:
                        temp_length += 2
                        cnt = 1
                    elif 1000> cnt >= 100:
                        temp_length += 3
                        cnt = 1
                    elif cnt == 1000:
                        temp_length += 4
                        cnt = 1
                    flag = 0

        if 10 > cnt > 1:
            temp_length += 1
            cnt = 1
        if 100> cnt >= 10:
            temp_length += 2
            cnt = 1
        elif 1000> cnt >= 100:
            temp_length += 3
            cnt = 1
        elif cnt == 1000:
            temp_length += 4
            cnt = 1
        flag = 0

        return temp_length
    
    
    for slice_len in range(1, len(s)):
        answer = min ( format_string(slice_len, s), answer)

 
    return answer