import streamlit as st

col1,col2,col3 = st.columns(3,gap="small",vertical_alignment="center")
with col2:
	st.markdown("News and Comments")

st.subheader("<h2 style='text-align: center;'>News and Comments</h2>")

st.markdown("""News and Comments""",unsafe_allow_html=True)
st.markdown("mark_donw")
st.title("title")
st.header("header")
st.subheader("subheader")

