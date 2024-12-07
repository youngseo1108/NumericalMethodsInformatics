import numpy as np

# Task a)
# Implement a method, calculating the LU factorization of A.
# Input: Matrix A - 2D numpy array (e.g. np.array([[1,2],[3,4]]))
# Output: Matrices P, L and U - same shape as A each.
def calculate_p(A):
  n = A.shape[0]
  P = np.eye(n)

  for i in range(n):
    row = max(range(i,n), key = lambda j: abs(A[j,i]))
    if i != row: # Swap the rows
      P[[i,row],:] = P[[row,i],:]
  return P

def lu(A):
  n = A.shape[0]
  L = np.eye(n)
  U = np.zeros(A.shape)
  
  P = calculate_p(A)
  PA = np.matmul(P, A)
    
  for j in range(n):
    for i in range(j+1):
      U[i,j] = PA[i,j] - np.dot(U[0:i,j],L[i,0:i])
    for i in range(j, n):
      L[i,j] = (PA[i,j] - np.dot(U[0:j,j], L[i,0:j])) / U[j,j]

  return P, L, U


# Task b)
# Implement a method, calculating the determinant of A.
# Input: Matrix A - 2D numpy array (e.g. np.array([[1,2],[3,4]]))
# Output: The determinant - a floating number
def determinant(A):
  n = A.shape[0]
  mat = A.copy()

  for k in range(0, n-1):
    for i in range(k+1, n):
      if not np.isclose(mat[i,k], 0.0):
        coef = mat[i,k] / mat[k,k]
        mat[i,k:n] -= coef*mat[k,k:n]

  return np.prod(np.diag(mat))