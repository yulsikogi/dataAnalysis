import pandas as pd

train_data = pd.read_csv('../data/train.csv')
test_data = pd.read_csv('../data/test.csv')
gender_submission = pd.read_csv('../data/gender_submission.csv')

print(train_data.head())
print(train_data.info())
print(train_data.describe())
