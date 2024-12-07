import numpy as np
         
# Find rank of a matrix
'''
def rowrank(matrix):
    rank = np.prod(matrix[0].shape) # self.C = len(Matrix[0])
    num_row = np.prod(matrix[:,0].shape) # self.R = len(matrix)
    for row in range(0, rank):
        # Before we visit current row 'row', 
        # make sure that mat[row,0],..,mat[row,row-1] = 0
     
        # Diagonal element is not zero
        if matrix[row,row] != 0:
            for col in range(0, num_row):
                if col != row:
                    # This makes all entries of current
                    # column as 0 except entry 'mat[row][row]'
                    lam = matrix[col,row] / matrix[row,row]
                    for i in range(rank):
                        matrix[col,i] -= lam * matrix[row,i]
                                                 
        # Diagonal element is already zero.
        # Two cases arise:
        # 1) If there is a row below it with non-zero entry, swap
        # this row with that row and process that row
        # 2) If all elements in current column below mat[r][row] are 0,
        # then remove this column by
        # swapping it with last column and
        # reducing number of columns by 1.
        else:
            reduce = True
                 
            # Find the non-zero element in current column
            for i in range(row+1, num_row):
                # Swap the row with non-zero element with this row.
                if matrix[i,row] != 0: # a[[x, y]] = a[[y, x]]
                    matrix[[row,i]] = matrix[[i,row]]
                    reduce = False
                    break
                         
            # If we did not find any row with
            # non-zero element in current
            # columnm, then all values in
            # this column are 0.
            if reduce:
                # Reduce number of columns
                rank -= 1
                
                # copy the last column here
                for i in range(0, num_row, 1):
                    matrix[i,row] = matrix[i,rank]
                         
                # process this row again
            row -= 1
                 
    # self.Display(Matrix, self.R,self.C)
    return rank
'''


def rowrank(matrix):
  rank = np.prod(matrix[0].shape)
  num_row = np.prod(matrix[:,0].shape)

  # Find the # of linearly independent rows
  for r in range(0, rank):
    # Check whether the diagonal element is non-zero
    if matrix[r,r] != 0:
    # below a pivot, mat[row,0],..,mat[row,row-1] = 0
      for c in range(0, num_row):
        if c != r:
          lam = matrix[c,r] / matrix[r,r]
          for i in range(rank):
            matrix[c,i] -= lam * matrix[r,i]
                                                 
    # If diagonal element is zero
    # 2) If all elements below the pivot in the pivot column are 0,
    # remove this column by swapping it with the last column &
    # reducing # of columns by 1.
    else:
      row_reduction = True

      for j in range(r+1, num_row):
        # 1) If there is a row with non-zero entry in the pivot column,
        if matrix[j,r] != 0:
          # Swap the row with non-zero element with this row.
          matrix[[r,j]] = matrix[[j,r]]
          row_reduction = False
          break

        # 2) If not (i.e. all elements below the pivot in the column are 0)
        if row_reduction:
          # Reduce number of columns
          rank -= 1
          # copy the last column
          for k in range(0, num_row, 1):
            matrix[k,r] = matrix[k,rank]
        # repeat the process for other rows
        r -= 1

  return rank


my_matrix = np.array([[1, 2, 1], [3, 4, 7], [3, 6, 3]])
#mat2 = np.array([[10, 20, 10], [-20, -30, 10], [30, 50, 0]])
print(rowrank(my_matrix)) # 오류 발견!
print(np.linalg.matrix_rank(my_matrix))
#print(rowrank(mat2))
#print(np.linalg.matrix_rank(mat2))