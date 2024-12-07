import numpy as np

def swapRows(vm, i, j):
  vc = vm.copy()
  if len(vc.shape) == 1:
    t = vc[i]
    vc[i] = vc[j]
    vc[j] = t
  else:
    vc[[i,j],:] = vc[[j,i],:]
  return vc

def solveLinearSystem(A, b): # A: coefficient matrix, b = vector
  n = len(b)
  
  s = np.zeros(n)
  for i in range(n):
    s[i] = max(np.abs(A[i,:]))

  for k in range(0, n-1):
    # row pivoting
    p = np.argmax(np.abs(A[k:n,k]) / s[k:n]) + k
    if p != k:
      swapRows(b,k,p)
      swapRows(s,k,p)
      swapRows(A,k,p)

    # elimination
    for i in range(k+1, n):
      if A[i,k] != 0.0:
        lam = A[i,k] / A[k,k]
        A[i,k+1:n] = A[i,k+1:n] - lam*A[k,k+1:n]
        b[i] = b[i] - lam*b[k]

    # back substitution
  b[n-1] = b[n-1] / A[n-1,n-1]
  for k in range(n-2, -1, -1):
    b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n])) / A[k,k]  
  
  return b # b -> x #np.ones(b.shape)


A = np.array([[1.0,2.0,5.0,3.0],
            [0.0,1.0,2.0,4.0],
            [2.0,3.0,5.0,3.0],
            [4.0,2.0,1.0,0.0]])
b = np.array([4.5,1.5,4.5,2])
print(solveLinearSystem(A, b))


#print(A[0,1])