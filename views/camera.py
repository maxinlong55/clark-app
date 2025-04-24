import streamlit as st
import cv2
import numpy as np

st.title("Camera with OpenCV Processing")
enable = st.checkbox("Enable Camera")
picture = st.camera_input("Take a picture", disabled=not enable)



if st.button("ballons"):
  st.balloons()

st.divider()


