def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    answer = [ [0 for i in range(col)] for i in range(row)]
    for r in range(row):
        for c in range(col):
            for k in range(len(arr2)):
                answer[r][c] += arr1[r][k] * arr2[k][c]
    return answer

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

# answer = [[0]*len(arr2)]*len(arr1)
# print(answer)
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         for k in range(len(arr2)):
#             answer[i][j] += arr1[i][k] * arr2[k][j]

# print(answer)
