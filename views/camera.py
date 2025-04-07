import streamlit as st
import cv2
import numpy as np
import mediapipe as mp

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

import streamlit as st
import cv2
import numpy as np
import mediapipe as mp

st.title("Hand Detection with MediaPipe")

# 初始化 MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 通过浏览器拍照
picture = st.camera_input("Take a picture for hand detection")
if picture:
    # 将图片转为 OpenCV 格式
    bytes_data = picture.getvalue()
    frame = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # 手势识别
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2) as hands:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, landmarks, mp_hands.HAND_CONNECTIONS)
    
    # 显示结果
    st.image(frame, channels="BGR", caption="Processed Image")
