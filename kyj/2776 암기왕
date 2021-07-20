T = int(input())

def find_M():
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    for i in note2:
        fst = 0
        end = len(note1) -1 
        while (1):
            mid = (fst + end) //2
            if fst > end :
                print(0)
                break
            elif note1[mid] > i:
                end = mid - 1
            elif note1[mid] < i :
                fst = mid + 1
            else :
                print(1)
                break
            

for  i in range(T):
    find_M()
