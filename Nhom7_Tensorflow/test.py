import numpy as np
from keras_preprocessing import image
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Canvas, Button, ttk
from keras.models import load_model
from PIL import Image,ImageTk
new_model=load_model('model.keras')
classes = ['Chuối', 'Dâu tây', 'Dứa', 'Khế', 'Măng cụt', 'Xoài']
def classify_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load and preprocess the selected image
        img = Image.open(file_path)
        img = img.convert('RGB')
        img = img.resize((64, 64))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # Predict the class of the image
        result = new_model.predict(img)
        result1 = result[0]
        for y in range(6):
            if result1[y] == 1.:
                break
        prediction = classes[y]
        
        # Display the prediction
        result_label.config(text=f'Đây là quả: {prediction}')

        # Display the selected image in a frame
        img = Image.open(file_path)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img
