import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="ProfitPulse AI", page_icon="📈")
with st.sidebar:
    st.title("Saira Nahid")
    st.write("🎓 **M.Tech (Computer Science)**")
    st.write("Building AI-driven solutions for small business efficiency.")
    st.divider()
    st.write("- Custom Business AI Tools")
    st.write("- Math & CS Tutoring")
    st.write("- Data Analysis Consulting")

st.title(" ProfitPulse: Business Growth AI")

tab1, tab2  = st.tabs(["📈 Expense Forecast", "💰 Profit Simulator"])

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
    
    # 1. This creates the input box
    rev = st.number_input("Enter your sales goal:", value=2000)
    
    # 2. This does the live calculation
    # (If Tab 1 hasn't run yet, we use a default of 1200)
    current_expenses = pred if 'pred' in locals() else 1200
    live_profit = rev - current_expenses
    
    # 3. This shows the result instantly
    st.header(f"Calculated Profit: ${live_profit:,.2f}")
    
    if live_profit > 0:
        st.success("You are in the Green! ✅")
    else:
        st.error("Warning: High Risk of Loss! ⚠️")

  st.subheader("🤖 AI Growth Advice")
    if live_profit > 1500:
        st.info("💡 **Strategy:** Your profit is strong! Consider scaling your marketing.")
    elif 0 < live_profit <= 1500:
        st.warning("💡 **Strategy:** Profit is thin. Look for ways to optimize costs.")
    else:
        st.error("💡 **Strategy:** Critical! You must increase prices or cut overhead.")






