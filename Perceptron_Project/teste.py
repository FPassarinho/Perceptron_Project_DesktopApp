import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import center_of_mass, shift

# Criar uma matriz 64x64 vazia (background preto)
matrix = np.zeros((64, 64))
print(matrix)

# Desenhar um "A" deslocado (simulação)
matrix[10, 30] = 1
matrix[11, 29] = 1
matrix[11, 31] = 1
matrix[12, 28] = 1
matrix[12, 32] = 1
matrix[13, 27] = 1
matrix[13, 33] = 1
matrix[14, 26] = 1
matrix[14, 34] = 1
matrix[15, 25:35] = 1  # Barra horizontal do "A"

# Encontrar centro de massa do "A"
cy, cx = center_of_mass(matrix)

# Definir centro ideal da matriz
target_cy, target_cx = 32, 32

# Calcular deslocamento necessário
shift_y = target_cy - cy
shift_x = target_cx - cx

# Aplicar translação
centered_matrix = shift(matrix, shift=[shift_y, shift_x], mode='constant', cval=0)

# Plotar antes e depois
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(matrix, cmap="gray")
axes[0].set_title("Antes (Deslocado)")

axes[1].imshow(centered_matrix, cmap="gray")
axes[1].set_title("Depois (Centralizado)")

plt.show()
