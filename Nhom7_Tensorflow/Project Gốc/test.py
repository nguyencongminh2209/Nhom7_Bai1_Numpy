import os
import numpy as np
import tensorflow as tf
from keras.preprocessing import image

# Load mô hình đã huấn luyện
model = tf.keras.models.load_model('model.keras')

# Đường dẫn đến thư mục chứa hình ảnh bạn muốn phân loại
image_directory = 'C:/Users/ADM/Desktop/Nhom7_Tensorflow/shape'  # Thay đổi đường dẫn đến thư mục chứa hình ảnh

# Kích thước mục tiêu cho hình ảnh
target_size = (64, 64)

# Danh sách để lưu các kết quả phân loại
results = []

# Lặp qua tất cả các tệp tin hình ảnh trong thư mục
for filename in os.listdir(image_directory):
    if filename.endswith(".png"):  # Đảm bảo chỉ xử lý các tệp tin hình ảnh
        # Xây dựng đường dẫn đầy đủ đến tệp tin hình ảnh
        image_path = os.path.join(image_directory, filename)

        # Load hình ảnh và tiền xử lý nó
        img = image.load_img(image_path, target_size=target_size)
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img /= 255.

        # Dự đoán lớp của hình ảnh
        prediction = model.predict(img)

        # Xác định lớp dự đoán và thêm vào danh sách kết quả
        classes = ["hinhchunhat", "hinhtamgiac", "hinhtron"]  # Tên lớp tương ứng với mô hình của bạn
        predicted_class = classes[np.argmax(prediction)]
        results.append((filename, predicted_class))

# Hiển thị kết quả phân loại
for filename, predicted_class in results:
    print(f'Hình ảnh "{filename}" được dự đoán là: {predicted_class}'.encode('utf-8').decode('cp1252'))
