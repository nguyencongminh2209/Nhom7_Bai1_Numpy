import tkinter as tk
from tkinter import Text, Button, Label, Scrollbar
import pandas as pd
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
in_data = None  # Khởi tạo biến in_data ở mức biến toàn cục
# Hàm tính toán thống kê
def calculate_statistics():
    global in_data
    df = pd.read_csv('diemPython.csv', index_col=0, header=0)
    in_data = array(df.iloc[:, :])

    result = "Tong so sinh vien tham gia mon hoc: {}\n".format(np.sum(in_data[:, 1]))
    result += 'Tong sinh vien dat diem A: {}\n'.format(np.sum(in_data[:, 3]))
    result += 'Tong sinh vien dat diem B+: {}\n'.format(np.sum(in_data[:, 4]))
    result += 'Tong sinh vien dat diem B: {}\n'.format(np.sum(in_data[:, 5]))
    result += 'Tong sinh vien dat diem C+: {}\n'.format(np.sum(in_data[:, 6]))
    result += 'Tong sinh vien dat diem C: {}\n'.format(np.sum(in_data[:, 7]))
    result += 'Tong sinh vien dat diem D+: {}\n'.format(np.sum(in_data[:, 8]))
    result += 'Tong sinh vien dat diem D: {}\n'.format(np.sum(in_data[:, 9]))
    result += 'Tong sinh vien dat diem F: {}\n'.format(np.sum(in_data[:, 10]))

    maxx = 0
    minn = 9999999
    lopp = lopmin = 0
    for i in range(0, 9):
        sum1 = 0
        for j in range(3, 10):
            sum1 += np.sum(in_data[i, j])
        if sum1 >= maxx:
            maxx = sum1
            lopp = in_data[i, 0]
        if sum1 <= minn:
            minn = sum1
            lopmin = in_data[i, 0]
        result += "Lop {}: {}\n".format(in_data[i, 0], sum1)

    result += "Lop {} co nhieu sinh vien duoc diem >= D nhieu nhat voi {} sinh vien\n".format(lopp, maxx)
    result += "Lop {} co it sinh vien duoc diem >= D nhieu nhat voi {} sinh vien\n".format(lopmin, minn)

    diemL1 = np.sum(in_data[:, 11])
    diemL2 = np.sum(in_data[:, 12])

    if diemL1 > diemL2:
        result += "Co nhieu sinh vien qua L1 hon L2\n"
    elif diemL1 < diemL2:
        result += "Co nhieu sinh vien qua L2 hon L1\n"
    else:
        result += "So sinh vien qua L1 va L2 la nhu nhau\n"

    display_result(result)

# Hàm hiển thị kết quả trong vùng văn bản
def display_result(result):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Hàm hiển thị biểu đồ
def display_graphs():
    global in_data
    diemA = in_data[:, 3]
    diemBc = in_data[:, 4]
    diemB = in_data[:, 5]
    diemCc = in_data[:, 6]
    diemC = in_data[:, 7]
    diemDc = in_data[:, 8]
    diemD = in_data[:, 9]
    diemF = in_data[:, 10]

    # Đoạn code để hiển thị biểu đồ ở đây
    # Đây là ví dụ, bạn có thể sửa đổi để hiển thị biểu đồ phù hợp với dữ liệu của bạn.
    plt.plot(range(len(diemA)), diemA, 'r-', label="Diem A")
    plt.xlabel('Lơp')
    plt.ylabel('So sv dat diem')
    plt.legend(loc='upper right')
    plt.show()

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Thống kê và Biểu đồ")

# Tạo nút bấm để tính toán thống kê
calculate_button = Button(root, text="Tính toán thống kê", command=calculate_statistics)
calculate_button.pack()

# Tạo nút bấm để hiển thị biểu đồ
graph_button = Button(root, text="Hiển thị biểu đồ", command=display_graphs)
graph_button.pack()

# Tạo vùng hiển thị kết quả
result_text = Text(root, height=10, width=50)
result_text.pack()

# Tạo thanh cuộn cho vùng hiển thị kết quả
scrollbar = Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

# Khởi đầu chương trình
root.mainloop()
