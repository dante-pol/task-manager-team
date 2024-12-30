def sum_matrix(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    '''

    :param matrix1:матрица которая хранит в себе целые числа
    :param matrix2:матрица которая хранит в себе целые числа
    :return: должна возвращать матрицу с суммой каждых i-ых элементов 2 матриц
    '''
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
    '''

    :param matrix1:матрица которая хранит в себе целые числа
    :param matrix2:матрица которая хранит в себе целые числа
    :return: должна возвращать матрицу с разностью каждых i-ых элементов 2 матриц
    '''
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

def prod_matrix(matrix1: list[list[int]], number: int) -> list[list[int]]:
    '''

    :param matrix1:матрица которая хранит в себе целые числа
    :param number:целое число
    :return:должна возвращать матрицу в которой кождый элемент перемножен на number
    '''
    matrix3 = []
    for i in range(len(matrix1)):
        matrix3.append([])
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix3[i].append(matrix1[i][j] * number)
    return matrix3