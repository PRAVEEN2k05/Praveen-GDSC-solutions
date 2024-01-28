def sort_non_boundary(matrix):
    non_boundary_elements = []
    boundary_elements = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                boundary_elements.append(matrix[i][j])
            else:
                non_boundary_elements.append(matrix[i][j])

    sorted_non_boundary = sorted(non_boundary_elements)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                continue
            else:
                matrix[i][j] = sorted_non_boundary.pop(0)

    return matrix

MAX = 100
 
def printDiagonalSums(mat, n):
 
    principal = 0
    secondary = 0;
    for i in range(0, n): 
        for j in range(0, n): 
 
            # Condition for principal diagonal
            if (i == j):
                principal += mat[i][j]
 
            # Condition for secondary diagonal
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]
         
    return principal+secondary
 
order = int(input("Enter the order of the square matrix: "))
# Input matrix
matrix = []
print("Enter the elements of the matrix:")
for _ in range(order):
    row = list(map(int, input().split()))
    matrix.append(row)

sorted_matrix = sort_non_boundary(matrix)
diagonal_sum=printDiagonalSums(matrix, 4)

print("\nSorted Matrix with Non-Boundary Elements:")
for row in sorted_matrix:
    print(row)

print("\nSum of Diagonal Elements after Sorting:",diagonal_sum)
