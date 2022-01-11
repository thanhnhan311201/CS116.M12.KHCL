import numpy as np

# 1.1. Array
# a = np.array([1, 2, 3])
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
# print(a)

# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b.shape)
# print(b[0, 0], b[0, 1], b[1, 0])

# 1.2. Array
# a = np.zeros((2, 2))
# print(a)
# b = np.ones((1, 2))
# print(b)
# c = np.full((2, 2), 7)
# print(c)
# d = np.eye(2)
# print(d)
# e = np.random.random((2, 2))
# print(e)

# 2.1. Indexing
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b = a[:2, 1:3]
# print(b)
# print(a[0, 1])
# b[0, 0] = 77
# print(a[0, 1])

# 2.2. Indexing
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# row_1 = a[1, :]
# row_2 = a[1:2, :]
# print(row_1, row_1.shape)
# print(row_2, row_2.shape)

# col_1 = a[:, 1]
# col_2 = a[:, 2]
# print(col_1, col_1.shape)
# print(col_2, col_2.shape)

# 2.3. Indexing
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a[[0, 1, 2], [0, 1, 0]])
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
# print(a[[0, 0], [1, 1]])
# print(np.array([a[0, 1], a[0, 1]]))

# 2.4. Indexing
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(a)

# b = np.array([0, 2, 0, 1])
# print(a[np.arange(4), b])

# a[np.arange(4), b] += 10
# print(a)

# 2.5. Indexing
# a = np.array([[1, 2], [3, 4], [5, 6]])

# bool_inx = (a > 2)

# print(bool_inx)
# print(a[bool_inx])
# print(a[a > 2])

# 2.6. Indexing
# x = np.array([1, 2])
# print(x.dtype)

# x = np.array([1.0, 2.0])
# print(x.dtype)

# x = np.array([1, 2], dtype=np.int64)
# print(x.dtype)

# 3.1. Thao tác trên Array
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# y = np.empty_like(x)

# for i in range(4):
#     y[i, :] = x[i, :] + v

# print(y)

# 3.2. Thao tác trên Array
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0 ,1])
# vv = np.tile(v, (4, 1))

# print(vv)

# vv2 = np.tile(v, (4, 2))
# print(vv2)

# y = x + vv
# print(y)

# 3.3. Thao tác trên Array
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])

# print(v+x)

# 3.4. Thao tác trên Array
# v = np.array([1, 2, 3])
# w = np.array([4, 5])

# x = np.array([[1, 2, 3], [4, 5, 6]])

# print(x + v)
# print((x.T + w).T)
# print(x * 2)