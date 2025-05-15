#streamlit run "E:\college\6th sem\Winniio\streamlit_dashboard\practice12.py"


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Simple Linear Data Dashboard")

st.sidebar.header("Adjust Linear Equation: y = mx + c")
slope = st.sidebar.slider("Slope (m)", min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
intercept = st.sidebar.slider("Intercept (c)", min_value=-20.0, max_value=20.0, value=1.0, step=0.5)

x = np.linspace(-10, 10, 100)
y = slope * x + intercept

fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {slope}x + {intercept}')
ax.set_title("Linear Graph")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend()

st.pyplot(fig)

if st.checkbox("Show data table"):
    st.dataframe({"x": x, "y": y})
