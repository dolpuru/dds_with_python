sizes = 	[[60, 50], [30, 70], [60, 30], [80, 40]]

w = []
h = []

for i in sizes:
    if i[0] > i[1]:
        w.append(i[0])
        h.append(i[1])
    else: 
        w.append(i[1])
        h.append(i[0])

w_max = max(w)
w_index = w.index(w_max)
li = []
for i in h:
    if h[w_index] <= i :
        li.append(i)
answer = w_max * max(li)

print(w)
print(h)

print(answer)

    
    

