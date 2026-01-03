# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 2. PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="RBI Monetary Policy Dashboard",
    layout="wide"
)

# ==============================
# 3. PAGE TITLE & DESCRIPTION
# ==============================
st.title("RBI Monetary Policy & Inflation Dashboard")

st.markdown("""
**Objective:**  
Analyze how RBI's repo rate changes affect inflation using official RBI data.

**Data Source:** Reserve Bank of India (RBI – DBIE)
""")

# ==============================
# 4. LOAD EXCEL DATA
# ==============================
# Make sure your Excel file is in a folder named 'data'
# Example: data/rbi_macro_data.xlsx
df = pd.read_excel(rbi_macro_data.xlsx", sheet_name="Sheet1", parse_dates=["Date"])

# Set date as index and sort
df.set_index("Date", inplace=True)
df.sort_index(inplace=True)

# Clean column names: lowercase + underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Show columns for verification (optional)
st.write("Columns in dataset:", df.columns)

# ==============================
# 5. SIDEBAR FILTERS
# ==============================
st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", df.index.min())
end_date = st.sidebar.date_input("End Date", df.index.max())

# Filter the dataframe based on sidebar selection
df_filtered = df[(df.index >= pd.to_datetime(start_date)) &
                 (df.index <= pd.to_datetime(end_date))]

# ==============================
# 6. KEY METRICS
# ==============================
st.subheader("Key Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Repo Rate (%)",
    round(df_filtered["repo_rate"].mean(), 2)
)

col2.metric(
    "Average Inflation (%)",
    round(df_filtered["inflation_rate"].mean(), 2)
)

col3.metric(
    "Correlation",
    round(df_filtered["repo_rate"].corr(df_filtered["inflation_rate"]), 2)
)

# ==============================
# 7. TIME-SERIES PLOT
# ==============================
st.subheader("Repo Rate vs Inflation (Time Series)")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df_filtered.index, df_filtered["repo_rate"], label="Repo Rate")
ax.plot(df_filtered.index, df_filtered["inflation_rate"], label="Inflation Rate")
ax.set_xlabel("Date")
ax.set_ylabel("Percent")
ax.legend()
st.pyplot(fig)

# ==============================
# 8. FOOTER / INTERPRETATION
# ==============================
st.markdown("""
### Interpretation
- Repo rate changes influence inflation with a **time lag**.
- This relationship aligns with RBI’s monetary transmission framework.
- Inflation is also influenced by other macroeconomic factors beyond repo rate.
""")