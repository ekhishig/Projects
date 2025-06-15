import pandas as pd
import os
import sqlite3
import matplotlib.pyplot as plt

df_path = os.path.join("NSO", "Number of Livestocks.xlsx")
df = pd.read_excel(df_path, header=0)

print(df.head())

# Connect to SQLite database
conn = sqlite3.connect(":memory:")  # Use ':memory:' for in-RAM db

# Save DataFrame to the database
df.to_sql("my_table", conn, index=False)

# query_result = pd.read_sql(
#     "SELECT * FROM my_table WHERE livestock = 'Goat' ORDER BY year ASC", conn
# )

# # print(query_result)

# # Creating a line graph showing the number of goat in Mongolia 
# plt.plot(query_result['year'], (query_result['amount'] / 1e3), color='black')
# plt.xlabel('Year')
# plt.ylabel('Goats (in millions)')
# plt.title('Total Number of Goats by Year in Mongolia')
# plt.show()

# livestock_types = pd.read_sql("SELECT DISTINCT livestock FROM my_table", conn)
# for livestock in livestock_types['livestock']:
#     result = pd.read_sql(
#         f"SELECT * FROM my_table WHERE livestock = '{livestock}' ORDER BY year ASC",
#         conn
#     )
#     print(f"Results for {livestock}:\n", result)


# Load all livestock data
df = pd.read_sql("SELECT * FROM my_table", conn)

# Pivot the data to get one column per livestock type
pivot_df = df.pivot(index='year', columns='livestock', values='amount')
pivot_df = pivot_df / 1e3

# Plot each livestock as a line
ax = pivot_df.plot(kind='line')

plt.title("Livestock Amount Over Years in Mongolia")
plt.xlabel("Year")
plt.ylabel("Amount (Millions)")
plt.legend(title="Livestock Type")
plt.tight_layout()
plt.figtext(0.9, 0.01, 'Data source: National Statistics Office of Mongolia', ha='right', fontsize=10, color='gray')
plt.show()