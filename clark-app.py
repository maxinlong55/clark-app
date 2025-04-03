import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

about_me=st.Page(page="views/about_me.py",
                title="About Me",
                icon=":material/home:",
                default=True)

chart=st.Page(page="views/chart.py",
                title="charts",
                icon=":material/account_circle:",
                )

test002=st.Page(page="views/test002.py",
                title="test002",
                icon=":material/account_circle:")
News_2025=st.Page(page="views/News_2025.py",
                title="News 2025 ",
                icon=":material/newspaper:")

pg=st.navigation(
    {
        "Info":[about_me],
        "Project":[chart,test002],
	"News":[News_2025]
    }
)
pg.run()

with st.sidebar:
	container = st.container(border=True)
	with container:
		st.write("AI Tool")
		st.markdown("China-[Deepseek](https://chat.deepseek.com/)|[Qwen](https://chat.qwen.ai/)")
		st.markdown("Global-[Chat GPT](https://chatgpt.com/)|[Grok](https://grok.com/?referrer=website)")

