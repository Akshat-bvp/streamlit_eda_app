import streamlit as st
import pandas as pd 
from openai import OpenAI
import os 
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport 
from eda_utils import *


client = OpenAI(
    base_url = 'https://models.github.ai/inference',
    api_key = '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'
)


st.set_page_config(page_title="EDA app", layout = "wide")
st.title("📊 EDA & Visualisation App")

uploaded_file = st.file_uploader("Upload your csv", type = "csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.write(f"**Shape**{df.shape}")
    st.dataframe(df.dtypes)

    st.subheader("🧹 Data Cleaning")
    method = st.radio("Missing value handling:", ["do nothing", "Drop", "Fill with mean"])
    method_map = {"do nothing":"do_nothing", "Drop": "drop", "Fill with mean":"mean"}
    df = clean_data(df, method=method_map[method])
    st.success(f"Applied method: {method}")

    st.subheader("📈 Statistics")
    st.write(describe_data(df))

    st.subheader("🧠 Profiling Report")
    profile = generate_profile(df)
    st_profile_report(profile)

    st.subheader("📊 Visualisation")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    plot_type = st.selectbox("Plot type", ["Histogram", "Boxplot", "Scatterplot", "Swarmplot", "Correlation Heatmap"])

    if plot_type == "Histogram":
        col = st.selectbox("Numeric column", numeric_cols)
        fig = generate_plot(df, "histogram", x=col)
        st.plotly_chart(fig, use_container_width = True)
        
    elif plot_type == "Boxplot":
        y = st.selectbox("Y (numeric)", numeric_cols)
        x = st.selectbox("X (categorical)", cat_cols)
        fig = generate_plot(df, "boxplot", x=x, y=y)
        st.plotly_chart(fig, use_container_width = True)

    elif plot_type == "Swarmplot":
        y = st.selectbox("Y", numeric_cols)
        x = st.selectbox("X", cat_cols)
        fig = generate_plot(df, "swarm", x=x, y=y)
        st.pyplot(fig)

    elif plot_type == "Correlation Heatmap":
        fig = generate_plot(df, "heatmap")
        st.pyplot(fig)
            
    st.subheader("💬 Ask Chatgpt About Your Data")
    question = st.text_input("Ask Something...")
    if question:
        with st.spinner("Thinking..."):
            prompt = f"Columns: {df.columns.tolist()}\nSample:\n{df.head().to_string()}\nQuestion: {question}"
            completion = client.chat.completions.create(
                model = "openai/gpt-4o-mini",
                messages = [{"role": "system", "content": "You're  helpful data analyst."},
                            {"role": "user", "content": prompt}
                ],
                max_tokens = 500    
            )
            st.success(completion.choices[0].message.content)
else:
    st.info("👈 Upload a CSV file to get started.")  