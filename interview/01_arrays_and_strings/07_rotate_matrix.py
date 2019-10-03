# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(layer, last):
            offset = 1 - first

            top = matrix[first][i]
            matrix[first][i] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            
    return True
