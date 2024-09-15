import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
#Đường dẫn này máy tính cá nhân down file hình ảnh ở đâu thì cop đường dẫn thay thế ở đó
training_set = train_datagen.flow_from_directory('C:/Users/ADM/Desktop/TKPMDTMNM/Nhom7/demo/train1',
                                                 target_size = (64, 64),
                                                 batch_size = 12,
                                                 class_mode = 'categorical')
test_datagen = ImageDataGenerator(rescale = 1./255)
#Đường dẫn này máy tính cá nhân down file hình ảnh ở đâu thì cop đường dẫn thay thế ở đó
test_set = test_datagen.flow_from_directory('C:/Users/ADM/Desktop/TKPMDTMNM/Nhom7/demo/test1',
                                            target_size = (64, 64),
                                            batch_size = 12,
                                            class_mode = 'categorical')
classes = ['Chuối','Dâu tây','Dứa','Khế','Măng cụt','Xoài']
print("Image Processing.......Compleated")
cnn = tf.keras.models.Sequential()
print("Building Neural Network.....")
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(units=32, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=64, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=256, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=256, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=6, activation='softmax'))
cnn.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
print("Training cnn")
cnn.fit(x = training_set, validation_data = test_set, epochs = 10)
cnn.save("model.keras")
