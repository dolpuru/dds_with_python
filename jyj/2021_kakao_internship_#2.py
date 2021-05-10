
i_acc = [1, -1, 0, 0]
j_acc = [0, 0, 1, -1]
i_acc2 = [[2,1,1], [-2,-1,-1],[0,1,-1],[0,1,-1],]
j_acc2 = [[0,1,-1], [0,1,-1],[2,1,1],[-2,-1,-1],]

size = 5
def check(i, j , array):
  global size

  X_array = [] # e, w, s, n
  for k in range(4):
    i_ = i+i_acc[k]
    j_ = j+j_acc[k]
    if i_ >= 0 and j_ >= 0 and i_<size and j_< size:
      if array[i_][j_] == 'P':
        return False
      elif array[i_][j_] == 'O':
        for r in range(3):
          i__ = i+i_acc2[k][r]
          j__ = j+j_acc2[k][r]
          if i__ >= 0 and j__ >= 0 and i__<size and j__< size:
            if array[i__][j__] == 'P':
              return False
      
  return True


def solution(places):
  global size
  answer = []
  for place in places:
    array = []
    for alphabet in place:
      array.append(list(alphabet))

    success = 1
    for i in range(size):
      for j in range(size):
        if array[i][j] == 'P':
          ans = check(i, j, array)
          if ans == False:
            success = 0

    answer.append(success)


  return answer

ex = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(ex)
