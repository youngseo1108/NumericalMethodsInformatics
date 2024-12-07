import numpy as np

#b = np.array([-14.0, 36.0, 6.0])
#n = np.prod(b.shape)
#print(n)

my_matrix = np.array([[1, 2, 1], [3, 4, 7], [3, 6, 3], [4,5,6]])
#print("Matrix")
#for row in my_matrix:
#    print(row)

#rank = len(matrix[0]) # self.C = len(Matrix[0])
#num_row = len(matrix) # self.R = len(matrix)

print(len(my_matrix[0])) # column length / self.C
print(len(my_matrix))
print(np.prod(my_matrix[:,0].shape))
#print(len(my_matrix)) # row length / self.R
#print(np.prod(my_matrix.shape))
#print(np.prod(my_matrix[0].shape))
#rank = np.linalg.matrix_rank(my_matrix)
#print("Rank of the given Matrix is : ",rank)

import numpy as np
print(np.degrees(180))
print(np.angle(180))
print(np.degrees(np.pi))