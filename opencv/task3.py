import streamlit as st
import cv2

st.header("Detect eyes & face from Webcam")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
frame_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_roi = gray[y:y + h, x:x + w]
        color_face_roi = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(face_roi, scaleFactor=1.1, minNeighbors=10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(color_face_roi, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    #convert back from gray image to rgb image
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame)

cap.release()
cv2.destroyAllWindows()