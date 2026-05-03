import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Dashboard Generator", layout="wide")

st.title("📊 Simple Dashboard Generator")

# Upload file
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:

    # Read file
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found in dataset")
    else:

        st.sidebar.header("⚙️ Chart Settings")

        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Bar Chart", "Line Chart", "Pie Chart"]
        )

        column = st.sidebar.selectbox("Select Column", numeric_cols)

        # BAR CHART
        if chart_type == "Bar Chart":
            fig = px.bar(df, y=column, title=f"Bar Chart - {column}")
            st.plotly_chart(fig)

        # LINE CHART
        elif chart_type == "Line Chart":
            fig = px.line(df, y=column, title=f"Line Chart - {column}")
            st.plotly_chart(fig)

        # PIE CHART
        elif chart_type == "Pie Chart":
            fig = px.pie(df, names=df.index, values=column, title=f"Pie Chart - {column}")
            st.plotly_chart(fig)

    # DOWNLOAD BUTTON
    st.subheader("⬇️ Download Data")

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download CSV File",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )