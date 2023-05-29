import pandas as pd

csv_data = pd.read_csv('shopping_data_missingvalue.csv')
#print(csv_data)

mean = csv_data['Age'].mean()
mean2 = csv_data['Annual Income (k$)'].mean()
mean3 = csv_data['Spending Score (1-100)'].mean()
setdata = csv_data.fillna ({'Age':mean, 'Annual Income (k$)': mean2, 'Spending Score (1-100)':mean3})
print(setdata)