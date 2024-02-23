import pandas as pd

ab_data = pd.read_csv("../data/AB_NYC_2019.csv")

print(ab_data.info())
print(ab_data.head())
print(ab_data.describe())
print(ab_data.isnull().sum())