import cv2
import numpy as np
import matplotlib.pyplot as plt

# Hàm để cập nhật và hiển thị ảnh sau khi zoom
def update_image():
    plt.clf()
    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i], cmap='gray')
    plt.show()

# Khởi tạo ảnh ban đầu và danh sách các phiên bản sau khi zoom
original_img = cv2.imread('a.png', cv2.IMREAD_GRAYSCALE)
half = cv2.resize(original_img, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(original_img, (1050, 1610))
stretch_near = cv2.resize(original_img, (780, 540), interpolation=cv2.INTER_LINEAR)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [original_img, half, bigger, stretch_near]
count = 4
current_scale = 1.0

# Hiển thị ban đầu
update_image()

# Lặp để cho phép người dùng thay đổi ảnh
while True:
    choice = input("Nhập '1' để Zoom In, '2' để Zoom Out, hoặc 'q' để thoát: ")
    if choice == '1':
        for i in range(count):
            images[i] = cv2.resize(images[i], (0, 0), fx=1.2, fy=1.2)
        current_scale *= 1.2
        update_image()
    elif choice == '2':
        for i in range(count):
            images[i] = cv2.resize(images[i], (0, 0), fx=1/1.2, fy=1/1.2)
        current_scale /= 1.2
        update_image()
    elif choice == 'q':
        break
