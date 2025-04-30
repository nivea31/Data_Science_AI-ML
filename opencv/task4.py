import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

st.header("Face & Eye Detection")

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    cap.release()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    st.subheader("Original Image")
    st.image(frame, channels="BGR")

    st.subheader("Cropped Faces")
    for i, (x, y, w, h) in enumerate(faces):
        face_crop = frame[y:y + h, x:x + w]
        st.image(face_crop, channels="BGR", caption=f"Face {i + 1}")

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    st.subheader("Eye Detection Image")
    st.image(frame, channels="BGR")
else:
    st.error("Failed to capture image")
cap.release()
cv2.destroyAllWindows()