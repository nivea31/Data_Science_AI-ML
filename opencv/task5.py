import streamlit as st
import cv2
import os
from PIL import Image

st.header("Face & Eye Detection with Save Option")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

cap = cv2.VideoCapture(0)
frame_placeholder = st.empty()
cropped_face_placeholder = st.empty()
detection_image_placeholder = st.empty()

# Variables to store images
captured_face = None
original_image = None
detection_image = None

# Prevent Crash If Camera Doesn't Open
if not cap.isOpened():
    st.error("No Camera Found!")
    cap.release()

# Capture and Process Frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.warning("No frame received.")
        continue

    # Store original image
    original_image = frame.copy()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)

    # Draw rectangle around face and detect eyes
    for (x, y, w, h) in faces:
        # Capture the first face only once
        if captured_face is None:
            captured_face = frame[y:y+h, x:x+w]

        # Draw a blue rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Detect eyes inside the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # Convert images to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Display Original Image
    frame_placeholder.image(original_image, channels="RGB", caption="📸 Original Image")

    # Display Cropped Face
    if captured_face is not None:
        cropped_face_rgb = cv2.cvtColor(captured_face, cv2.COLOR_BGR2RGB)
        cropped_face_placeholder.image(cropped_face_rgb, caption="🧑‍🤝‍🧑 Cropped Face")

    # Display Detection Image
    detection_image = frame
    detection_image_placeholder.image(detection_image, caption="👀 Face & Eye Detection Image")

    # Stop capturing once face is detected
    cap.release()

# ✅ SAVE IMAGES TO FOLDER
if captured_face is not None:
    # Save original image
    original_image_path = "captured_images/original_image.jpg"
    Image.fromarray(original_image).save(original_image_path)

    # Save cropped face
    cropped_face_path = "captured_images/cropped_face.jpg"
    Image.fromarray(cropped_face_rgb).save(cropped_face_path)

    # Save face-eye detection image
    detection_image_path = "captured_images/detection_image.jpg"
    Image.fromarray(detection_image).save(detection_image_path)

    # ✅ Provide Download Buttons
    st.subheader("✅ Download Your Images")
    with open(original_image_path, "rb") as file:
        st.download_button("📥 Download Original Image", file, file_name="original_image.jpg")

    with open(cropped_face_path, "rb") as file:
        st.download_button("📥 Download Cropped Face", file, file_name="cropped_face.jpg")

    with open(detection_image_path, "rb") as file:
        st.download_button("📥 Download Detection Image", file, file_name="detection_image.jpg")
if st.button("Capture New Face"):
    st.experimental_rerun()
