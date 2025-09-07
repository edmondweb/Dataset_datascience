import pandas as pd
import numpy as np


# Importing the dataset
sales_data = pd.read_csv("SalesDataAnalysis.csv")

sales_data.head()
print(sales_data.head())


# Question 1: How much revenue was generated from the three top-selling product categories?

# Convert 'Price Each' and 'Sales' to numeric, handling errors and cleaning
sales_data['Price Each'] = sales_data['Price Each'].astype(str).str.replace('[$,]', '', regex=True)
sales_data['Price Each'] = pd.to_numeric(sales_data['Price Each'], errors='coerce')

sales_data['Sales'] = sales_data['Sales'].astype(str).str.replace('[$,]', '', regex=True)
sales_data['Sales'] = pd.to_numeric(sales_data['Sales'], errors='coerce')


# Calculate total revenue for each product category
category_revenue = sales_data.groupby('Product Category')['Sales'].sum()

# Get the top 3 product categories by sales
top_3_categories_revenue = category_revenue.sort_values(ascending=False).head(3)

# Print the result
print("Revenue generated from the three top-selling product categories:")
print(top_3_categories_revenue)









