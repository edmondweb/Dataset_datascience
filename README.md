README for Sales Data Analysis
==============================

This Python script analyzes sales data from a CSV file, "SalesDataAnalysis.csv". It processes the data to answer several business questions related to product sales, trends, and customer behaviors. The script utilizes **pandas**, **matplotlib**, and **seaborn** for data manipulation, analysis, and visualization.
Requirements

------------

* Python 3.x

* pandas

* numpy

* matplotlib

* seaborn

File Description
----------------

* **SalesDataAnalysis.csv**: This CSV file contains sales data including fields such as `Product`, `Sales`, `Price Each`, `Order Date`, `City`, `Customer_ID`, and more. Ensure that the dataset is available in the same directory as the script for it to work properly.

Key Sections of the Script
--------------------------

1. **Data Preprocessing**:
   
   * Cleans and converts the `Price Each` and `Sales` columns into numeric data, removing symbols like `$` and `,`.
   
   * Converts `Order Date` into a datetime format to facilitate time-based analysis.

2. **Analysis and Insights**:
   
   * **Revenue from Top 3 Product Categories**: Calculates total revenue generated from the top 3 product categories.
   
   * **Percentage of Overall Sales by Category in 2019**: Determines the contribution of each product category to the total sales in 2019.
   
   * **Widest Price Range by Category**: Identifies the product category with the widest range of prices.
   
   * **Monthly Sales Trend for iPhone**: Plots the sales trend for iPhone on a monthly basis.
   
   * **Products Not Sold in Each City**: Lists the products that have not been sold in each city.
   
   * **Top 3 Cities by Number of Orders**: Finds the top 3 cities by the number of orders for each time of day (Morning, Afternoon, Evening, Night).
   
   * **Top 3 Customers by Sales**: Identifies the top 3 customers by total sales, both by `Purchase Address` and `Customer_ID`.

Output
------

The script outputs the following:

* Revenue generated from the top 3 product categories.

* Percentage of overall sales for each product category in 2019.

* Product category with the widest price range.

* A line plot showing iPhone's sales trend on a monthly basis.

* A list of products that have not been sold in each city.

* The top 3 cities in terms of orders for different times of the day.

* The top 3 customers by total sales.

Plot
----

The script also generates a **line plot** showing the monthly sales trend for the iPhone, helping visualize sales performance over time.
Usage

Ensure the following before running the script:

* The `SalesDataAnalysis.csv` file is located in the same directory as the script.

* Required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`) are installed.

Run the script in a Python environment, and the outputs will be printed to the console and visualized as a plot.
