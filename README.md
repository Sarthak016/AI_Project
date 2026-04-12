# 📊 AI Data Analyst — Natural Language Analytics & Dashboard Builder

An AI-powered analytics tool that lets you query, visualize, and understand your data using plain English. Upload any CSV, ask questions conversationally, and get SQL, smart charts, and business insights — instantly.

---

## 🌐 Live Demo
👉 https://insightmind-ai.streamlit.app/

---

## 🚀 Features

- 🔍 **Natural Language → SQL** — Ask questions in plain English, get accurate SQL queries powered by Claude
- 🧠 **Smart Chart Selection** — AI automatically picks the best chart type (bar, line, pie, scatter, histogram) based on your data and question
- 💬 **Conversational Follow-ups** — Ask follow-up questions naturally ("now filter by 2024", "break that down by region") with full context memory
- 📊 **Dashboard Builder Mode** — Describe an entire dashboard in one sentence; AI generates multiple charts in a grid layout automatically
- 🧾 **Query Explanation** — Every SQL query explained in plain English
- 🔧 **Auto SQL Fix** — Broken queries are automatically detected and corrected by AI
- 🧩 **Multi-Dataset Support** — Upload multiple CSVs and query across them with JOINs
- 💡 **AI Business Insights** — Specific, number-driven insights generated from your query results

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend & App** | Streamlit |
| **Backend** | Python |
| **Database** | SQLite |
| **AI Model** | Claude Sonnet (Anthropic API) |
| **Visualization** | Plotly |

---

## 📂 How It Works

### 💬 Single Query Mode
1. Upload one or more CSV files
2. Ask any question in plain English
3. Claude generates the SQL query
4. SQL executes on your data
5. Results shown with AI-chosen chart + business insights
6. Ask follow-up questions — the app remembers context

### 📊 Dashboard Builder Mode
1. Upload your CSV files
2. Describe your full dashboard in one sentence
   > *"Show monthly sales trend, top 5 products by revenue, and breakdown by region"*
3. Claude splits it into individual chart questions
4. Multiple charts rendered in a 2-column grid
5. Overall AI insights generated across all charts

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/AI_Project.git
cd AI_Project
pip install -r requirements.txt
```

Add your Anthropic API key to `.streamlit/secrets.toml`:

```toml
ANTHROPIC_API_KEY = "your-api-key-here"
```

Run the app:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

> *(Updated screenshots coming soon)*

---

## 🗂️ Project Structure

```
AI_Project/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── secrets.toml        # API key (not committed to git)
├── data.db                 # SQLite database (auto-generated)
└── README.md
```

---

## 📦 Requirements

```
streamlit
pandas
anthropic
plotly
```

---

## 💡 Example Questions You Can Ask

| Single Query Mode | Dashboard Builder Mode |
|---|---|
| "Show me total sales by month" | "Show monthly trend, top products, and regional breakdown" |
| "Which product has the highest revenue?" | "Give me a sales performance dashboard" |
| "Now filter that by the North region" *(follow-up)* | "Compare revenue vs cost across all categories" |
| "Show correlation between price and quantity" | "Show KPIs: total revenue, top customer, best month" |

---

## 🧠 AI Capabilities

- **Claude Sonnet** handles SQL generation, chart selection, query fixing, and insight generation
- Conversation memory enables natural follow-up questions within a session
- Chart type is selected based on data shape and question intent — not hardcoded
- Dashboard mode decomposes complex requests into individual actionable queries

---

## 👤 Author

Built by [Sarthak Arora](https://github.com/Sarthak016)  
Feel free to ⭐ the repo if you find it useful!
