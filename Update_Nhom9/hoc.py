import cv2.face
import numpy as np
from PIL import Image
import os

p = 'du_lieu'

r = cv2.face_LBPHFaceRecognizer.create()
d = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def timvahoc(p):
    i = [os.path.join(p, f) for f in os.listdir(p)]
    f = []
    ids = []

    for k in i:
        P = Image.open(k).convert('L')
        n = np.array(P, 'uint8')

        id = int(os.path.split(k)[-1].split(".")[1])
        faces = d.detectMultiScale(n)

        for (x, y, w, h) in faces:
            f.append(n[y:y+h, x:x+w])
            ids.append(id)

    return f, ids

print("\n Học dữ liệu...")
faces, ids = timvahoc(p)
r.train(faces, np.array(ids))

r.save('hoc/hoc.yml')

print("\n {0} khuôn mặt được tìm thấy. Thoát.".format(np.unique(ids)))