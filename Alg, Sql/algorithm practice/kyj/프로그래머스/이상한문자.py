s = "try hello world"
li = s.split(" ")

s = []
for i in range(len(li)):
    str_ = list(li[i])
    for j in range(len(str_)):
        if j%2 == 0:
            str_[j] = str_[j].upper()
        elif j %2 == 1:
            str_[j] = str_[j].lower()
    li[i] = "".join(str_)
    
print(" ".join(li))