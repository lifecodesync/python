# 17. Addition of two 3x3 matrices using nested lists
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        result[i][j] = A[i][j] + B[i][j]
print("Matrix A + Matrix B:")
for row in result:
    print(row)
