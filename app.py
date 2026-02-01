import streamlit as stimport numpy as npfrom sklearn.linear_model import LinearRegression

# --- . THE APP INTERFACE ---
st.title(" Bakery Growth & ProfitPulse")

tab1, tab2 = st.tabs([" Expense Forecast", " Profit Simulator"])
with tab1:    st.subheader("Predict Next Month's Bills")  
  data = st.text_input("Past 6 months expenses (comma separated):", "500, 550, 600, 580, 620, 650")   
is_fest = st.toggle("Is next month a Festival?")       
if data:       
  y = np.array([float(x.strip()) for x in data.split(",")]).reshape(-1, 1)       
  x = np.array(range(len(y))).reshape(-1, 1)       
  model = LinearRegression().fit(x, y)        
  pred = model.predict([[len(y)]])[0][0]        
  if is_fest: pred *= 1.3        
    st.metric("Predicted Bill", f"${pred:,.2f}")
with tab2:    st.subheader("What-If Simulator")    
  rev = st.number_input("Monthly Revenue", value=2000)   
inf = st.slider("Simulate Inflation (%)", 0, 30, 5)   
st.metric("Adjusted Profit", f"${rev - (pred * (1 + inf/100)):,.2f}")


# --- TAB 3: STUDENT & TUTOR CORNER ---with tab3:   
st.header(" Interactive Math Solver")   
st.write("Helping students visualize Calculus & Algebra through code.")       
math_topic = st.selectbox("Choose a Topic to Visualize:", ["Linear Equations", "Quadratic Curves", "Calculus: Derivatives"])
    if math_topic == "Linear Equations":      
      st.write("Equation: $y = mx + c$")      
      m = st.slider("Slope (m)", -10.0, 10.0, 2.0)       
      c = st.slider("Intercept (c)", -50, 50, 0)             
      x = np.linspace(-10, 10, 100)      
      y = m * x + c              
      fig, ax = plt.subplots()       
      ax.plot(x, y, color='green')       
      ax.axhline(0, color='black', lw=1)       
      ax.axvline(0, color='black', lw=1)       
      ax.set_title(f"Visualizing $y = {m}x + {c}$")      
      st.pyplot(fig)
    elif math_topic == "Quadratic Curves":       
      st.write("Equation: $y = ax^2 + bx + c$")      
      a = st.slider("Curvature (a)", -5.0, 5.0, 1.0)              
      x = np.linspace(-10, 10, 100)       
      y = a * (x**2)               
      fig, ax = plt.subplots()        
      ax.plot(x, y, color='purple')       
      st.pyplot(fig)       
      st.info("Notice how the 'a' value changes the width of the parabola!")



