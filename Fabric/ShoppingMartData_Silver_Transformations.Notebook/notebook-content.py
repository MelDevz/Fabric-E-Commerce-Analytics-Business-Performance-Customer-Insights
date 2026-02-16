# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "5b6d38c6-406e-4bc9-ac91-8bad3492f404",
# META       "default_lakehouse_name": "ShoppingMart_Bronze_Layer",
# META       "default_lakehouse_workspace_id": "06059e2d-9ef8-435d-9b23-17f4de24aa9e",
# META       "known_lakehouses": [
# META         {
# META           "id": "5b6d38c6-406e-4bc9-ac91-8bad3492f404"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## SILVER Layer Notebook: Data Cleaning & Integration

# MARKDOWN ********************

# **Load Broze Data**

# CELL ********************

from pyspark.sql.functions import *

df_customers = spark.read.format("csv").option("header", "true").load("Files/ShoppingMart_Bronze_Customers/ShoppingMart_customers.csv")
df_orders = spark.read.format("csv").option("header", "true").load("Files/ShoppingMart_Bronze_Orders/ShoppingMart_orders.csv")
df_products = spark.read.format("csv").option("header", "true").load("Files/ShoppingMart_Bronze_Products/ShoppingMart_products.csv")
display(df_orders)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/ShoppingMart_Bronze_Customers/ShoppingMart_customers.csv")
# df now is a Spark DataFrame containing CSV data from "Files/ShoppingMart_Bronze_Customers/ShoppingMart_customers.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_orders = df_orders.dropna(subset = ["OrderID", "CustomerID", "ProductID", "OrderDate", "TotalAmount"])
df_orders = df_orders.withColumn("OrderDate", to_date(col("OrderDate")))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import *

df_customers = spark.read.format("csv").option("header", "true").load("Files/ShoppingMart_Bronze_Customers/ShoppingMart_customers.csv")
df_orders = spark.read.format("csv").option("header", "true").load("Files/ShoppingMart_Bronze_Orders/ShoppingMart_orders.csv")
df_products = spark.read.format("csv").option("header", "true").load("Files/ShoppingMart_Bronze_Products/ShoppingMart_products.csv")

df_orders = df_orders.dropna(subset = ["OrderID", "CustomerID", "ProductID", "OrderDate", "TotalAmount"])
df_orders = df_orders.withColumn("OrderDate", to_date(col("OrderDate")))

df_orders = df_orders \
     .join(df_customers, on = 'CustomerID', how="inner") \
     .join(df_products, on = "ProductID", how = "inner")

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_orders.write.mode("overwrite").parquet("Files/ShoppingMart_Bronze_Customers/ShoppingMart_customers_orderdata")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
