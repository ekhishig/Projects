# My Moto for 2025
print("Courage 2025")

# Importing Libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Importing data (Labour and Performance Indicators of Enterprises in Hungary in 2022)
df_path = os.path.join("Labour_and_performance_indicators_of_enterprises.csv")
df = pd.read_csv(df_path, delimiter=';', encoding='utf-8', index_col=0)

print("The first 5 rows of the dataset:", df.head())
print("Shape of the dataset:", df.shape)

# Renaming the index
df.index = df.index.str.split('-').str[1]
print("The first 5 rows of the dataset:", df.head())

# Creating a horizontal bar chart that shows the % of total enterprices by activity
df["Enterprise_Precentage"] = ((df[df.columns[0]]/df[df.columns[0]].sum()) * 100).round(2)
df_ent_perc = df["Enterprise_Precentage"].sort_values()
# plt.pie(df, labels=df.index, autopct='%1.1f%%')
plt.barh(df_ent_perc.index, df_ent_perc)
plt.yticks(fontsize=8)
plt.xlabel("%")
plt.title("Enterprises by activity in Hungary (2022)", fontweight='bold')
plt.tight_layout()
plt.show()

# Creating a horizontal bar chart that show the % of total wages and salaries by enterprise activity
print(df.columns)
df["Wages_Precentage"] = df["Wages and salaries (WAGE) (thousand HUF)"]/df['Number of employees in full-time equivalent units (SAL_FTE) (capita)']
df["Wages_Precentage"] = ((df["Wages_Precentage"]/df["Wages_Precentage"].sum()) * 100).round(2)
df_wage_perc = df["Wages_Precentage"].sort_values()
plt.barh(df_wage_perc.index, df_wage_perc)
plt.yticks(fontsize=8)
plt.xlabel("%")
plt.title("Average wages by enterprise activity in Hungary (2022)", fontweight='bold')
plt.tight_layout()
plt.show()


