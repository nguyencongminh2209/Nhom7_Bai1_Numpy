import cv2

video = cv2.VideoCapture('http://192.168.1.216:8080/video')

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n Nhập ID khuôn mặt <Enter> ==> ')
print("\n Hiển thị")

count = 0

while True:
    ret, frame = video.read()
    img = cv2.flip(frame, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        cv2.imwrite("du_lieu/User." + str(face_id) + "." + str(count) + ".jpg", gray[y:y + h, x:x + w])

    cv2.imshow("luu khuon mat", img)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
    elif count >= 30:
        break

print("\n Thoát")
video.release()
cv2.destroyAllWindows()