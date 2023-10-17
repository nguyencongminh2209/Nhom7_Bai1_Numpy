import cv2

import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('ic_check.png',cv2.IMREAD_GRAYSCALE)

half = cv2.resize(img,(0,0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(img,(1050,1610))
stretch_near = cv2.resize(img,(780,540),interposition = cv2.INTER_LINEAR)
Titles = ["Original","Half","Bigger","Interposition Nearest"]
images = [img,half,bigger,stretch_near]
count = 4
for i in range(count):
    plt.subplot(2,2,i+1)
    plt.title(Titles[1])
    plt.imshow(images[i])

plt.show()