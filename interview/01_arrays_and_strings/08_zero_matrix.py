# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def set_zeros_optimized(matrix):
    rowHasZeros = False
    colHasZeros = False

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            rowHasZeros = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            colHasZeros = True
            break
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)
    
    if rowHasZeros:
        nullify_row(matrix, 0)
    
    if colHasZeros:
        nullify_column(matrix, 0)

def set_zeros(matrix):
    row = [False for _ in range(len(matrix))]
    columns = [False for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                columns[j] = True

    for i in range(len(row)):
        if row[i]:
            nullify_row(map, i)
    
    for j in range(len(columns)):
        if columns[j]:
            nullify_column(matrix, j)

def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullify_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0