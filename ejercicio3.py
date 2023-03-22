import numpy as np

def media_y_devstd(matriz):
    # calculo la media y la desviación estándar de cada columna ( axis=0 para que sea por columnas)
    media = np.mean(matriz, axis=0)
    devstd = np.std(matriz, axis=0)
    # operación se realiza elemento a elemento utilizando broadcasting de NumPy,
    # que ajusta automáticamente las dimensiones de los arrays para realizar operaciones de forma eficiente
    return (matriz - media) / devstd

MatA = np.array([[0, -4, 2],
              [-2, 0, 2],
              [4, 0, 5]])
print( 'Matriz original:\n', MatA)
print( 'Matriz transformada:\n', media_y_devstd(MatA))
