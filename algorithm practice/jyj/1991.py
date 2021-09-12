import sys
from collections import deque
input = sys.stdin.readline

array = []

def preorder(index):
    print(chr(index+65), end='')
    if array[index][0] != -19:
        preorder(array[index][0])
    if array[index][1] != -19:
        preorder(array[index][1])

def inorder(index):
    if array[index][0] != -19:
        inorder(array[index][0])
    print(chr(index+65), end='')
    if array[index][1] != -19:
        inorder(array[index][1])

def postorder(index):
    if array[index][0] != -19:
        postorder(array[index][0])
    if array[index][1] != -19:
        postorder(array[index][1])
    print(chr(index+65), end='')

def func():
    preorder(0)
    print()
    inorder(0)
    print()
    postorder(0)


if __name__ == '__main__':
    N = int(input())
    array = [['', ''] for i in range(N)]
    for i in range(N):
        index, left, right = map(str, input().split(' '))
        index_ = ord(index[0]) - 65
        array[index_][0] = ord(left[0])- 65
        array[index_][1] = ord(right[0])-65
    func()

