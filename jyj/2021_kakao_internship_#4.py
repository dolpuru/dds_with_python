def swap(a, b):
  return b, a


def solution(n, start, end, roads, traps):
  vert = [9999999 for i in range(n+1)]
  reverse_vert = [9999999 for i in range(n+1)]        
  is_reversed = [0 for i in range(n+1)]    
  edge = [[] for i in range(n+1)]
  reverse_edge = [[] for i in range(n+1)]

  for road in roads:
    edge[road[0]].append([road[1], road[2]]) 
    reverse_edge[road[1]].append([road[0], road[2]]) 



  idx = start
  stack = [start]
  vert[start] = 0

  while len(stack) > 0:
    print(stack)
    idx = stack.pop()
    for i in edge[idx]:
      if vert[i[0]] != 9999999: continue
      for j in edge[i[0]]:
        stack.append(j[0])

      if i[0] in traps:
        is_reversed[i[0]] = 1
        if is_reversed[i[0]] == 1:
          edge[i[0]], reverse_edge[i[0]] = swap(edge[i[0]], reverse_edge[i[0]])
          for j in edge[i[0]]:
            for k in edge[j[0]]:
              if k[0] == i[0]:
                reverse_edge[j[0]].append(k)
                edge[j[0]].remove(k)
          reverse_vert[i[0]] = min(reverse_vert[i[0]], vert[idx]+i[1])
        else:
          edge[i[0]], reverse_edge[i[0]] = swap(edge[i[0]], reverse_edge[i[0]])
          vert[i[0]] =  min(vert[i[0]], vert[idx]+i[1])
      else:
        vert[i[0]] = min(vert[i[0]], vert[idx]+i[1])
      
      
  print(vert)
  print(reverse_vert)
  print(edge)
  print(reverse_edge)

  return 0

#solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3])
