# 📊 Sales Data Analysis Dashboard

## Overview

The **Sales Data Analysis Dashboard** is a Python-based project that analyzes sales data from a CSV file and generates key business insights. The project demonstrates basic data analytics techniques such as data processing, KPI calculation, and sales performance analysis using Python's built-in libraries.

---

## Features

* Reads sales data from a CSV file
* Calculates Total Sales, Total Profit, and Total Quantity Sold
* Displays the total number of orders
* Analyzes sales by region
* Generates a simple sales summary in the console
* Lightweight implementation without external data analysis libraries

---

## Technologies Used

* Python 3.13
* CSV Module (Built-in Python Library)

---

## Project Structure

```
Sales-Data-Analysis/
│
├── sales_analysis.py
├── sales_data.csv
└── README.md
```

---

## Dataset

The dataset contains the following fields:

* Order ID
* Date
* Region
* Category
* Product
* Sales
* Profit
* Quantity

---

## How to Run

1. Download or clone the repository.
2. Place `sales_analysis.py` and `sales_data.csv` in the same folder.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python sales_analysis.py
```

---

## Sample Output

```
========================================
SALES DATA ANALYSIS
========================================

Total Sales    : ₹XXXXXX
Total Profit   : ₹XXXXX
Total Quantity : XXX

Sales by Region

North : XXXXX
South : XXXXX
East  : XXXXX
West  : XXXXX
```

---

## Learning Outcomes

This project demonstrates:

* Reading CSV files in Python
* Data processing using dictionaries
* Aggregating sales information
* Business KPI calculation
* Basic data analytics concepts
* Console-based reporting

---

## Future Enhancements

* Add graphical charts and dashboards
* Interactive filtering
* Monthly and yearly sales trends
* Product-wise and category-wise analysis
* Export reports to Excel or PDF

---
