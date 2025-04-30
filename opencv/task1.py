import streamlit as st
import cv2

#1. Webcam Integration

st.header("Live Webcam Feed on Streamlit")
st.text("Press 'Start' to start webcam.")

start = st.button("Start")
stop = st.button("Stop")

frame_placeholder = st.empty()
if start:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not access the webcam.")
    else:
        st.text("Webcam started. Press 'Stop Webcam' to exit.")

        while not stop:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture video")
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame_placeholder.image(frame, channels="RGB")

        cap.release()
        cv2.destroyAllWindows()

elif stop:
    st.success("Webcam feed stopped.")

