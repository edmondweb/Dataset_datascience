import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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
# Filter iPhone Data
iphone_sales = sales_data[sales_data['Product'] == 'iPhone'].copy()
# Convert 'Order Date' to datetime
iphone_sales['Order Date'] = pd.to_datetime(iphone_sales['Order Date'], format='%d-%m-%Y %H:%M')

# Extract Year and Month
iphone_sales['Year_Month'] = iphone_sales['Order Date'].dt.to_period('M')

# Group by Year_Month and Sum Sales
monthy_iphone_sales = iphone_sales.groupby('Year_Month')['Sales'].sum()

# Plot the Sales trend for iPhone on a Monthly basis
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthy_iphone_sales.index.astype(str), y=monthy_iphone_sales.values)
plt.xlabel('Year_Month')
plt.ylabel('Sales')
plt.title('Sales trend for iPhone on a Monthly basis')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Question 5: For every city, list the products that have not yet been sold in that city.
# Get all unique products and cities

all_products = sales_data['Product'].unique()
all_cities = sales_data['City'].unique()

# Create a dictionary to store products not sold in each city
products_not_sold_by_city = {}

# Iterate through each city
for city in all_cities:
    # Get the products sold in the current city
    products_sold_in_city = sales_data[sales_data['City'] == city]['Product'].unique()
    
    # Find products that are in all_products but not in the product_sold_in_city
    products_not_sold = set(all_products) - set(products_sold_in_city)
    
    # Store the products not sold in the current city
    products_not_sold_by_city[city] = list(products_not_sold)
    
# Print the results
for city, products in products_not_sold_by_city.items():
    print(f"Products not sold in {city}:")
    if products:
        for product in products:
            print(f"- {product}")
    else:
        print("- All products have been sold in this city.")
    
    print("-" * 30)
    



# Question 6: List the top 3 cities in terms of the number of orders for each time of the day (Morning/Afternoon/Evening/Night).
# Group by Time of Day and City, and count the number of orders
city_orders_by_time = sales_data.groupby(['Time of Day', 'City']).size().reset_index(name='Number of Orders')

# Get the top 3 cities for each Time of Day
top_cities_by_time = city_orders_by_time.groupby('Time of Day').apply(lambda x: x.nlargest(3, 'Number of Orders')).reset_index(drop=True)

# Print the results
print("Top 3 cities by number of orders for each time of the day:")
print(top_cities_by_time)


# Question 7: Find the top 3 customers by Sales per Purchase Address 
top_customers = sales_data.groupby('Purchase Address')['Sales'].sum().sort_values(ascending=False).head(3)
print("The top 3 customers by Sales:")
print(top_customers)

# Top 3 customers by sales per customer id
top_customers = sales_data.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(3)
print("The top 3 customers by Sales:")
print(top_customers)





