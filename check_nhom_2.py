import numpy as np

matrix = [int(input("Enter value: ")) for _ in range(9)]
newarr = np.array(matrix).reshape(3, 3)
x = newarr.T  # Ma trận chuyển vị

print("Matrix you entered:")
print("---------------------------------------")
print(newarr)
print("---------------------------------------")

print("Transposed matrix:")
print("---------------------------------------")
print(x)
print("---------------------------------------")
# tối ưu code nhóm 2
# sự khác biệt xuất hiện khi giá trị tạo mảng lớn dần
#trong giá trị lớn hơn 10000
#code nhóm 2 thực hiện trong 0.04700803756713867 seconds
# code tối ưu chạy trong 0.010142326354980469 seconds
