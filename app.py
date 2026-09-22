
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Retail Store Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# =========================
# Load Data
# =========================

df = pd.read_csv("./data/cleaned_df.csv")

# =========================
# Header
# =========================

st.title("Retail Store Sales Dashboard")
st.caption("This dashboard provides an overview of retail store sales data")

st.divider()

# =========================
# Sidebar Filters
# =========================

st.sidebar.header("Filters")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Products",
        "Customers",
        "Transactions",
        "Insights",
        "Recommendations"
    ]
)

category = st.sidebar.multiselect(
    'Select Category:',
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

payment_method = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment Method"].unique(),
    default=df["Payment Method"].unique()
)

location = st.sidebar.multiselect(
    "Location",
    options=df["Location"].unique(),
    default=df["Location"].unique()
)

year = st.sidebar.multiselect(
    "Transaction Year",
    options=sorted(df["Transaction Year"].unique()),
    default=sorted(df["Transaction Year"].unique())
)

filtered_df = df[
    df["Category"].isin(category)
    & df["Payment Method"].isin(payment_method)
    & df["Location"].isin(location)
    & df["Transaction Year"].isin(year)
]

st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns([1.5,1,1,1.5])

col1.metric("Total Sales", f"${filtered_df['Total Spent'].sum():,.2f}")
col2.metric("Transactions", f"{len(filtered_df):,}")
col3.metric("Customers", filtered_df["Customer ID"].nunique())

avg_transaction_value = filtered_df["Total Spent"].mean()
avg_transaction_value = 0 if pd.isna(avg_transaction_value) else avg_transaction_value
col4.metric("Avg. Transaction Value", f"${avg_transaction_value:,.2f}")

st.divider()
##############################################################################################
if page == "Overview":
    st.subheader("Sales Overview")

    col1, col2 = st.columns(2)

    with col1:
        sales_by_year = (
            filtered_df
            .groupby("Transaction Year")["Total Spent"]
            .sum()
            .reset_index()
            .sort_values("Transaction Year")
        )

        fig = px.line(
            sales_by_year,
            x="Transaction Year",
            y="Total Spent",
            title="Sales by Year",
            markers=True
        )

        st.plotly_chart(fig)

    with col2:
        sales_by_month = (
            filtered_df
            .groupby("Transaction Month")["Total Spent"]
            .sum()
            .reset_index()
            .sort_values("Transaction Month")
        )

        fig = px.line(
            sales_by_month,
            x="Transaction Month",
            y="Total Spent",
            markers=True,
            title="Sales by Month"
        )

        st.plotly_chart(fig)

    st.divider()

    year_transactions = df["Transaction Year"].value_counts().sort_index()

    fig = px.line(
        x=year_transactions.index.astype(str),
        y=year_transactions.values,
        markers=True,
        labels={"x": "Transaction Year", "y": "Number of Transactions"},
        title="Number of Transactions Across Years",
    )

    st.plotly_chart(fig)

##############################################################################################
elif page == "Products":
    st.subheader("Product Analysis")

    col1, col2 = st.columns(2)

    with col1:
        sales_by_category = (
            filtered_df
            .groupby("Category")["Total Spent"]
            .sum()
            .reset_index()
            .sort_values(by="Total Spent", ascending=False)
        )

        fig = px.bar(
            sales_by_category,
            x="Total Spent",
            y="Category",
            orientation="h",
            title="Sales by Category"
        )

        st.plotly_chart(fig)

        avg_quantity_by_category = (
            filtered_df
            .groupby("Category")["Quantity"]
            .mean()
            .reset_index()
            .sort_values("Quantity", ascending=False)
        )

        fig = px.bar(
            avg_quantity_by_category,
            x="Quantity",
            y="Category",
            orientation = "h",
            title="Average Quantity by Category"
        )

        st.plotly_chart(fig)

    with col2:
        top_items = (
            filtered_df
            .groupby("Item")["Total Spent"]
            .sum()
            .head(10)
            .reset_index()
            .sort_values(by="Total Spent", ascending=False)
        )

        fig = px.bar(
            top_items,
            x="Total Spent",
            y="Item",
            orientation="h",
            title="Top 10 Items by Sales"
        )

        st.plotly_chart(fig)

        top_items_by_quantity = (
            filtered_df
            .groupby("Item")["Quantity"]
            .sum()
            .reset_index()
            .sort_values("Quantity", ascending=False)
            .head(10)
        )

        fig = px.bar(
            top_items_by_quantity,
            x="Quantity",
            y="Item",
            orientation="h",
            title="Top 10 Items by Quantity"
        )

        st.plotly_chart(fig)

    fig = px.histogram(
    filtered_df,
    x="Price Per Unit",
    y="Total Spent",
    title="Sales by Price Range",
    nbins=10
    )

    st.plotly_chart(fig)

##############################################################################################
elif page == "Customers":
    st.subheader("Customer Analysis")

    col1, col2 = st.columns(2)

    with col1:
        top_customers = (
            filtered_df
            .groupby("Customer ID")["Total Spent"]
            .sum()
            .reset_index()
            .sort_values("Total Spent", ascending=False)
            .head(10)
        )

        fig = px.bar(
            top_customers,
            x="Customer ID",
            y="Total Spent",
            title="Top 10 Customers by Total Spending"
        )

        st.plotly_chart(fig)

    with col2:
        avg_customer_spending = (
            filtered_df
            .groupby("Customer ID")["Total Spent"]
            .mean()
            .reset_index()
            .sort_values("Total Spent", ascending=False)
            .head(10)
        )

        fig = px.bar(
            avg_customer_spending,
            x="Customer ID",
            y="Total Spent",
            title="Top 10 Customers by Average Spending"
        )

        st.plotly_chart(fig)

    st.divider()

    customers_by_category = (
    filtered_df
    .groupby("Category")["Customer ID"]
    .nunique()
    .reset_index()
    .rename(columns={"Customer ID": "No. of Customers"})
    .sort_values("No. of Customers", ascending=False)
    )

    fig = px.bar(
        customers_by_category,
        x="No. of Customers",
        y="Category",
        orientation="h",
        title="No. of Customers by Category"
    )

    st.plotly_chart(fig)

##############################################################################################
elif page == "Transactions":
    col1, col2 = st.columns(2)

    with col1:
        payment_sales = (
            filtered_df
            .groupby("Payment Method")["Total Spent"]
            .sum()
            .reset_index()
            .sort_values("Total Spent", ascending=False)
        )

        fig = px.bar(
            payment_sales,
            x="Payment Method",
            y="Total Spent",
            title="Sales by Payment Method"
        )

        st.plotly_chart(fig)

    with col2:
        location_sales = (
            filtered_df
            .groupby("Location")["Total Spent"]
            .sum()
            .reset_index()
            .sort_values("Total Spent", ascending=False)
        )

        fig = px.pie(
            location_sales,
            names="Location",
            title="Sales by Location"
        )

        st.plotly_chart(fig)

    st.divider()

    discount_sales = (
        filtered_df
        .groupby("Discount Applied")["Total Spent"]
        .sum()
        .reset_index()
        .sort_values("Total Spent", ascending=False)
    )

    fig = px.pie(
        discount_sales,
        names="Discount Applied",
        title="Sales by Discount Status"
    )

    st.plotly_chart(fig)

##############################################################################################
elif page == "Insights":
    st.subheader("Sales Insights")

    st.markdown(
        """
        - Sales are relatively evenly distributed across product categories.
        - Cash generates the highest total sales among payment methods.
        - Sales vary across the transaction years, while 2025 contains fewer transactions than the previous years.
        - January records the highest monthly sales.
        """
    )

    st.subheader("Product Insights")

    st.markdown(
        """
        - Butchers has the highest total sales among categories.
        - Milk Products has the lowest total sales among categories.
        """
    )

    st.subheader("Customer Insights")

    st.markdown(
        """
        - CUST_24 has the highest number of transactions.
        - CUST_24 also has the highest total spending.
        - Customers are evenly distributed across product categories.
        """
    )

    st.subheader("Transaction Insights")

    st.markdown(
        """
        - January has the highest monthly sales.
        - Cash generates the highest total sales.
        - 2025 has fewer transactions than previous years.
        """
    )

##############################################################################################
if page == "Recommendations":
    st.subheader("Recommendations")

    st.markdown(
        """
        Based on the sales, products, customers analysis, the following actions can help improve performance.
        """
    )

    st.markdown("**Sales Recommendations**")

    st.markdown(
        """
        - Focus on increasing sales during months with lower performance.
        - Monitor 2025 sales separately because it contains fewer transactions.
        - Continue supporting cash payments while maintaining other payment methods.
        """
    )

    st.markdown("**Product Recommendations**")

    st.markdown(
        """
        - Promote Butchers products to maintain their strong sales performance.
        - Review Milk Products performance and consider targeted promotions.
        """
    )

    st.markdown("**Customer Recommendations**")

    st.markdown(
        """
        - Reward high-value customers such as CUST_24 with loyalty offers.
        """
    )
