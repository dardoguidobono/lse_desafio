import numpy as np
# puntos
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# centroides
C = np.array([[1, 0, 0],
              [0, 1, 1]
              ])

def distancia_euclidiana(puntos, centroides):
    # agrego una dimension a los puntos para poder restarlos con los centroides
    # puntos[:, np.newaxis, :] -> agrego una dimension a los puntos
    return np.sqrt(np.sum((puntos[:, np.newaxis, :] - centroides)**2, axis=2))

distancias = distancia_euclidiana(X, C)
print(distancias)