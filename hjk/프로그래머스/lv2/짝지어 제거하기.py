# # 시간초과
# # def solution(s): # 지우고 또 지워야해서 개수 세어서 푸는건 불가.
# #     answer = -1
# #     s = s.upper()
# #     check_list = []
    
# #     i = 0
# #     while i < len(s)-1:
# #         if s[i] == s[i+1]:
# #             s = s[:i] + s[i+2:]
# #             i = 0
# #             continue
# #         i += 1
        
# #     if s:
# #         answer = 0
# #     else:
# #         answer = 1

# #     return answer

# def solution(s): # 지우고 또 지워야해서 개수 세어서 푸는건 불가.
#     answer = -1
#     s = s.upper()
#     check_list = []
    
#     i = 0
#     while i < len(s)-1:
#         if s[i] == s[i+1]:
#             s = s[:i] + s[i+2:]
#             i = 0
#             continue
#         i += 1
        
#     if s:
#         answer = 0
#     else:
#         answer = 1

#     return answer

import re
a = "aabbc1"
c = "cdcd"
def solution(s): # 지우고 또 지워야해서 개수 세어서 푸는건 불가.
    answer = re.sub("([a-z]){2})","",s)
    while True:
        temp = re.sub("([a-z]){2}","",answer)
        answer = re.sub("([a-z]){2}","",temp)
        if answer == temp:
            break
    print(answer)       
    if len(answer) == 0:
        return 1
    else:
        return 0
print(solution(a))
print(solution(c))