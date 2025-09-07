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


# Question 2: What percentage of overall Sales do each of the categories contribute in 2019?




# Question 3: Which product category shows the widest price range of products?




# Question 4: Plot the Sales trend for iPhone on a Monthly basis.




# Question 5: For every city, list the products that have not yet been sold in that city.





# Question 6: List the top 3 cities in terms of the number of orders for each time of the day (Morning/Afternoon/Evening/Night).



# Question 7: Find the top 3 customers by Sales.
top_customers = sales_data.groupby('Purchase Address')['Sales'].sum().sort_values(ascending=False).head(3)
print("The top 3 customers by Sales:")
print(top_customers)


top_customers = sales_data.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(3)
print("The top 3 customers by Sales:")
print(top_customers)





