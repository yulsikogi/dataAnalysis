import pandas as pd

test_data = pd.read_csv('../data/test.csv')

print(test_data.head())
print(test_data.info())
print(test_data.describe())
