# Numpy is a library for scientific computing. It has many useful functions.
# There are many other advantages like speed an memory.
# Numpy is also the basis for pandas, so check out our pandas video.
# As numpy arrays contain data of the same type, we can use the attribute "dtype" to obtain
# numpy arrays are mutable

import numpy as np
# if there is a single float element the array will be float array
# array1 = np.array([1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7])
# array2 = np.array([7.9, 5.6, 2.1, 9.1, 6.24, 7.4, 12.01])

# print(type(array1))  # <class 'numpy.ndarray'>
# print(array1.dtype)  # int64
# print(array2.dtype)  # float64

# print(array1.size)
# print(array1.ndim)

# print(array2[1:3])  # [5.6 2.1]
# array2[0] = 9.9
# print(array2)  # [ 9.9   5.6   2.1   9.1   6.24  7.4  12.01]


# ----- Vector addition -----


# non Optamize
u = np.array([1, 2])  # 1 column
v = np.array([3, 4])  # 2 column
nonOptSum = u+v

print('Non optimized vector sum : ', nonOptSum)  # [4 6]


# Optamized
OptSum = []
for i, j in zip(u, v):
    OptSum.append(int(i + j))  # Convert to native Python int
print("Optimized vector sum :", OptSum)


# ----- Vector Subtraction -----

sub = []
for i, j in zip(u, v):
    sub.append(int(i-j))
print("Vector subtraction : ", sub)


# ----- Vector Multiplication and Division with Scalar -----

scalarMul = []
for n in u:
    scalarMul.append(int(2*n))
print("Scalar Multiplication : ", scalarMul)  # [2, 4]


scalarDiv = []
for n in u:
    scalarDiv.append(float(n/2))

print("Scalar Division : ", scalarDiv)  # [0.5, 1.0]

print(np.array([1, -1])*np.array([1, 1]))


# ----- Dot Product -----


dotProduct = np.dot(u, v)  # 1*3 + 2*4 = 8+3
print(dotProduct)  # 11
print(np.dot(np.array([1, -1]), np.array([1, 1])))


# Universal Functions


mean_u = u.mean()  # takes average of all the array elements
print("Mean of u : ", mean_u)

max_v = v.max() / np.pi  # find maximum of all the array elements
print("Max of v : ", max_v)  # divided maximum value with pi

min_v = v.min()  # find maximum of all the array elements
print("Min of v : ", min_v)


max_v_radians = np.radians(max_v)
min_v_radians = np.radians(min_v)


cos_max_v = np.cos(max_v_radians)
print("cos of max v : ", cos_max_v)  # 0.9997530965806385


sin_min_v = np.sin(min_v_radians)  # 0.052335956242943835
print("sin of min v : ", sin_min_v)


# Generate sample space


sampleSpace = np.linspace(-2, 2, num=10)
# generating evenly spaced elements of 10 from range of -2 to 2

print("sample space : ", sampleSpace)
