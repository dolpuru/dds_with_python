s = 	"{{20,111},{111}}"
answer = []
s_li = s.split("},")
for i in range(len(s_li)):
    s_li[i] = s_li[i].replace("{","")
    s_li[i] = s_li[i].replace("}","")
    s_li[i] = s_li[i].split(",")

s_li.sort(key = len)

for i in s_li:
    for j in i:
        if int(j) not in answer:
            answer.append(int(j))
            break
print(answer)
