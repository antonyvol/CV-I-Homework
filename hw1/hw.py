import numpy as np

# task 1
print(np.zeros(10))
print('\n')

# task 2
matrix = np.arange(9).reshape(3, 3)
print(np.multiply(matrix, np.full(matrix.shape, 3))) # scalar multiplication 
print('\n')

# task 3
a = np.matrix([[1, 4], [2, 5], [3, 6]])
b = np.matrix([[1, 0], [0, 1], [0, 0]])
res_matrix = np.transpose(a).dot(b)
print(res_matrix)
print('\n')

# task 4
v = np.matrix([[-1, 1], [-1, 1]])
print(np.add(res_matrix, v))
print('\n')

# task 5
x = np.random.rand(3, 3)
f1 = np.vectorize(lambda x : 1 if x > 0.5 else 0)
c = f1(x).astype(bool)
f2 = np.vectorize(lambda c, x : -1 if c else x)
res = f2(c, x)
print(res)
print('\n')

