import pandas as pd

ab_data = pd.read_csv("../data/AB_NYC_2019.csv")

# name과 host_name의 결측치를 'empty_data'로 대체.
ab_data['name'].fillna('empty_data', inplace=True)
ab_data['host_name'].fillna('empty_data', inplace=True)

# last_review의 결측치를 현재 날짜(2024년 2월 23일)로 대체.
ab_data['last_review'].fillna('2024-02-23', inplace=True)

# reviews_per_month의 결측치를 0으로 대체.
ab_data['reviews_per_month'].fillna(0, inplace=True)

print(ab_data.isna().sum())

# 결측치 처리한 데이터 파일화
# ab_data.to_csv("../data/AB_NYC_2019_modify.csv", index=False)