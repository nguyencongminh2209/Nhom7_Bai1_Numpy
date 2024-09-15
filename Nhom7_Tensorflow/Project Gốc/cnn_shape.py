import numpy as np
import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Tạo dữ liệu huấn luyện và tiền xử lý dữ liệu
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# Tải dữ liệu huấn luyện
training_set = train_datagen.flow_from_directory(
    'C:/Users/ADM/Desktop/Nhom7_Tensorflow/train1',
    target_size=(64, 64),
    batch_size=12,
    class_mode='sparse',  # Sử dụng 'sparse' cho việc nhận dạng đối tượng
    classes=['hinhchunhat', 'hinhtamgiac','hinhtron' ])

# Tải dữ liệu kiểm tra
test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
    'C:/Users/ADM/Desktop/Nhom7_Tensorflow/test1',
    target_size=(64, 64),
    batch_size=12,
    class_mode='sparse',  # Sử dụng 'sparse' cho việc nhận dạng đối tượng
    classes=['hinhchunhat', 'hinhtamgiac','hinhtron' ])

print("Image Processing.......Compleated")

# Xây dựng mạng nơ-ron
cnn = tf.keras.models.Sequential()
print("Building Neural Network.....")
cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=(64, 64, 3)))
cnn.add(MaxPooling2D(pool_size=2, strides=2))
cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(MaxPooling2D(pool_size=2, strides=2))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=64, activation='relu'))

# Lớp đầu ra cho nhận dạng đối tượng
# Đầu ra 4 giá trị cho mỗi đối tượng: x, y, chiều rộng, chiều cao
# Đầu ra 3 giá trị cho dự đoán lớp: hình tròn, hình chữ nhật, hình bình hành
cnn.add(Dense(units=12, activation='sigmoid'))  # Điều chỉnh số đơn vị theo cần thiết

# Biên dịch mô hình
cnn.compile(optimizer='adam', loss='mse', metrics=['accuracy'])  # Sử dụng 'mse' cho việc nhận dạng đối tượng

print("Training cnn")
cnn.fit(x=training_set, validation_data=test_set, epochs=5)
cnn.save("model.keras")
