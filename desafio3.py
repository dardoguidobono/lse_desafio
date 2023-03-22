import numpy as np

def calc_norma(matrix, n):
    # norma l0 (suma la cantidad de elementos no nulos)
    if n == 0:
        return np.sum(matrix != 0, axis=1)
    # norma l-infinity (valor máximo absoluto)
    elif n == np.inf:
        return np.max(np.abs(matrix), axis=1)
    # l-n generalizada 
    else:
        return np.sum(np.abs(matrix) ** n, axis=1) ** (1/n)

def ordenar_x_norma2(matrix):
    norms = calc_norma(matrix, 2)
    # ordeno los índices de mayor a menor norma [::-1] invierte el orden
    indices = np.argsort(norms)[::-1]
    # retorno filas de la matriz original en el orden de indices calculado previamente
    return matrix[indices]

MatA = np.array([[0, -4, 2],
              [-2, 0, 2],
              [4, 0, 5]])

print( 'Matriz original:\n', MatA)
print( 'Norma l-2:\n', calc_norma(MatA, 2))
print( 'Matriz ordenada:\n', ordenar_x_norma2(MatA))
