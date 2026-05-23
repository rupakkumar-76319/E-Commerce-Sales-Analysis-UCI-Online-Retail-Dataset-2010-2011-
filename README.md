# E-Commerce Sales Analysis
### UCI Online Retail Dataset (2010–2011)

## What This Project Is About

I picked up this dataset because it is real transactional data from
an actual UK-based online retail store. It covers two full years of
orders which gave me enough data to look at trends properly rather
than just surface level numbers.

The main goal was to understand where the revenue was coming from,
which products were moving, and how sales changed over time.

---

## Dataset

- **Source:** UCI Machine Learning Repository
- **Records:** 541,909 transactions
- **Period:** December 2010 to December 2011
- **Countries:** 38 countries
- **Columns:** InvoiceNo, StockCode, Description, Quantity,
  InvoiceDate, UnitPrice, CustomerID, Country

---

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## What I Did

**Step 1 — Cleaning the Data**
The raw dataset had quite a few problems. There were cancelled
orders mixed in with normal ones, a good chunk of rows had no
CustomerID, and some quantity and price values did not make sense.
I removed all of that before doing any analysis so the numbers
would actually mean something.

**Step 2 — Exploratory Analysis**
Once the data was clean I started digging into it. I looked at
which countries were ordering the most, which months had the
highest sales, and which products kept appearing in orders again
and again.

**Step 3 — Visualisation**
I built charts for everything that mattered — monthly revenue
trend, top 10 products by quantity sold, country-wise revenue
split, and order frequency distribution. The idea was to make
the findings easy to understand at a glance.

---

## Key Findings

- The United Kingdom made up around 84% of all transactions
  in the dataset
- November 2011 had the highest revenue across the entire
  two year period likely due to pre-holiday buying
- A small group of about 10 products accounted for a
  disproportionately large share of total units sold
- A significant number of high value customers placed orders
  repeatedly throughout the year rather than just once

---

## Output

All charts and visualisation outputs are saved in the
`/outputs` folder.

---

## How to Run

1. Clone the repo
2. Install requirements: `pip install pandas matplotlib seaborn`
3. Open `analysis.ipynb` in Jupyter Notebook
4. Run all cells from top to bottom

---

## Folder Structure
├── data/
│   └── online_retail.xlsx
├── outputs/
│   └── summary.txt
├── Scripts
│   └── ecsa_EDA.py
├── .gitignore/
├── LICENCE/
└── README.md

---

## About

This was done as part of building my data analysis portfolio.
The dataset is publicly available on the UCI Machine Learning
Repository and has been widely used for retail analytics practice.
