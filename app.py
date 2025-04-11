import streamlit as st
import pandas as pd
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "your-google-api-key")  

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.5,
    convert_system_message_to_human=True
)

def analyze_transactions(df):
    """Generate financial insights using LLM"""
    prompt = PromptTemplate(
        input_variables=["transactions"],
        template="""
        Analyze these transactions:
        {transactions}

        Provide:
        1. Spending patterns (top categories, trends)
        2. Savings suggestions
        3. Budgeting advice
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(transactions=df.head(50).to_string())

st.set_page_config(
    page_title="Finance Manager",
    layout="centered",
    initial_sidebar_state="expanded"
)

if "transactions" not in st.session_state:
    st.session_state.transactions = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])

page = st.sidebar.selectbox("Menu", ["Add Transaction", "Upload CSV", "View Insights"])

if page == "Add Transaction":
    st.header("➕ Add Transaction")
    with st.form("transaction_form"):
        cols = st.columns(2)
        with cols[0]:
            date = st.date_input("Date")
        with cols[1]:
            category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])

        description = st.text_input("Description")
        amount = st.number_input("Amount", min_value=0.01, step=0.01, format="%.2f")

        if st.form_submit_button("Add"):
            new_transaction = pd.DataFrame([[date, description, amount, category]],
                                           columns=["Date", "Description", "Amount", "Category"])
            st.session_state.transactions = pd.concat([st.session_state.transactions, new_transaction], ignore_index=True)
            st.success("Transaction added!")

elif page == "Upload CSV":
    st.header(" Upload Statement")
    uploaded_file = st.file_uploader("Choose CSV", type="csv")
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            required_cols = {"Date", "Description", "Amount", "Category"}
            if not required_cols.issubset(df.columns):
                st.error("CSV must contain: Date, Description, Amount, Category columns")
            else:
                st.session_state.transactions = pd.concat([st.session_state.transactions, df], ignore_index=True)
                st.success(f" Added {len(df)} transactions!")
        except Exception as e:
            st.error(f"Error: {str(e)}")

elif page == "View Insights":
    st.header("Insights")

    if not st.session_state.transactions.empty:
        with st.expander("View Transactions"):
            st.dataframe(st.session_state.transactions, hide_index=True)

        st.subheader("Spending Breakdown")
        tab1, tab2 = st.tabs(["By Category", "Over Time"])

        with tab1:
            st.bar_chart(st.session_state.transactions.groupby("Category")["Amount"].sum())

        with tab2:
            st.line_chart(st.session_state.transactions.set_index("Date")["Amount"])

        st.subheader("AI Analysis")
        if st.button("Generate Insights", type="primary"):
            with st.spinner("Analyzing..."):
                try:
                    insights = analyze_transactions(st.session_state.transactions)
                    st.markdown(f"```\n{insights}\n```")
                except Exception as e:
                    st.error(f"Analysis failed: {str(e)}")
    else:
        st.warning("No transactions found. Add or upload data first.")

st.sidebar.markdown("---")
st.sidebar.caption(" Deployed on Hugging Face Spaces")
