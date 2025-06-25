# 📊 Streamlit EDA App

An interactive, browser-based EDA (Exploratory Data Analysis) tool built with **Streamlit**, designed to help data analysts, students, and enthusiasts explore CSV datasets with ease.

---

## ✨ Features

- 📁 Upload any CSV file
- 🧹 Clean missing values (drop, fill with mean, etc.)
- 📈 Auto-generate descriptive statistics
- 🧠 Pandas Profiling report integration
- 📊 Plot histograms, boxplots, scatterplots, heatmaps, swarmplots
- 💬 Ask ChatGPT (GPT-4o) questions about your data using the OpenAI API
- 🧠 Modular backend (`eda_utils.py`) for easy maintenance

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/your-username/streamlit-eda-app.git
cd streamlit-eda-app

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
