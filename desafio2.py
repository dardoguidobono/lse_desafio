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


MatA = np.array([[0, -4, 2],
              [-2, 0, 2],
              [4, 0, 5]])

print('Norma l-0 de A:', calc_norma(MatA, 0))
print('Norma l-1 de A:', calc_norma(MatA, 1))
print('Norma l-2 de A:', calc_norma(MatA, 2))
print('Norma l-Inf de A:', calc_norma(MatA, np.inf))