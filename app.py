import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="ProfitPulse AI", page_icon="📈")

st.title("🧁 ProfitPulse: Bakery Growth AI")

tab1, tab2, tab3 = st.tabs(["📈 Expense Forecast", "💰 Profit Simulator", "📐 Math Solver"])

with tab1:
    st.subheader("Predict Next Month's Bills")
    data = st.text_input("Past 6 months expenses (comma separated):", "500, 550, 600, 580, 620, 650")
    if data:
        y = np.array([float(x.strip()) for x in data.split(",")]).reshape(-1, 1)
        x = np.array(range(len(y))).reshape(-1, 1)
        model = LinearRegression().fit(x, y)
        pred = model.predict([[len(y)]])[0][0]
        st.metric("Predicted Next Bill", f"${pred:,.2f}")

with tab2:
    st.subheader("What-If Simulator")
    rev = st.number_input("Monthly Revenue", value=2000)
    st.write("Adjust your revenue and costs to see potential profit.")

with tab3:
    st.subheader("Student Corner: Math Visualizer")
    m = st.slider("Slope (m)", -10.0, 10.0, 2.0)
    st.write(f"Visualizing the equation: y = {m}x")


