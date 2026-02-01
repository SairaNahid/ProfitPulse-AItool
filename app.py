import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="ProfitPulse", page_icon="📈")
with st.sidebar:
    st.title("Saira Nahid")
    st.write("🎓 **M.Tech (Computer Science)**")
    st.write("Building AI-driven solutions for small business efficiency.")
    st.divider()
    st.write("- Custom Business AI Tools")
    st.write("- Math & CS Tutoring")
    st.write("- Data Analysis Consulting")

st.title(" ProfitPulse: Business Growth by Saira")
 
tab1, tab2  = st.tabs(["📈 Expense Predictor", "💰 Profit Analyzer"])

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
st.header("📊 Profit Analyzer")
    st.write("Check your business health by testing different sales targets.")

    # 1. THE INPUT (The 'Enter Monthly Revenue' box)
    rev = st.number_input("Enter Monthly Sales Goal ($):", value=2000)

    # 2. THE MATH (Predicting Profit)
    # This uses 'pred' from Tab 1. If Tab 1 hasn't run, it uses a default.
    current_expenses = pred if 'pred' in locals() else 677.33
    live_profit = rev - current_expenses

    # 3. THE RESULT DISPLAY
    st.subheader(f"Projected Net Profit: ${live_profit:,.2f}")

    if live_profit > 0:
        st.success("Target Achieved: Your Business is Profitable! ✅")
    else:
        st.error("Threshold Not Met: High Risk of Loss! ⚠️")

    # 4. THE GROWTH ADVICE (Paste this at the very bottom of Tab 2)
    st.divider()
    st.subheader(" Business Strategy")
    
    if live_profit > 1500:
        st.info("💡 **Strategy:** Your profit is strong! Consider scaling your marketing.")
    elif 0 < live_profit <= 1500:
        st.warning("💡 **Strategy:** Profit is thin. Look for ways to optimize costs.")
    else:
        st.error("💡 **Strategy:** Critical! You must increase prices or cut overhead.")

    





