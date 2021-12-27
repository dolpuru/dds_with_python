N , M = map(int, input().split())
tree = list(map(int, input().split()))

def get_tree(hi,tree):
    get = 0
    for i in tree:
            if hi< i:
                get = get + i - hi
    return get
    
fst = 0
end = max(tree)

while fst <= end:
    mi = (fst + end)//2
    get = get_tree(mi, tree)

    if get >= M:
        fst = mi+1

    else :
        end = mi -1

print(end)
