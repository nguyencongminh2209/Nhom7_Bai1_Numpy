import numpy as np

# Nhập kích thước của ma trận vuông từ người dùng
n = int(input("Enter the size of the square matrix: "))

# Nhập giá trị của ma trận từ người dùng
matrix_values = []
for i in range(n):
    row = [float(input(f"Enter value for row {i + 1}, column {j + 1}: ")) for j in range(n)]
    matrix_values.extend(row)

# Tạo ma trận ban đầu từ danh sách giá trị
matrix_A = np.array(matrix_values).reshape(n, n)

# Tính ma trận chuyển vị của ma trận A
matrix_A_transpose = matrix_A.T

# Hiển thị ma trận chuyển vị
print("Original Matrix (A):")
print(matrix_A)
print("Transpose of Matrix (A^T):")
print(matrix_A_transpose)
