import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
import cv2 as cv

st.title("Camera with OpenCV Processing")
enable = st.checkbox("Enable Camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    bytes_data = picture.getvalue()
    cv_image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    processed_image = cv_image.copy()
    hsv_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2HSV)
    col1, col2 = st.columns(2)
    with col1:
        st.image(cv_image, channels="BGR", caption="Original Image")
    with col2:
        st.image(hsv_image, channels="HSV", caption="Processed Image (HSV)")

if st.button("ballons"):
  st.balloons()

st.divider()

st.title("real-time hand detection with mediapipe")

mp_hand = mp.solutions.hands
hands = mp_hand.Hands(static_image_mode=False,max_num_hands=2)

mp_drawing = mp.solutions.drawing_utils
enable = st.checkbox("Start")

cap = cv.VideoCapture(0)
frame_placeholder =st.empty()


while cap.isOpened() and enable:
    ret,frame = cap.read()
    if not ret:
        st.erro("Failed to capture frame.")
        break
    rgb_frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hand.HAND_CONNECTIONS)
    frame_placeholder.image(frame,channels="BGR")
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
hands.close()
