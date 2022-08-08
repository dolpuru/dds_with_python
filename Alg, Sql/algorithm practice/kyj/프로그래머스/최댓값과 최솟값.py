 # def solution(s):
#     answer = ''

#     s = s.split()
#     for i in range(len(s)):
#         s[i] = int(s[i])

#     s.sort()
#     answer = str(s[0]) + " " + str(s[-1]) 
#     return answer
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " "+ str(max(s))