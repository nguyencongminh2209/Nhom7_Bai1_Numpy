import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm để cập nhật và hiển thị ảnh sau khi zoom
def update_image():
    scaled_img = cv2.resize(original_img, None, fx=current_scale, fy=current_scale, interpolation=cv2.INTER_LINEAR)
    img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# Hàm xử lý sự kiện khi nút "Zoom In" được nhấn
def zoom_in():
    global current_scale
    current_scale *= 1.2
    update_image()

# Hàm xử lý sự kiện khi nút "Zoom Out" được nhấn
def zoom_out():
    global current_scale
    current_scale /= 1.2
    update_image()

# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def select_image():
    global original_img, current_scale
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        current_scale = 1.0
        update_image()

# Tạo cửa sổ
window = tk.Tk()
window.title("Zoom In/Out Image")

# Khai báo biến toàn cục
current_scale = 1.0
original_img = None

# Tạo nút "Chọn ảnh" và đặt sự kiện khi nút này được nhấn
select_button = tk.Button(window, text="Chọn ảnh", command=select_image)
select_button.pack()

# Tạo nút "Zoom In" và đặt sự kiện khi nút này được nhấn
zoom_in_button = tk.Button(window, text="Zoom In", command=zoom_in)
zoom_in_button.pack()

# Tạo nút "Zoom Out" và đặt sự kiện khi nút này được nhấn
zoom_out_button = tk.Button(window, text="Zoom Out", command=zoom_out)
zoom_out_button.pack()

# Tạo label để hiển thị ảnh
img_label = tk.Label(window)
img_label.pack()

window.mainloop()
