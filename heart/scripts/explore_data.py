import pandas as pd

heart_data = pd.read_csv('../data/heart.csv')

print(heart_data.info())
print(heart_data.head())
print(heart_data.describe())
print(heart_data.isnull().sum())
