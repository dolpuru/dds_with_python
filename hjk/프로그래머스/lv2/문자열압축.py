def solution(s):
    answer = len(s) # 문자열 자르는 길이가 1일때 , # 어차피 젤 앞에서부터 잘라야한단다.
    
    
    
    def format_string( slice_len, s):
        check_stack = []
        temp_length = len(s)

        check_form = ["1"]

        for j in range(0, len(s), slice_len):
            if len(check_stack) == 0: 
                check_stack.append(s[j:j + slice_len])
                print(s[j:j + slice_len])

            else:
                if check_stack[-1] == s[j:j + slice_len]:
                    if check_form[0] == s[j:j + slice_len]:
                       temp_length -= slice_len 
                    else:
                        check_form[0] = s[j:j + slice_len]
                        # temp_length += 1
                    
                    print("temp_length : " , temp_length)
                else:
                    check_stack.append(s[j:j + slice_len])
        print(check_stack)
        print("temp_length2 : " , temp_length)
        return temp_length
    
    for slice_len in range(1, len(s)):

        answer = min ( format_string(slice_len, s), answer)

    print(answer)    
    return answer
solution("aabbaccc")