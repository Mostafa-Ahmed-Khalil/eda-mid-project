# Retail Store Sales EDA Dashboard

## Overview
This project explores and visualizes retail store sales data using Python, Pandas, Plotly, and Streamlit.

The project includes:
- Data inspection and cleaning in `eda.ipynb`
- Feature engineering for transaction dates
- Exploratory analysis of sales, products, customers, and transactions
- An interactive Streamlit dashboard with filters, metrics, charts, insights, and recommendations

## Dataset
The project uses the Retail Store Sales dataset from Kaggle:
[Retail Store Sales Dataset](https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning/data)

The dataset includes transaction-level information such as:
- Transaction and customer identifiers
- Product categories and items
- Transaction dates
- Quantity and price per unit
- Total amount spent
- Payment method
- Location
- Discount status

- **Raw dataset path:** `retail_store_sales.csv`
- **Cleaned dataset path:** `data/cleaned_df.csv`

## Project Objectives
The main objectives are to:
- Inspect the structure and quality of the retail sales data
- Correct data types and handle missing values
- Derive useful date-based features
- Analyze sales performance across products, categories, customers, locations, and payment methods
- Explore transaction and quantity distributions
- Present findings through an interactive Streamlit dashboard

## Data Cleaning & Preprocessing
The notebook performs the following preprocessing steps:
1. Loads the raw CSV dataset with Pandas.
2. Inspects the data using `head()`, `info()`, and descriptive statistics.
3. Converts:
   - Quantity to nullable integer type
   - Transaction Date to a datetime value
   - Discount Applied to a boolean type during inspection
4. Converts missing discount values to "Unknown" for analysis.
5. Fills missing Price Per Unit values when both Total Spent and Quantity are available:
   $$\text{Price Per Unit} = \frac{\text{Total Spent}}{\text{Quantity}}$$
6. Creates a reference table using valid category, item, and price combinations.
7. Uses the reference table to fill missing item values when the category and price identify an item.
8. Removes rows where both Quantity and Total Spent are missing.
9. Checks for duplicate rows.
10. Creates date features: Transaction Year, Transaction Month, and Transaction Day.
11. Removes Transaction Date and Transaction ID after feature extraction.
12. Saves the processed data to `data/cleaned_df.csv`.

## Exploratory Data Analysis
The notebook investigates the following questions across multiple dimensions:

- **Sales Analysis:**
  - Which category has the highest total sales?
  - Which items generate the highest total sales?
  - How does total sales vary by year and month?
  - What is the distribution of transaction amounts?
  - Which discount status generates the highest total sales?
- **Category and Product Analysis:**
  - Which category has the highest total quantity sold, average spending, average price per unit, and number of transactions?
  - Which items are purchased most frequently?
  - What is the relationship between price per unit and quantity purchased?
- **Payment and Location Analysis:**
  - Which payment method and location generate the highest total sales / usage frequency?
- **Customer Analysis:**
  - Which category has the highest number of unique customers?
  - Which customers have the highest total spending and transaction counts?
- **Time-Based & Quantity Analysis:**
  - How do sales and transactions change across years and months?
  - What is the distribution of purchased quantities?

## Dashboard Features
The Streamlit dashboard is titled **Retail Store Sales Dashboard** and provides:

### Sidebar Filters
Users can filter the dashboard by:
- Category
- Payment method
- Location
- Transaction year

### Key Metrics
Displays core metrics for the selected filters:
- Total sales
- Number of transactions
- Number of customers
- Average transaction value

### Dashboard Pages
- **Overview:** Sales by year, sales by month, and transaction counts across years.
- **Products:** Sales by category, average quantity by category, item sales, item quantity, and sales by price range.
- **Customers:** Top customers by total spending, customers by average spending, and number of customers by category.
- **Transactions:** Sales by payment method, location, and discount status.
- **Insights & Recommendations:** Project findings and analysis-based recommendations regarding sales performance, product performance, and customer engagement.

*Note: All charts are interactive Plotly visualizations rendered in Streamlit.*

## Key Insights
- **Butchers** has the highest total sales among categories, while **Milk Products** has the lowest.
- **Cash** is the leading payment method by sales and transaction count.
- **Online sales** are slightly higher than in-store sales.
- **Furniture** has the highest total quantity sold and number of transactions.
- **January** has the highest monthly sales and transaction count.
- Sales peak in **2024** and decline sharply in **2025** (which also contains fewer transactions).
- **Item_2_BEV** is the most frequently purchased item, while **Item_25_FUR** generates the highest total sales.
- **CUST_24** has the highest total spending and number of transactions.
- Transaction amounts are concentrated below 200 and show a right-skewed distribution.
- The analysis reports no clear relationship between price per unit and quantity purchased.

*Disclaimer: These findings describe patterns in the available dataset and should not be interpreted as causal conclusions.*

## Technologies & Tools
- Python 3.12+
- Pandas & NumPy
- Plotly
- Streamlit
- Jupyter Notebook (`nbformat`)
- `uv`, `Black`, `isort`

## Project Structure
```text
eda-mid-project/
├── data/
│   ├── retail_store_sales.csv
│   └── cleaned_df.csv
├── app.py
├── eda.ipynb
├── pyproject.toml
├── uv.lock
└── README.md
```
*(Note: `app.py` is generated in the notebook's Streamlit section and loads the cleaned dataset from `data/cleaned_df.csv`)*

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd eda-mid-project
   ```
   *(Replace `<repository-url>` with the repository's actual Git URL.)*

2. **Install dependencies:**
   This project uses `uv`:
   ```bash
   uv sync
   ```
   *(Requires Python 3.12 or later)*

3. **Run the Streamlit application:**
   ```bash
   uv run streamlit run app.py
   ```
   *If `app.py` has not yet been created, run the Streamlit section of `eda.ipynb` first. The notebook writes the application file and creates `data/cleaned_df.csv` during preprocessing.*

## Usage
1. Open the local Streamlit URL shown in the terminal.
2. Select a dashboard page from the sidebar.
3. Apply category, payment method, location, and year filters.
4. Review updated metrics and interactive charts.
5. Use the Insights and Recommendations pages to review the analysis findings.

## Future Improvements
- Add automated data-quality checks and validation tests.
- Improve the handling and documentation of incomplete transaction records.
- Add export functionality for filtered dashboard data.
- Add more detailed monthly and customer-retention analysis.
- Improve chart formatting and consistent sorting across dashboard visualizations.

## Author
Mostafa Khalil