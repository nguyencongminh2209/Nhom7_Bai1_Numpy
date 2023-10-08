import numpy as np
from keras_preprocessing import image
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Canvas, Button, ttk
from keras.models import load_model
from PIL import Image,ImageTk
new_model=load_model('model.keras')
classes = ['Chuối', 'Dâu tây', 'Dứa', 'Khế', 'Măng cụt', 'Xoài']
