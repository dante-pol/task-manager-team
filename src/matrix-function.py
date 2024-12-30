def sum_matrix(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    matrix3 = []
    if len(matrix1) != len(matrix2):
        return None
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            return None
    for i in range(len(matrix1)):
        matrix3.append([])
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix3[i].append(matrix1[i][j] + matrix2[i][j])
    return matrix3

def diff_matrix(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    matrix3 = []
    if len(matrix1) != len(matrix2):
        return None
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            return None
    for i in range(len(matrix1)):
        matrix3.append([])
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix3[i].append(matrix1[i][j] - matrix2[i][j])
    return matrix3