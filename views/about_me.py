import streamlit as st

col1,col2 = st.columns(2,gap="small",vertical_alignment="center")
with col1:
	st.image("./assets/profile_image.png",width=230)
with col2:
	st.title("Clark Ma",anchor=False)
	st.write(
		"""
		- Hydraulic engineer.
		- A little knowledge about Python
		"""
	)

st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
	"""
	- 2 Years maintain experience of hydraulic system
	- 7 Years tail-made pressure test equipment design
	- 8 Years Paper machine hydraulic design """
)

st.write("\n")
st.subheader("Hard skill", anchor=False)
st.write(
	"""
	- Tools: Auto Cads, Invent, AmeSim
	- Design scope: hydraulic,Pneumatic,Lubrication
	- Scope:Fluid design \ Workshop test \ Commissioning """
)
