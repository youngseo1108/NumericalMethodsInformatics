import numpy as np

# Task a)
# Implement a method, calculating the largest eigenvector of A with b as an initial guess.
# Input: Matrix A, Vector b. A - 2D numpy array, b - 1D numpy array
# Output: The Eigenvector of A with the largest (absolute) Eigenvalue, given as 1D np.array.
def powerMethod(A: np.array, b: np.array) -> np.array:
  tolerance_value = 1e-10
  m = 1.0
  condition =  True
  b = b / max(abs(b))
  while condition:
    b = np.matmul(A,b)
    m_new = max(abs(b))    
    b = b/m_new
    error = abs(m_new - m)
    m = m_new
    condition = error > tolerance_value
  return b


# Task b)
# Implement a method, calculating the smallest eigenvector of A with b as an initial guess.
# Input: Matrix A, Vector b. A - 2D numpy array, b - 1D numpy array
# Output: The Eigenvector of A with the smallest (absolute) Eigenvalue, given as 1D np.array.
def inversePowerMethod(A: np.array, b: np.array) -> np.array:
  n = len(A)
  I = np.eye(n)
  # initial guess for alpha (A-a*I)
  a = 0
  np.seterr(all = 'ignore')
  b = b / max(abs(b))
  # error
  error = 1
  condition = True
  tolerance_value = 1e-10
  v = 1.0
  while condition:
    try:
      y = np.linalg.solve(A - a * I, b)       
    except:
      return 'Invalid Input'
    m = max(abs(y))
    v_new = (1. / m) + a
    b = y / m
    error = abs(v_new - v)
    v = v_new
    condition = error > tolerance_value
  return b


# Task c)
# Implement a method performing a PCA on given data.
# Input: Vectors x,y. Both 1D np.array of same size.
# Output: The Principal direction of the given data, represented as 1D np.array
def linearPCA(x: np.array, y: np.array) -> np.array:
  data = np.array([x,y])
  D = np.cov(data, bias = True)
  covMatrix = np.matmul(D.T, D)
  w, v = np.linalg.eigh(covMatrix)
  idx = np.argwhere(w == max(abs(w)))[0][0]
  return v[idx]