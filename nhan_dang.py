import cv2.face
import cv2
import numpy as np
import os
video = cv2.VideoCapture('http://192.168.1.216:8080/video')
r = cv2.face_LBPHFaceRecognizer.create()
r.read('hoc/hoc.yml')
d = ("haarcascade_frontalface_default.xml")
face = cv2.CascadeClassifier(d)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0;

ten = [0, "Nam", 2, 3, 4]
while True:
    ret, frame = video.read()
    img = cv2.flip(frame, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        id, do_chinh_xac = r.predict(gray[y:y + h, x:x + w])

        if (do_chinh_xac<100):
            id = ten[id]
        else:
            id = "chua_biet"

        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.imshow("nhan dien khuon mat", img)

        if cv2.waitKey(10) & 0xFF:
            KeyboardInterrupt

print("\n Thoát")
video.release()
cv2.destroyAllWindows()
