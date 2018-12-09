def null_checker(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        sum = 0
        current = []
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
            current.append(matrix[i][j])
        if sum != 0:
            new_matrix.append(current)
    return new_matrix


def transpose(matrix):
    new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def mult_by_number(matrix, num):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * num
    return matrix


def mult_by_matrix(matrix1, matrix2):
    new_matrix = [[0 for j in range(len(matrix2[i]))] for i in range(len(matrix1))]

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
                for k in range(len(matrix1[0])):
                    new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return new_matrix


def matrix_sum(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix1

def matrix_deff(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix1[i][j] = matrix1[i][j] - matrix2[i][j]
    return matrix1

def matrix_pow(matrix, n):
    for i in range(n-1):
        matrix = mult_by_matrix(matrix, matrix)
    return matrix


def to_triangle(matrix, arg):
    k = 0

    for j in range(len(matrix[0])):
        t = matrix[k][j]
        if t == 0:
            break
        for i in range(len(matrix)):
            x = matrix[i][j] / t
            if i > k:
                for n in range(len(matrix[0])):
                    matrix[i][n] = matrix[i][n] - matrix[k][n] * x
                    if matrix[i][n]-int(matrix[i][n]) < 0.00001:
                        matrix[i][n] = int(matrix[i][n])
        k += 1

    matrix = null_checker(matrix)

    if arg == 0:
        return matrix
    else:
        return transpose(matrix)


def determinant(matrix):
    matrix = to_triangle(matrix, 0)
    det = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                det *= matrix[i][j]
                break
    return det


def to_diagonal(matrix):
    return to_triangle(to_triangle(matrix, 1), 0)


def get_rank(matrix):
    matrix = to_triangle(matrix, 0)
    return len(matrix)


def inverse(matrix):
    if determinant(matrix) != 0:
        x = 1/determinant(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = x * matrix[i][j]
                return null_checker(matrix)
    else:
        return "Определитель равен нулю!"





