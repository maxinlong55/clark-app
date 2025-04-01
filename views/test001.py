import streamlit as st
import numpy as np
import pandas as pd

st.title("My test steamlit python App")

chart_data = pd.DataFrame(np.random.randn(15, 3), columns=["A", "B", "C"])

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
	["line_chart", "Area Chart", "bar_chart", "scatter_chart", "data_frame", "code"])
tab1.line_chart(chart_data["A"], x_label="This is x-axis", y_label="This is Y axis", use_container_width=True,
                color=(0, 255, 0))
tab1.line_chart(chart_data, x="A", y="B", x_label="This is x-axis", y_label="This is Y axis", use_container_width=True,
                color=(0, 255, 255))
tab1.line_chart(chart_data, x_label="This is x-axis", y_label="This is Y axis", use_container_width=True,
                color=[(255, 255, 0), (0, 255, 0), (0, 0, 255)])
tab2.subheader("Area Chart")
tab2.area_chart(chart_data)

tab3.bar_chart(chart_data)
tab3.bar_chart(chart_data["B"])

tab4.subheader("scatter")
tab4.scatter_chart(chart_data)

tab5.write(chart_data)

example = """def hello():
	print('hello')
	print("ok")"""
tab6.code(example)
