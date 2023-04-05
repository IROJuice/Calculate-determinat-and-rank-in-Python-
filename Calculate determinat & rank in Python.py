

import numpy as np

def cofactor_determinant(A):
    n = len(A)

    if n == 1:
        determinant = A[0][0]
        rankA = 1
        return determinant, rankA

    determinant = 0
    for j in range(n):
        # Calculate the cofactor of A[0][j]
        sign = (-1)**j
        submatrix = [[A[i][k] for k in range(n) if k != j] for i in range(1, n)]
        cofactor = sign * cofactor_determinant(submatrix)[0]

        # Add the contribution of this cofactor to the determinant
        determinant += A[0][j] * cofactor

    # Calculate the rank of the matrix
    rankA = np.linalg.matrix_rank(A)

    return determinant, rankA

# Prompt user to enter elements of the matrix
n = int(input('Enter the dimension of the matrix: '))
print('Enter the elements of the matrix:')
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input(f'A({i+1},{j+1}) = ')))
    A.append(row)

# Calculate the determinant and rank of the matrix using the cofactor method
determinant, rankA = cofactor_determinant(A)

# Display the results
print('The determinant of the matrix is:')
print(determinant)
print('The rank of the matrix is:')
print(rankA)
