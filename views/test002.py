import streamlit as st
import cv2
st.title("third")
if st.button("ballons"):
  st.balloons()


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
