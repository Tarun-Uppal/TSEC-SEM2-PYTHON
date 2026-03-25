import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(array_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(array_3d)

print("\n--- Reshaping ---")
reshaped_1d = array_1d.reshape(5, 1)
print("1D reshaped to 5x1:")
print(reshaped_1d)

reshaped_2d = array_2d.reshape(1, 9)
print("\n2D reshaped to 1x9:")
print(reshaped_2d)

print("\n--- Slicing ---")
print("1D array slice [1:4]:", array_1d[1:4])
print("2D array slice [0:2, 1:3]:")
print(array_2d[0:2, 1:3])
print("3D array slice [0, 1, :]:")
print(array_3d[0, 1, :])

print("\n--- Indexing ---")
print("1D array index [2]:", array_1d[2])
print("2D array index [1, 2]:", array_2d[1, 2])
print("3D array index [1, 0, 1]:", array_3d[1, 0, 1])

print("\n--- Dot Product ---")
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2)
print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Dot Product: {dot_product}")

print("\n--- Cross Product ---")
cross_product = np.cross(vector1, vector2)
print(f"Cross Product: {cross_product}")