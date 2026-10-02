# 📊 Smart Data Analysis Platform

## About the Project

**Smart Data Analysis Platform** is a Python and Streamlit-based web application designed to make data analysis simple, interactive, and accessible.

The application allows users to upload **CSV or Excel datasets**, explore the data through an interactive dashboard, clean the dataset, create different visualizations, generate a summary report, and get quick insights using the Smart Dataset Assistant.

I built this project to strengthen my skills in **Python, Pandas, Streamlit, data analysis, and data visualization**, while learning how a complete data-analysis application can be developed and organized into reusable modules.

---

## Features

- 📂 Upload CSV and Excel datasets
- 📊 Interactive dashboard with dataset overview
- 🧹 Data cleaning
  - Remove missing values
  - Remove duplicate rows
- 📈 Interactive data visualization
  - Histogram
  - Scatter Plot
  - Box Plot
  - Line Chart
  - Bar Chart
  - Pie Chart
  - Correlation Heatmap
- 🤖 Smart Dataset Assistant for common dataset-related questions
- 📄 Dataset report generator
- 🌙 Clean and responsive dark-themed user interface
- 🧩 Modular project structure for easier maintenance

---

## Technologies Used

- **Python** — Core programming language
- **Streamlit** — Web application framework
- **Pandas** — Data loading, cleaning, and analysis
- **NumPy** — Numerical operations
- **Plotly** — Interactive data visualization

---

## Project Architecture

The application follows a modular structure where different components handle specific responsibilities.

```text
Smart_Data_Analysis_Platform/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── utils/
    ├── ai_assistant.py
    ├── dashboard.py
    ├── data_loader.py
    ├── data_cleaning.py
    ├── visualization.py
    └── report_generator.py
```

### Module Description

| Module | Purpose |
|---|---|
| `app.py` | Main Streamlit application and user interface |
| `data_loader.py` | Loads CSV and Excel datasets |
| `data_cleaning.py` | Handles data-cleaning operations |
| `dashboard.py` | Displays dataset overview and dashboard information |
| `visualization.py` | Creates interactive charts using Plotly |
| `ai_assistant.py` | Provides rule-based dataset insights |
| `report_generator.py` | Generates a summary report of the dataset |

The modular structure keeps the application organized, easier to debug, maintain, and extend.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/2chandana5/Smart_Data_Analysis_Platform.git
```

### 2. Move into the Project Directory

```bash
cd Smart_Data_Analysis_Platform
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## How to Use

1. Launch the application using Streamlit.
2. Upload a CSV or Excel dataset.
3. View the dataset overview through the dashboard.
4. Clean the data by removing missing values or duplicate rows.
5. Select the required columns and create visualizations.
6. Use the Smart Dataset Assistant to get quick insights.
7. Generate and download the dataset report.

---

## Smart Dataset Assistant

The application includes a **Smart Dataset Assistant** that helps users quickly understand their uploaded dataset.

It uses **Python and Pandas with rule-based logic** to answer common dataset-related questions.

The assistant can provide information such as:

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Numerical columns
- Categorical columns
- Maximum values
- Minimum values
- Average values
- Basic dataset statistics

### Example

For a dataset containing employee information, a user could ask questions such as:

```text
How many rows are there?
```

or

```text
What is the average salary?
```

The assistant processes the request and performs the corresponding operation on the uploaded dataset.

---

## Data Cleaning

The platform provides basic data-cleaning functionality to prepare datasets for analysis.

### Missing Values

Users can remove rows containing missing values.

Example:

```python
df.dropna()
```

### Duplicate Records

Users can remove duplicate rows.

Example:

```python
df.drop_duplicates()
```

These operations help improve the quality and consistency of the dataset before analysis.

---

## Data Visualization

The platform provides several interactive visualizations using **Plotly**.

### Histogram

Used to understand the distribution of numerical data.

### Scatter Plot

Used to examine the relationship between two numerical variables.

### Box Plot

Used to understand data distribution and identify potential outliers.

### Line Chart

Used to visualize trends over a sequence such as time.

### Bar Chart

Used to compare values across categories.

### Pie Chart

Used to show proportions among categories.

### Correlation Heatmap

Used to visualize relationships between numerical variables.

---

## Report Generator

The platform includes a report-generation feature that provides a summary of the uploaded dataset.

The report can include information such as:

- Dataset dimensions
- Column names
- Data types
- Missing values
- Basic statistics
- Dataset summary

This provides users with a consolidated overview of their data.

---

## Key Learning Outcomes

Working on this project helped me improve my understanding of:

- Building web applications using Streamlit
- Python-based data analysis
- Data cleaning and preprocessing
- Working with Pandas DataFrames
- Creating interactive visualizations using Plotly
- Numerical data processing using NumPy
- Modular Python programming
- Designing a simple and user-friendly interface
- Organizing a data-analysis application into reusable components

---

## Future Improvements

Planned improvements for future versions include:

- 🤖 AI-powered natural-language queries using LLMs
- 📄 PDF report generation
- 🤖 Machine-learning prediction models
- 📊 Advanced statistical analysis
- 🔐 User authentication
- ☁️ Cloud deployment
- 📈 More advanced interactive dashboards
- 🧠 More intelligent dataset recommendations

---

## Author

**Chandana Chadalawada**

Bachelor of Technology  
Computer Science and Engineering

Interested in **Software Development, Data Science, Python, AI, and Data Analytics**.

---

## License

This project was created for learning purposes and personal portfolio use.
