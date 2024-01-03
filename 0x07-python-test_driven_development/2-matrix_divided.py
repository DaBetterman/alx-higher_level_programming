#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
        
    new_list=[]
    count = len(matrix)

    for i in range(count):
        for j in range(3):
            result = (matrix[i][j] / div)
            new_result = '%.2f' % result
            new_list.append(new_result)
    return (new_list)


'''
def matrix_divided(matrix, div):
    # Validate matrix
    for row in matrix:
        if not isinstance(row, list) or len(row) != len(matrix[0]):
            raise TypeError("matrix must be a matrix (list of lists) with the same size in each row")
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = matrix_divided(matrix, 3)
print(result)

'''