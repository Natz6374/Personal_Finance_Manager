# Finance Manager – Personal Finance Insights with AI

A Streamlit-based web app to manage and analyze your personal finances. Add transactions manually or via CSV, then get smart insights powered by Google's Gemini Pro LLM using LangChain.

---

## Features

- Add transactions manually through a form
- Upload CSV bank statements
- View spending insights by category and over time
- Generate AI-powered financial analysis:
  - Spending patterns
  - Savings suggestions
  - Budgeting advice

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/finance-manager.git
cd finance-manager
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Set your Google API key as an environment variable:

```bash
export GOOGLE_API_KEY=your-google-api-key
```

Replace `"your-google-api-key"` with your actual Google Generative AI API key.

---

## Run the App

Launch the app using Streamlit:

```bash
streamlit run app.py
```

The app will open in your default web browser.

---

## CSV Format

Uploaded CSV files must contain the following columns:

- `Date`
- `Description`
- `Amount`
- `Category`

### Example:

```csv
Date,Description,Amount,Category
2024-01-05,Groceries,50.75,Food
2024-01-06,Taxi Ride,15.00,Transport
```

---

## AI Analysis

The app uses LangChain and Google’s Gemini Pro model to process up to the first 50 transactions and provide:

- Insights on top spending categories
- Financial trends
- Personalized savings and budgeting advice

---

## Deployment (Optional)

You can deploy this app on platforms like:

### Hugging Face Spaces

1. Create a new Streamlit space
2. Upload your project files
3. Set the `GOOGLE_API_KEY` in the space’s **Secrets**

### Heroku

1. Create a new app on Heroku
2. Add buildpacks for Python
3. Set `GOOGLE_API_KEY` in your config vars
4. Push your code via Git

---

## Tech Stack

- Python
- Streamlit
- Pandas
- LangChain
- Google Generative AI (Gemini Pro)

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Generative AI](https://ai.google/)
- [Streamlit](https://streamlit.io/)
