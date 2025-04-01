import streamlit as st
st.title("third")
if st.button("ballons"):
  st.balloons()

enable = st.checkbox("Enable Camera")
picture=st.camera_input("take a picture",disabled= not enable)
if picture:
	st.image(picture)
