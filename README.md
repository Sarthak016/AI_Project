# 🤖 AI-Powered Data Analytics Assistant

An AI-driven analytics tool that allows users to query datasets using natural language. The system converts user queries into SQL, executes them on structured data, and returns results with visualizations and insights.

---

## 🚀 Features

- 🔍 Natural Language → SQL query generation using LLMs  
- 📊 Automatic data visualization using Plotly  
- 🧠 AI-generated business insights  
- 🧾 Query explanation in simple terms  
- 🔧 Automatic SQL error detection and correction  
- 📁 Support for multiple datasets (multi-table querying)

---

## 🛠️ Tech Stack

- **Frontend & App:** Streamlit  
- **Backend:** Python  
- **Database:** SQLite  
- **AI Model:** Claude (Anthropic API)  
- **Visualization:** Plotly  

---

## 📂 How It Works

1. Upload one or more CSV files  
2. Ask questions in plain English  
3. AI converts query → SQL  
4. SQL executes on database  
5. Results are displayed with charts & insights  

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/ai-data-analyst.git
cd ai-data-analyst
pip install -r requirements.txt
streamlit run app.py
