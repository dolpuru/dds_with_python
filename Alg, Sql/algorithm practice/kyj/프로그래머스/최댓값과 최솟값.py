s= "1 2 3 4"
answer = ''

s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])


s.sort()
answer = str(s[0]) + " " + str(s[-1])
print( answer)