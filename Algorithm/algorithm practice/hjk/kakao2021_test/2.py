import re
def solution(n, k):
    
    temp = n
    temp_str = ""
    
    while temp > 0:
        temp, mod = divmod(temp, k)
        temp_str += str(mod)
        
    n_jin = temp_str[::-1]
    
    answer = n_jin.split("0")
    prime_list = []
    
    for i in answer:
        if i != "":
            prime_list.append(int(i))
            
    if len(prime_list) == 0:
        return 0
    
    answer = 0
    for i in prime_list:
        if i == 1:
            continue
        for j in range(2, int(i**0.5)+1):
            
            if i % j == 0:
                break
        else:
            answer += 1

    return answer