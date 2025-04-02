import streamlit as st
st.title("News and Comments")
st.markdown("hello, this is markdown")
st.write("hello, this is write")
st.markdown("""
第一行文字（默认左对齐）  
<span style="text-align: center; display:block">第二行文字（居中）</span>  
第三行文字（默认左对齐）
""", unsafe_allow_html=True)
