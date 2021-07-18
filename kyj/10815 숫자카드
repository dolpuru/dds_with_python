N = int(input())
N_card = list(map(int , input().split()))
M = int(input())
M_list = list(map(int , input().split()))

N_card.sort()

def find_n(fst, end, M , N_card):
    mid = (fst + end)//2
    if fst > end:
        return 0 
    elif M > N_card[mid]:
        return find_n(mid+1,end,M,N_card)
    elif M < N_card[mid]:
        return find_n(fst,mid-1,M,N_card)
    else:
        return 1


for i in M_list:
    fst = 0
    end = len(N_card)-1
    print(find_n(fst,end,i,N_card))
