# 📈 Smart Financial Market Analytics and Stock Prediction using Apache Spark

## 📌 Project Overview

The **Smart Financial Market Analytics and Stock Prediction System** is developed using **Apache Spark (PySpark)** to perform large-scale financial data analysis and predict stock closing prices using Machine Learning.

The project demonstrates distributed data processing, Exploratory Data Analysis (EDA), Spark SQL, ETL, feature engineering, and stock price prediction using **Random Forest Regression**.

---

## 🎯 Objectives

- Analyze historical stock market data using Apache Spark.
- Perform Exploratory Data Analysis (EDA).
- Implement RDD and DataFrame operations.
- Execute Spark SQL queries for financial analysis.
- Build ETL pipelines for data preprocessing.
- Develop a Machine Learning model to predict stock closing prices.
- Evaluate model performance using RMSE, MAE, and R² Score.

---

## 🛠 Technologies Used

- Apache Spark
- PySpark
- Python
- Spark SQL
- Pandas
- NumPy
- Matplotlib
- Apache Spark MLlib
- Git & GitHub
- Google Colab

---

## 📂 Project Structure

```
Smart_Financial_Market_Analytics_Case_Study/
│
├── notebooks/
│   └── Smart_Financial_Market_Analytics_Case_Study.ipynb
│
├── data/
│   └── Dataset Link / Dataset Description
│
├── screenshots/
│   ├── EDA_Output.png
│   ├── SparkSQL_Output.png
│   ├── Model_Result.png
│
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

Dataset contains historical stock market information including:

- Date
- Open Price
- High Price
- Low Price
- Close Price
- Volume
- Stock Symbol

Dataset folders:

- Stocks
- ETFs
- Data (Financial News)

Only the **Stocks** dataset was used for this project.

---

## ⚙️ Features Implemented

- Spark Session Creation
- Multiple Stock File Loading
- Data Cleaning
- Missing Value Detection
- Duplicate Detection
- Statistical Analysis
- RDD Operations
- Pair RDD Operations
- DataFrame Operations
- Window Functions
- Spark SQL Queries
- ETL Pipeline
- Feature Engineering
- Machine Learning using Random Forest Regression
- Model Evaluation
- Data Visualization

---

## 📈 Machine Learning Model

Algorithm Used:

- Random Forest Regression

### Input Features

- Open
- High
- Low
- Volume

### Target Variable

- Close Price

---

## 📉 Model Performance

| Metric | Value |
|---------|---------|
| RMSE | 3.03 |
| MAE | 0.78 |
| R² Score | 0.959 |

The model achieved high prediction accuracy and successfully predicted stock closing prices using historical market data.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/RonakkudalAI/Smart_Financial_Market_Analytics_Case_Study.git
```

Move into the project directory

```bash
cd Smart_Financial_Market_Analytics_Case_Study
```

Install dependencies

```bash
pip install pyspark pandas numpy matplotlib
```

---

## ▶️ Execution

Run the Jupyter Notebook

```bash
jupyter notebook
```

or open

```
Smart_Financial_Market_Analytics_Case_Study.ipynb
```

Execute all cells sequentially.

---

## 📌 Key Insights

- Historical stock prices exhibit significant fluctuations over time.
- Trading volume varies across different companies and reflects market activity.
- Data preprocessing improved overall dataset quality by removing missing and duplicate records.
- Spark SQL enabled efficient company-wise and time-based financial analysis.
- Random Forest Regression accurately predicted stock closing prices with excellent performance.

---

## 📷 Output

The project generates:

- Exploratory Data Analysis
- Spark SQL Analysis
- Stock Price Trends
- Trading Volume Analysis
- Closing Price Distribution
- Machine Learning Predictions
- RMSE, MAE and R² Evaluation Metrics

---

## 🔮 Future Scope

- Real-time stock market prediction using live APIs.
- Financial news sentiment analysis.
- Deep Learning models (LSTM, GRU, Transformers).
- Streamlit dashboard for interactive visualization.
- Cloud deployment using Docker and Kubernetes.

---

## 👨‍💻 Author

**Ronak Kudal**

Artificial Intelligence & Machine Learning

GitHub: https://github.com/RonakkudalAI

---

## 📄 License

This project is developed for educational and academic purposes.
