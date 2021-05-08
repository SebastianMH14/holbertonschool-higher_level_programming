#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = []
    for i in matrix[:]:
        mtx.append(list(map(lambda k: k ** 2, i)))
    return mtx
