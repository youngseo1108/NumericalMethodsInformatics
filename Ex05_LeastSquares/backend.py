import numpy as np

# Task a)
# Implement a method performing least squares approximation of a linear courve.
# Input: Vectors x,y. Both 1D np.array of same size.
# Output: list of factors [m, b] representing the linear courve f(x) = mx + b.
def linearLSQ(x: np.array, y: np.array) -> list:
  # assemble matrix X
  X = np.vstack([x, np.ones(len(x))]).T
  # turn y into a column vector
  y = y[:, np.newaxis]
  # Direct least square regression
  m, b = (np.linalg.inv(X.T @ X) @ (X.T @ y)).T[0]
  return [m, b]


# Task b)
# Implement a method, orthogornalizing the given basis.
# Input: sourceBase - list of vectors, as in a)
# Output: orthoronalizedBase - list of vectors, with same size and shape as sourceBase
def orthonormalize(sourceBase: list) -> list:
  X = np.stack(sourceBase)
  n, p = X.shape
  U = np.zeros((n, p))
  I = np.eye(n)

  v1 = X[:,0]
  U[:, 0] = v1 / np.sqrt(np.dot(v1, v1))

  for i in range(1, p):
    v_p = X[:, i]
    W = X[:, 0:i]

    M = I - W @ np.linalg.inv(W.T @ W) @ W.T
    u = M @ v_p

    U[:, i] = u / np.sqrt(np.dot(u,u))

  return list(U)