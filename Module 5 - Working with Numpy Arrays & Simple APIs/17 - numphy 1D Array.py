# Numpy is a library for scientific computing. It has many useful functions.
# There are many other advantages like speed an memory.
# Numpy is also the basis for pandas, so check out our pandas video.
# As numpy arrays contain data of the same type, we can use the attribute "dtype" to obtain


import numpy as np
array = np.array([1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7])

print(type(array))  # <class 'numpy.ndarray'>
print(array.dtype)  # int64
print(array.size)
print(array.ndim)
