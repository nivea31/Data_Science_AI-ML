import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df=pd.read_csv("sales_data_large.csv")

# Task 1: Calculate the total sales for each product and rank the products based on sales performance.
total_sales=df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(total_sales)

# Task 2: Find the region with the highest total sales and the region with the lowest sales.
sales=df.groupby("Region")["Sales"].sum()
highest_total_sales=sales.idxmax()
print("Highest total sales-",highest_total_sales)
lowest_total_sales=sales.idxmin()
print("Lowest total sales-",lowest_total_sales)

# Task 3: Determine the product with the highest profit margin (profit as a percentage of sales) and compare it with the lowest profit margin product.
df["Profit Margin"]=(df["Profit"]/df["Sales"])*100

profit=df.groupby("Product")["Profit Margin"].sum()
highest_profit=profit.idxmax()
print("Highest profit margin-",highest_profit)
lowest_profit=profit.idxmin()
print("Lowest profit margin-",lowest_profit)

# Task 4: Identify the product that contributes the most to the total profit and the product with the lowest profit contribution.
product_contri=df.groupby("Product")["Profit"].sum()
highest_product_contri=product_contri.idxmax()
print("Highest product contri-",highest_product_contri)
lowest_product_contri=product_contri.idxmin()
print("Lowest product contri-",lowest_product_contri)

# Task 5: Create a new column Revenue assuming the profit is 20% of the revenue and compare revenue per product.
df["Revenue"]=df["Profit"]/0.2 #(20% of profit)
print(df)
revenue=df.groupby("Product")["Revenue"].sum()
print(revenue)

# Task 6: Sort the sales data by profit in descending order and display the top 3 most profitable sales transactions.
sales_sort=df.sort_values("Profit",ascending=False).head(3)
print(sales_sort)

# Task 7: Find the total sales and total profit for each region and visualize this using a pie chart.
region_sales=df.groupby("Region")["Sales"].sum()
print(region_sales)
region_profit=df.groupby("Region")["Profit"].sum()
print(region_profit)

# fig,axes=plt.subplots(1,2)
# axes[0].pie(region_sales,labels=region_sales.index,autopct="%.2f%%")
# axes[1].pie(region_profit,labels=region_profit.index,autopct="%.2f%%")
#plt.show()

# Task 8: Identify regions where the total profit is below the average profit and suggest potential strategies to improve sales.
avg_profit=df["Profit"].mean()
print("Average Profit-",avg_profit)
total_profit=df.groupby("Region")["Profit"].sum()
print("Total Profit-",total_profit)
print(total_profit<=avg_profit)

# Task 9: Calculate the percentage contribution of each product to total sales and display the top 3 highest contributing products.
total_sales1=df["Sales"].sum()
print(total_sales1)
df["Percentage Contribution"]=(df["Sales"]/total_sales1)*100
print(df)
high_product_contri=df.groupby("Product")["Percentage Contribution"].sum().sort_values(ascending=False).head(3)
print(high_product_contri)

# Task 10: Create a grouped bar chart to compare total sales and total profit for each product using Matplotlib or Seaborn.
product_total_profit=df.groupby("Product")["Profit"].sum()
#print(product_total_profit)
product_total_sales=df.groupby("Product")["Sales"].sum()
#print(product_total_sales)
product=np.arange(len(df["Product"].unique()))
#print(product)
barwidth=0.15

plt.bar(product,product_total_profit,width=barwidth,label="Total Profit")
plt.bar(product+0.15,product_total_sales,width=barwidth,label="Total Sales")
plt.legend()
plt.xlabel("Product")
plt.ylabel("Amount")
plt.title("Total Sales and Total Profit by Product")
plt.legend()
plt.show()