import streamlit as st
import cv2

st.header("Capture Image from Webcam")

cap = cv2.VideoCapture(0)
capture = st.button("Capture Image")

frame_placeholder = st.empty()

captured = False
image = None

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if capture:
        image = frame
        captured = True
        st.image(image, caption="Captured Image")
        break

    if not captured:
        frame_placeholder.image(frame)

cap.release()
cv2.destroyAllWindows()