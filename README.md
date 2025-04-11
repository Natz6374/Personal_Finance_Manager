# Finance Manager – Personal Finance Insights with AI

A Streamlit-based web app to manage and analyze your personal finances. Add transactions manually or via CSV, then get smart insights powered by Google's Gemini Pro LLM using LangChain.

---

## Features

- Add Transactions manually
- Upload CSV bank statements
- Visualize spending by category and over time
- AI-powered insights on:
  - Spending patterns
  - Savings suggestions
  - Budgeting advice

---

## Installation

```bash
git clone https://github.com/your-username/finance-manager.git
cd finance-manager
pip install -r requirements.txt
Set your Google API Key:

bash
Copy
Edit
export GOOGLE_API_KEY=your-google-api-key
Run the app:

bash
Copy
Edit
streamlit run app.py
CSV Format
Your CSV file must have these columns:

Date

Description

Amount

Category

Example:

csv
Copy
Edit
Date,Description,Amount,Category
2024-01-01,Coffee Shop,4.50,Food
2024-01-02,Bus Ticket,2.75,Transport
AI Analysis
The app uses LangChain with Gemini Pro to analyze up to the first 50 transactions and generate:

Top spending categories

Financial habits

Suggestions for saving and budgeting

Tech Stack
Python

Streamlit

Pandas

LangChain

Google Generative AI

License
MIT License

Built to help you understand your money better — one transaction at a time.

yaml
Copy
Edit

---

Let me know if you want this tailored with your GitHub repo link or Hugging Face deployment URL.
