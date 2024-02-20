import pandas as pd

train_data = pd.read_csv('../data/train.csv')

print(train_data.head())
print(train_data.info())
print(train_data.describe())
