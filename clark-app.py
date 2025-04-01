import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

about_me=st.Page(page="views/about_me.py",
                title="About Me",
                icon=":material/:home",
                default=True)

test001=st.Page(page="views/test001.py",
                title="test001",
                icon=":material/account_circle:",
                )

test002=st.Page(page="views/test002.py",
                title="test002",
                icon=":material/account_circle:")

#pg = st.navigation(pages=[test001,test002])
pg = st.navigation({
	"Info":[about_me],
	"Project":[test001,test002],
})
pg.run()


with st.sidebar:
	st.markdown("This is a side Bar")
	container = st.container(border=True)
	with container:
		st.write("AI Tool")
		st.markdown("China-[Deepseek](https://chat.deepseek.com/)|[Qwen](https://chat.qwen.ai/)")
		st.markdown("Global-[Chat GPT](https://chatgpt.com/)|[Grok](https://grok.com/?referrer=website)")
