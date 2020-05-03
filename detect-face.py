import cv2

# load the classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# get capture from webcam(0)
cap = cv2.VideoCapture(0)

#infinite loop to get each frame of the video
# return two variables: _, img(frame itself)
while True:
    _, img = cap.read()


    # convert RBG image to cvt
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # take the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # draw rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()


