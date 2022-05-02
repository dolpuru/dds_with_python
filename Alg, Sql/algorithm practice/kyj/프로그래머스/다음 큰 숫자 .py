n=78

answer = n +1
n_c = str(bin(n)).count('1')
print(n_c)
while str(bin(answer)).count('1') != n_c:
    answer += 1
    print(bin(answer))

print(answer)