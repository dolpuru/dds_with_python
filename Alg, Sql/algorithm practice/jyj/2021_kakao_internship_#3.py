def solution(n, k, cmd):
    array = [i for i in range(n)]
    removed = []

    for c in cmd:
      if c[0] == 'D':
        k += int(c[2:])
      elif c[0] == 'U':
        k -= int(c[2:])
      elif c[0] == 'C':
        remove = array.pop(k)
        removed.append([remove, k]) # 삭제된 원소의 숫자와 삭제 될 때의 인덱스를 저장
        if k == len(array):
          k -=1
      elif c[0] == 'Z':
        latest = removed.pop()
        if array[k] > latest[0]:
          k+=1
        array.insert(latest[1], latest[0])
        
    x_cnt = 0
    result = ""
    i=0
    j=0
    while i < n:
      if j >= len(array) : j-=1
      if i != array[j]:
        result += "X"
        i+=1
      else:
        result+= "O"
        i+=1
        j+=1


      
    return result

solution(8, 2, 	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
solution(8, 7, ["C","C","C","C","C"])
