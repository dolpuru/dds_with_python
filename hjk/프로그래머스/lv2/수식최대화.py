def solution(expression): # 특이한 알고리즘이 필요한게 아니라 단순 구현 같은데 .. ! split를 이용하면 바로 될 것 같음
    s_list = [["-","+","*"],["-","*","+"],["+","-","*"],["+","*","-"],["*","-","+"],["*","+","-"]]

    answer = 0
    for i in range(6):
        temp = expression 
        s = s_list[i]
        first,second,third = 0, 1, 2
        first_value_list = list(map(str, temp.split(s[first]))) # 첫번째 요소로 나누기
        print(first_value_list)
        second_value_list = []
        for j in range(len(first_value_list)):
            second_value_list.append(list(map(str, first_value_list[j].split(s[second])))) # [[,,],[,,]]
            
        temp_second_list = [[] for _ in range(len(second_value_list))] # 마지막 요소 시행
        
        print("s first", s[first])
        print("s second", s[second])
        print("s third", s[third])
        print("second_value_list", second_value_list)
        for k in range(len(second_value_list)):
            for m in range(len(second_value_list[k])):
                if s[third] == "+":
                    temp = list(map(int, second_value_list[k][m].split("+")))
                    temp_second_list[k].append(sum(temp))
            
                elif s[third] == "-":

                    temp = list(map(int, second_value_list[k][m].split("-")))
                    temp_minus = temp[0]
                    for l in range(1, len(temp)):
                        temp_minus -= temp[l]
                    temp_second_list[k].append(temp_minus)
                    
                elif s[third] == "*":
                    temp = list(map(int, second_value_list[k][m].split("*")))
                    temp_mul = temp[0]
                    for l in range(1, len(temp)):
                        temp_mul *= temp[l]
                    temp_second_list[k].append(temp_mul)
        
        print("temp_second_list", temp_second_list)
        temp_first_list = [] # 두번쨰 요소 시행
        
        for k in range(len(temp_second_list)):
            if s[second] == "+":
                temp_first_list.append(sum(temp_second_list[k]))

            else:
                temp = temp_second_list[k][0]
                for m in range(1, len(temp_second_list[k])):

                    if s[second] == "-":
                        temp -= temp_second_list[k][m]

                    elif s[second] == "*":
                        temp *= temp_second_list[k][m]

                temp_first_list.append(temp)

        print("temp_first_list", temp_first_list)
        # 마지막 리스트 합치기
        if s[first] == "+":
            temp_answer = sum(temp_first_list)
        else:
            temp_value = temp_first_list[0]
            for k in range(1,len(temp_first_list)):
                if s[first] == "-":
                    temp_value -= temp_first_list[k]
                elif s[first] == "*":
                    temp_value *= temp_first_list[k]
            temp_answer = temp_value
        answer = max(abs(temp_answer), abs(answer))
        print("answer", answer)
        print("\n")
    return answer

print("result !!!! : " , solution("100-200*300-500+20"))

print("result !!!! : ", solution("50*6-3*2"))