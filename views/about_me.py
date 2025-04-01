import streamlit as st

col1,col2 = st.columns(2,gap="small",vertical_alignment="center")
with col1:
	st.image("./assets/profile_image.png",width=230)
with col2:
	st.title("Clark Ma",anchor=False)
	st.write("Hydraulic engineer")
	st.write("A little knowledge about Python")
