
import numpy as np

l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matrix1 = np.array(l1)
matrix2 = np.array(l2)


matrix3 = matrix1+matrix2

# print(l1.ndim)
print("Matrix 1 ", matrix1)
print("Matrix 2 ", matrix2)
print("Matrix 3 ", matrix3)


# A = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.dot(A, B))
#  ValueError: shapes (4,2) and (3,3) not aligned: 2 (dim 1) != 3 (dim 0)
