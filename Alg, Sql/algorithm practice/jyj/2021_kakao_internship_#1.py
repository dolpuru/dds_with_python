array = [4, 3, 3, 5,4 , 4, 3, 5, 5, 4]
find = ["ze", "on", "tw", "th", "fo", "fi", "si", "se", "ei", "ni"]

def solution(s):
  result = ""
  length = len(s)
  i = 0
  while i < length:
    if s[i].isdigit():
      result += s[i]
      i+=1
    else:
      idx = find.index(s[i:i+2])
      result += str(idx)
      i += array[idx]
  return int(result)



solution('one4seveneight')
