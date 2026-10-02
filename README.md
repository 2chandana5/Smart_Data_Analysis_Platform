#  📊 Smart Data Analysis Platform

## About the Project

AI Data Analyst Assistant is a web application built using **Python** and **Streamlit** to make basic data analysis simple and interactive. The application allows users to upload a CSV or Excel dataset, clean the data, visualize it through different charts, generate a report, and get quick insights about the dataset.

I built this project to strengthen my skills in Python, Pandas, Streamlit, and data visualization while learning how data analysis applications are developed. The project follows a modular structure, making the code simple, organized, and easy to understand.

---

## Features

- 📂 Upload CSV and Excel datasets
- 📊 Interactive Dashboard with dataset overview
- 🧹 Data Cleaning
  - Remove missing values
  - Remove duplicate rows
- 📈 Data Visualization
  - Histogram
  - Scatter Plot
  - Box Plot
  - Line Chart
  - Bar Chart
  - Pie Chart
  - Correlation Heatmap
- 🤖 Smart Dataset Assistant to answer common questions about the uploaded dataset
- 📄 Report Generator with dataset summary
- 🌙 Clean and responsive dark-themed user interface

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly

---

## Project Structure

```text
AI-Data-Analyst-Assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── utils/
│   ├── ai_assistant.py
│   ├── dashboard.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── visualization.py
│   └── report_generator.py
│
└── venv/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/2chandana5/Smart_Data_Analysis_Platform.git
```

Move into the project folder

```bash
cd Smart_Data_Analysis_Platform
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## How to Use

1. Launch the application.
2. Upload a CSV or Excel dataset.
3. View the dashboard to understand the dataset.
4. Clean the data if needed.
5. Create different visualizations.
6. Ask questions using the Smart Dataset Assistant.
7. Generate and download the dataset report.

---

## Smart Dataset Assistant

The application includes a Smart Dataset Assistant that helps users understand their uploaded dataset. It can answer common questions such as:

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Numeric columns
- Categorical columns
- Highest value
- Lowest value
- Average values
- Basic dataset summary

The assistant is built using Python and Pandas with simple rule-based logic to provide quick responses based on the uploaded data.

---

## What I Learned

Working on this project helped me improve my understanding of:

- Building web applications using Streamlit
- Working with Pandas for data analysis
- Cleaning and preparing datasets
- Creating interactive charts using Plotly
- Writing modular and reusable Python code
- Designing a simple and user-friendly interface

---

## Future Improvements

Some features that can be added in future versions include:

- AI-powered natural language queries using LLMs
- PDF report generation
- Machine Learning prediction models
- More advanced statistical analysis
- User authentication
- Cloud deployment

---

## Author

**Chandana Chadalawada**

Bachelor of Technology (Computer Science and Engineering)

Interested in Data Science, Python, AI, and Data Analytics.

---

## License

This project is created for learning purposes and personal portfolio use.
