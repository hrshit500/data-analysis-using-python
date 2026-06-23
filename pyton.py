# this part is for data cleaning
import pandas as pd
df = pd.read_csv('C:\\Users\\zeusq\\OneDrive\\Documents\\python project in data analyst\\Diwali Sales Data.csv', encoding= 'unicode_escape')
#  it shows size of column
# print(df.shape)  
# it throw information of column
# print(df.info())  
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True) 
# to print null value counted
# print(pd.isnull(df).sum())   
df['Amount'] = df['Amount'].astype('int')
df.rename(columns= {'Holla':'Marital_Status'},inplace=True)
# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
# print(df[['Age', 'Orders', 'Amount']].describe())

# this part is cover for showing chart with lots of calculation

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# for show a bar chart count of selected column
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
# for showing value in graph
for bars in ax.containers:
    ax.bar_label(bars)

# for checking who makes more with value
# sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# print(sales_gen)
# to show in graph form
# sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

# total number of orders from top 10 states
# sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

# sns.set(rc={'figure.figsize':(15,5)})
# sns.barplot(data = sales_state, x = 'State',y= 'Orders')
plt.show()