import pandas as pd
import numpy as np

df = pd.read_csv('issues1.csv', index_col=None)
df['ItemCode'] = df['ItemCode'].str.strip()
df = df.loc[df['ItemCode'] == '01.01.007']
print(df)
df.to_excel("Issues1_to_date.xlsx", index = False, header=True)

df1 = pd.read_csv('Goods Receiving1.csv', index_col=None)
df1['ItemCode'] = df1['ItemCode'].str.strip()
df1 = df1.loc[df1['ItemCode'] == '01.01.007']
print(df1)
df1.to_excel("Goods Receiving1_to_date.xlsx", index = False, header=True)

df2 = pd.read_csv('Stock adjustment1.csv', index_col=None)
df2['ItemCode'] = df2['ItemCode'].str.strip()
df2 = df2.loc[df2['ItemCode'] == '01.01.007']
print(df2)
df2.to_excel("Stock adjustment1_to_date.xlsx", index = False, header=True)

df3 = pd.read_csv('stocks1.csv', index_col=None)
df3['ItemCode'] = df3['ItemCode'].str.strip()
df3 = df3.loc[df3['ItemCode'] == '01.01.007']
print(df3)
df3.to_excel("stocks1_to_date.xlsx", index = False, header=True)

