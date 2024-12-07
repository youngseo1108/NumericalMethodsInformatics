import numpy as np
from ctscanner import CTScanner

# Task a)
# Implement a method, calculating the rowrank of a given matrix and return it.
# Obviously, you're not allowed to use any method solving that problem for you.
def rowrank(matrix):
  count = np.prod(matrix[0].shape)
  num_row = np.prod(matrix[:,0].shape)

  # Find the # of linearly independent rows
  for r in range(0, count):
    # If the diagonal element is non-zero
    if matrix[r,r] != 0:
    # below a pivot, mat[row,0:row-1] = 0
      for c in range(0, num_row):
        if c != r:
          lam = matrix[c,r] / matrix[r,r]
          for i in range(count):
            matrix[c,i] -= lam * matrix[r,i]
                                                 
    # If the diagonal element is zero
    else:
      row_reduction = True

      for j in range(r+1, num_row):
        # 1) If there's a row with non-zero entry in the column
        if matrix[j,r] != 0:
          # Swap the row with non-zero element with this row.
          matrix[[r,j]] = matrix[[j,r]]
          row_reduction = False
          break

      # 2) If not (i.e. all elements in the column are 0)
      if row_reduction:
        # Reduce number of columns
        count -= 1
        # copy the last column
        for k in range(0, num_row, 1):
          matrix[k,r] = matrix[k,count]
      # repeat the process for other rows
      r -= 1
  return count


# Task b)
# Implement a method setting up the linear system, as described in the exercise.
# Make use of the scanner.shootRays(angle) function.
def setUpLinearSystem(scanner):
  A = np.ones((scanner.resolution ** 2, scanner.resolution ** 2))
  b = np.zeros(scanner.resolution ** 2)

  indices = []
  intensities = []
  lengths = []

  for angle in np.arange(0, np.degrees(np.pi)):
    index, intensity, length = scanner.shootRays(angle)
    indices.extend(index)
    intensities.extend(intensity)
    lengths.extend(length)

  for i in range(0, 400):
    b[i] = intensities[i]

  for idx in range(0, 400):
    for j in range(0, len(indices[idx])):
      A[idx, indices[idx][j]] = lengths[idx][j]
  return A, b


# Task c)
# Implement the gaussian elimination method, to solve the given system of linear equations
# Add full pivoting to increase accuracy and stability of the solution
def swap_row(m, i, j):
  m_copy = m.copy()
  if len(m_copy.shape) == 1:
    t = m_copy[i]
    m_copy[i] = m_copy[j]
    m_copy[j] = t
  else:
    m_copy[[i,j],:] = m_copy[[j,i],:]
  return m_copy

def swap_col(m, i, j):
  m_copy = m.copy()
  m_copy[:,[i,j]] = m_copy[:,[j,i]]
  return m_copy

def solveLinearSystem(A, b): # A: coefficient matrix, b = vector
  n = np.size(b)
  
  s = np.zeros(n)
  for i in range(n):
    s[i] = max(np.abs(A[i,:]))

  for k in range(0, n-1):
    # row pivoting
    l = np.argmax(np.abs(A[k:n,k]) / s[k:n]) + k
    if l != k:
      swap_row(b,k,l)
      swap_row(s,k,l)
      swap_row(A,k,l)

    # Gaussian elimination
    for i in range(k+1, n):
      if A[i,k] != 0.0:
        cof = A[i,k] / A[k,k]
        A[i,k+1:n] = A[i,k+1:n] - cof*A[k,k+1:n]
        b[i] = b[i] - cof*b[k]

  # back substitution
  b[n-1] = b[n-1] / A[n-1,n-1]
  for k in range(n-2, -1, -1):
    b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n])) / A[k,k]
  
  return b