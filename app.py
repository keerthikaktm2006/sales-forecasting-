import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# -------------------------------
# Title
# -------------------------------
st.title("📊 Tomorrow Sales Prediction")
st.write("Random Forest Regressor based Sales Forecasting")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    return df

df = load_data()

# -------------------------------
# Feature Engineering
# -------------------------------
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day

# Target & Features
X = df[['Year', 'Month', 'Day']]
y = df['Sales']

# -------------------------------
# Train Random Forest Model
# -------------------------------
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
model.fit(X, y)

# -------------------------------
# User Input
# -------------------------------
st.subheader("🔢 Enter Date for Tomorrow Prediction")

year = st.number_input("Year", min_value=2015, max_value=2035, value=2026)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
day = st.number_input("Day", min_value=1, max_value=31, value=26)

input_data = pd.DataFrame({
    'Year': [year],
    'Month': [month],
    'Day': [day]
})

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Tomorrow Sales"):
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Sales: {prediction[0]:.2f}")

# -------------------------------
# Visualization
# -------------------------------
st.subheader("📈 Historical Sales Overview")

daily_sales = df.groupby('Order Date')['Sales'].sum()

fig = plt.figure()
plt.plot(daily_sales)
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Historical Sales Trend")
st.pyplot(fig)
