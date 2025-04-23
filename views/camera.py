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

import cv2
import mediapipe as mp
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

# 初始化 MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)
mp_drawing = mp.solutions.drawing_utils

# Streamlit 页面设置
st.title("🖐️ 实时手势识别 (MediaPipe + Streamlit)")
st.markdown("使用 MediaPipe 检测手部关键点，并通过 Streamlit 实时显示")

# 使用 webrtc-streamer 获取摄像头流
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # 转换为 RGB（MediaPipe 需要 RGB 格式）
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 手势检测
    results = hands.process(img_rgb)

    # 绘制关键点
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2),
            )

    return av.VideoFrame.from_ndarray(img, format="bgr24")

# 启动 WebRTC 摄像头流
webrtc_ctx = webrtc_streamer(
    key="example",
    video_frame_callback=video_frame_callback,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

# 如果没有摄像头，显示提示
if not webrtc_ctx.state.playing:
    st.warning("请允许访问摄像头以启动手势识别")
