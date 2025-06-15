# My Moto for 2025
print("Courage 2025")

# Importing Libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
# import csv

# Importing data (Labour and Performance Indicators of Enterprises in Hungary in 2022)
df_path = os.path.join("Labour_and_performance_indicators_of_enterprises.csv")
df = pd.read_csv(df_path, delimiter=';', encoding='utf-8', index_col=0)

# Importing csv using csv library will return rows as lists
# with open(df_path, newline='', encoding='utf-8') as csvfile:
#     df = csv.reader(csvfile)

print("The first 5 rows of the dataset:", df.head())
print("Shape of the dataset:", df.shape)

# Renaming the index
df.index = df.index.str.split('-').str[1]
print("The first 5 rows of the dataset:", df.head())

# Creating a horizontal bar chart that shows the % of total enterprices by activity
df['Enterprise_Precentage'] = ((df[df.columns[0]] / df[df.columns[0]].sum()) * 100).round(2)
df_ent_perc = df['Enterprise_Precentage'].sort_values()
plt.barh(df_ent_perc.index, df_ent_perc)
plt.yticks(fontsize=8)
plt.xlabel("%")
plt.title("Enterprises by activity in Hungary (2022)", fontweight='bold')
plt.tight_layout()
plt.show()

# Creating a horizontal bar chart that shows the % of total wages and salaries by enterprise activity
print(df.columns)
df['Wage_per_capita'] = df['Wages and salaries (WAGE) (thousand HUF)'] / df['Number of employees in full-time equivalent units (SAL_FTE) (capita)']
df['Wages_Precentage'] = ((df['Wage_per_capita']/df['Wage_per_capita'].sum()) * 100).round(2)
df_wage_perc = df['Wages_Precentage'].sort_values()
fig, ax = plt.subplots()
ax.barh(df_wage_perc.index, df_wage_perc)
plt.yticks(fontsize=8)
plt.xlabel("%")
plt.title("Average wages by enterprise activity in Hungary (2022)", fontweight='bold')
plt.tight_layout()
plt.show()

# Creating a horizontal bar chart that shows the monthly gross average wages and salaries by enterprise activity
df['Wage_per_capita'] = ((df['Wages and salaries (WAGE) (thousand HUF)'] / df['Number of employees in full-time equivalent units (SAL_FTE) (capita)']) / 12).round(2)
df_wage_per_capita = df['Wage_per_capita'] .sort_values()
fig, ax = plt.subplots()
ax.barh(df_wage_per_capita.index, df_wage_per_capita)
country_avg_wages = ((df['Wages and salaries (WAGE) (thousand HUF)'].sum() / df['Number of employees in full-time equivalent units (SAL_FTE) (capita)'].sum()) / 12).round(2)
print(country_avg_wages)
ax.axvline(country_avg_wages,  color='red', linestyle='--', label='Country average')
plt.yticks(fontsize=8)
plt.xlabel("Thousand HUF")
plt.title("Average gross monthly wages by Enterprise activity in Hungary (2022)", fontweight='bold')
ax.legend()
fig.text(0.95, 0.01, 'Source: Hungarian Central Statistical Office (KSH)', 
         ha='right', va='bottom', fontsize=10, color='gray')
plt.tight_layout()
plt.show()

# Creating a horizontal bar chart that shows the average monthly working hours by enterprise activity
df['Hours_per_employee_month'] = ((df['Hours worked by employees (HOWK) (hours)'] / df['Number of employees in full-time equivalent units (SAL_FTE) (capita)']) / 12).round(2)
df_hours_per_employee = df['Hours_per_employee_month'].sort_values()
plt.barh(df_hours_per_employee.index, df_hours_per_employee)
plt.xlabel("Hours")
plt.title("Average monthly working hours by Enterprise activity in Hungary (2022)")
plt.show()

