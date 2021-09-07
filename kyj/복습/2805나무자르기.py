import sys
input = sys.stdin.readline

def get_tree():
    n,m = map(int,input().split())
    tree = list( map(int,input().split()))

    fst = 1
    end = max(tree)

    while fst <= end:
        mid = (fst + end) //2
        get = 0
        for i in tree:
            if i > mid:
                get += i - mid
        
        if get >= m :
            fst = mid + 1
        else : 
            end = mid - 1
    return end

print(get_tree())