import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

st.header("")

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if st.button("Capture"):
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        st.image(frame, channels="BGR")

        for i, (x, y, w, h) in enumerate(faces):
            face_crop = frame[y:y + h, x:x + w]
            st.image(face_crop, channels="BGR", caption=f"Face {i + 1}")
            st.write(f"Total number of faces in above captured image are - {i+1} ")
            break
        else:
            st.write("Sorry,No face Detected!")
    else:
        st.error("Failed to capture image")
cap.release()
cv2.destroyAllWindows()