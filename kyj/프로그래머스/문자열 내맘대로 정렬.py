strings = ["sun", "bed", "car"]
n = 1

answer = []
result = []
strings.sort()
for i in strings:
    answer.append(i[n] + i)
answer.sort() 
for i in  answer:
    result.append(i[1:])

print(result)