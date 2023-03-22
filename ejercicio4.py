import numpy as np


MatA = np.array([[0, -4, 2],
              [-2, 0, 2],
              [4, 0, 5]])


print("Matriz:\n", MatA)
print("Inversa:\n", np.linalg.inv(MatA))
print("Determinante:", np.linalg.det(MatA))
print("Traza:", np.trace(MatA))
autovalores, autovectores = np.linalg.eig(MatA)
print("Autovalores:", autovalores)
print("Autovectores:\n", autovectores)