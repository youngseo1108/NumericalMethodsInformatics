import backend, frontend
import numpy as np

# Maybe change this to a propper matrix, which you can calculate by hand as well.
A = np.random.random((10, 10))
A += np.identity(10)


# These are the methods you are supposed to implement in backend.py
P, L, U = backend.lu(A)
det = backend.determinant(A)

frontend.displayLU(A, P, L, U)

# Sorry, there is no nice way to visualize a determinant.
print("Your determinant:", det)
print("Reference: ", np.linalg.det(A))