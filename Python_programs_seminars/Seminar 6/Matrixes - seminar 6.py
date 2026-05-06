import numpy as np

A = np.array([[1, 2, 3],[4, -1, 6],[7, 5, 9]])
B = np.array([[1, 1, 3],[4, 2, -3],[5, 8, 2]])

sum_matrix = A + B
sub_matrix = A - B
mult_matrix = A @ B

print(f"Sum of A and B: {sum_matrix}")
print(f"Subtraction of B from A: {sub_matrix}")
print(f"Multiplated A by B: {mult_matrix}")

with open("matrix_calc.bin", "wb") as f:
    np.save(f, f"{sum_matrix} {sub_matrix} {mult_matrix}")