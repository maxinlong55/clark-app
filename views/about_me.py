import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
	contact_form()

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
	if st.button("✉Contact Me"):
		show_contact_form()

st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
	"""
	- 2 Years hydraulic system maintain experience in Iron and Steel plant
	- 7 Years tail-made pressure test equipment design 
	- 8 Years Paper machine hydraulic design """
)

st.write("\n")
st.subheader("Hard skill", anchor=False)
st.write(
	"""
	- Tools: Auto Cads, Invent, AmeSim
	- Design scope: hydraulic,Pneumatic,Lubrication
	- Scope:Fluid design | Workshop test | Commissioning """
)
