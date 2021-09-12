array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for i in range(len(commands)):
    temp = array[commands[i][0]-1:commands[i][1]]
    temp.sort()
    answer.append(temp[commands[i][2]-1])

