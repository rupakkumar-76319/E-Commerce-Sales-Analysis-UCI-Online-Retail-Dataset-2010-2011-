import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import calendar

# Data Loading and intial exploration.........................
df=pd.read_excel("Data/Online_Retail.xlsx")
# print(df)
# print("-------------------------------------This is Shape (rows, Column)-------------------------------------\n",df.shape)
# print("--------------------------------------------------------- Name of the Columns ------------------------------------------------\n",df.columns)
# print(f"-------------------------------------This is the top five rows in the Data Frame------------------------------------- \n",df.head())
# print("-------------------------------------This is the last five rows in the Data Frame------------------------------------- \n",df.tail())
# print("-------------------------------------This is te INFO-------------------------------------")
# df.info()
# print("-------------------------------------------------------------Describe the Data-------------------------------------------------------------\n",df.describe)

# Data Cleaning 
# Just convert to float to string of CustomerID
df['CustomerID']=df['CustomerID'].astype(str)
# print(df.info())

# Add the new column Day, Month and Year
df['Day']=df['InvoiceDate'].dt.day_name()
df['Month']=df['InvoiceDate'].dt.month_name()
df['Year']=df['InvoiceDate'].dt.year
print("--------------------------------------------------------- Name of the Columns ------------------------------------------------\n",df.columns)

# Checking Null or not
print("-------------------------------------Checking Missing Value-------------------------------------\n")
print(df.isnull().sum())
print("-------------------------------------Fill the Unknown-------------------------------------\n")
df=df.fillna("There is no need to describe.")
print(df.isnull().sum())
print(df[df.duplicated()])
print("------------------------------------- remove the Duplicate -------------------------------------")
df = df.drop_duplicates(keep='first')
print(df.duplicated().sum())




df.info()
# print(df.describe)