import streamlit as st
import numpy as np
import pandas as pd

st.title("All kinds of Chart")

df= pd.read_csv("assets/diabetes.csv")
df=df.head(30)
tab1,tab2,tab3,tab4,tab5,tab6,=st.tabs(["line chart","line chart_x_y","line_in_one","chart area","bar chart","scatter chart"])
tab1.line_chart(df["Glucose"],x_label="No meaning1",y_label="value1",color=(0,255,0),use_container_width=True) #default x is int (0,11)
tab2.line_chart(df,x="Age",y="Glucose",x_label="No meaning2",y_label="value2",color=(255,255,0),use_container_width=False)
tab3.line_chart(df,x_label="No meaning 3",y_label="valve3",use_container_width=True) # if we defin color, color should be a list
tab4.area_chart(df,x_label="No meaning 4",y_label="valve4")
tab5.bar_chart(df,x_label="No meaning 5",y_label="valve5")
tab5.bar_chart(df["Glucose"],x_label="No meaning 5",y_label="valve5")
tab6.scatter_chart(df,size=30,x_label="No meaning 6",y_label="valve6")

st.divider()
st.markdown("Matplotlib")


fig,ax = plt.subplots(3,2,figsize=(10,15))
# plt.xkcd()
# plt.style.use("fivethirtyeight")
ax[0,0].scatter(range(len(df["Glucose"])),df["Glucose"],color='red')
ax[0,0].set_title("mapltolib title")
ax[0,0].set_xlabel("Number")
ax[0,0].set_ylabel("value")


ax[0,1].plot(range(len(df["Glucose"])),df["Glucose"],color='green',label="Glucose")
ax[0, 1].legend(loc="upper right")
ax[0, 1].set_title("Glucose Trend")
ax[0, 1].set_xlabel("Index")
ax[0, 1].set_ylabel("Glucose Level")

number = 6
myexplode = [0.2, 0, 0, 0,0,0]
mylabels=[]
for i in range(number):
	mylabels.append(f"Glucose-{i}")

ax[1,0].bar(mylabels,df["Glucose"].head(number))
ax[1,0].set_xticklabels(mylabels,rotation=75)


ax[1,1].pie(df["Glucose"].head(number),labels=mylabels,explode=myexplode,shadow = True)


ax[2,0].barh(mylabels,df["Glucose"].head(number))

# plt.legend()
plt.tight_layout()
st.pyplot(fig)
