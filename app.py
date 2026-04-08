import streamlit as st
import pandas as pd
import sqlite3
import anthropic
import plotly.express as px
import re

@st.cache_resource
def get_connection():
    return sqlite3.connect("data.db", check_same_thread=False)

conn = get_connection()

# Initialize client
client = anthropic.Anthropic(
    api_key=st.secrets["ANTHROPIC_API_KEY"]
)

st.title("AI Query Generator")

uploaded_files = st.file_uploader("Upload CSVs", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    
    table_info = []   # ✅ store schema info

    for file in uploaded_files:
        try:
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file, encoding='latin1')
                st.warning(f"{file.name}: Loaded using latin1 encoding")
            except UnicodeDecodeError:
                df = pd.read_csv(file, encoding='ISO-8859-1')
                st.warning(f"{file.name}: Loaded using ISO-8859-1 encoding")
    
        table_name = file.name.split(".")[0].replace(" ", "_").lower()
    
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        # Store schema
        cols = ", ".join(df.columns)
        table_info.append(f"{table_name} ({cols})")

        st.write(f"✅ Loaded table: {table_name}")
        st.dataframe(df.head())
    st.info("You can now ask questions across multiple datasets.")

    st.subheader("Available Tables")
    for info in table_info:
        st.write(info)    

    question = st.text_input("Ask your question:")

    if question:
        tables_schema = "\n".join(table_info)

        prompt = f"""
        You are a data analyst.

        Here are the available tables and their columns:

        {tables_schema}

        If multiple tables are needed, use JOINs appropriately.

        Convert the user's question into SQL.

        Question: {question}

        Only return SQL query. No explanation.
"""


        try:
            response = client.messages.create(
                model="claude-sonnet-4-0",
                max_tokens=200,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Clean SQL
            raw_sql = response.content[0].text.strip()

            match = re.search(r"(SELECT .*?)(;|$)", raw_sql, re.IGNORECASE | re.DOTALL)
            if match:
                sql_query = match.group(1)
            else:
                sql_query = raw_sql

            sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

            st.code(sql_query, language="sql")
            try:
                explanation_prompt = f"""
                Explain this SQL query in simple terms:

                {sql_query}

                Keep it short.
                """

                explanation_response = client.messages.create(
                    model="claude-sonnet-4-0",
                    max_tokens=100,
                    messages=[{"role": "user", "content": explanation_prompt}]
                )

                st.subheader("Query Explanation")
                st.write(explanation_response.content[0].text)

            except:
                st.warning("Could not generate explanation")

            # Execute SQL
            # ✅ Execute SQL with auto-fix
            try:
                result = pd.read_sql_query(sql_query, conn)
                st.write(result)

            except Exception as e:
                st.warning("Query failed. Trying to fix...")

                fix_prompt = f"""
                The following SQL query failed:

                {sql_query}

                Error:
                {e}

                Fix the SQL query. Only return corrected SQL.
                """

                try:
                    fix_response = client.messages.create(
                        model="claude-sonnet-4-0",
                        max_tokens=200,
                        messages=[
                            {"role": "user", "content": fix_prompt}
                        ]
                    )

                    fixed_sql = fix_response.content[0].text.strip()
                    fixed_sql = fixed_sql.replace("```sql", "").replace("```", "").strip()

                    st.code(fixed_sql, language="sql")

                    result = pd.read_sql_query(fixed_sql, conn)
                    st.success("Query fixed and executed!")
                    st.write(result)

                except:
                    st.error("Could not fix query")

            # 📊 Smart Chart
            if 'result' in locals():
                try:
                    numeric_cols = result.select_dtypes(include=['number']).columns

                    if len(result.columns) >= 2 and len(numeric_cols) >= 1:
                        x_col = result.columns[0]
                        y_col = numeric_cols[0]

                        fig = px.bar(result, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
                        st.plotly_chart(fig)

                except:
                    st.warning("Could not generate chart")

            # 🧠 Insights (always runs)
            if 'result' in locals():
                try:
                    insight_prompt = f"""
                    You are a data analyst.

                    Here is the data:
                    {result.head(10).to_string()}

                    Give 2-3 short business insights.
                    """

                    insight_response = client.messages.create(
                        model="claude-sonnet-4-0",
                        max_tokens=150,
                        messages=[
                            {"role": "user", "content": insight_prompt}
                        ]
                    )

                    insights = insight_response.content[0].text
                    st.subheader("Insights")
                    st.write(insights)

                except:
                    st.warning("Could not generate insights")

        except Exception as e:
            st.error(f"Error: {e}")
