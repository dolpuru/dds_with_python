from collections import defaultdict

dict = defaultdict(list)
for i in range(len(list)):
    dict[list[i][1]] += [list[i][0]]
print(dict)