import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askinteger

start_x, start_y, end_x, end_y = -1, -1, -1, -1
is_drawing = False
selected_region = None
smoothing_value = 5


def select_region(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, is_drawing, img, selected_region

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            end_x, end_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        end_x, end_y = x, y

        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

        selected_region = img[start_y:end_y, start_x:end_x]
