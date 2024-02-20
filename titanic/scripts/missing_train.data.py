import pandas as pd

train_data = pd.read_csv('../data/train.csv')

median_ages = train_data.groupby(['Pclass', 'Sex'])['Age'].median()

def fill_age(row):
    if pd.isna(row['Age']):
        return median_ages[row['Pclass'], row['Sex']]
    else:
        return row['Age']

train_data['Age'] = train_data.apply(fill_age, axis=1)

# Cabin 열에서 첫 글자 추출
train_data['Cabin_Section'] = train_data['Cabin'].apply(lambda x: x[0] if pd.notna(x) else 'Unknown')

# Cabin_Section별 평균 Fare 계산
average_fares = train_data.groupby(['Pclass', 'Cabin_Section'])['Fare'].mean().sort_index()

def assign_cabin(pclass, fare, average_fares):
    cabin_order = {
        1: ['B', 'C', 'D', 'E', 'A', 'T'],
        2: ['F', 'D', 'E'],
        3: ['G', 'E', 'F']
    }

    # Pclass에 해당하는 Cabin 순서 가져오기
    cabins = cabin_order[pclass]
    closest_cabin = 'Unknown'
    min_diff = float('inf')

    # 가장 가까운 평균 요금을 가진 Cabin 찾기
    for cabin in cabins:
        if (pclass, cabin) in average_fares:
            cabin_fare = average_fares[(pclass, cabin)]
            diff = abs(fare - cabin_fare)

            if diff < min_diff:
                min_diff = diff
                closest_cabin = cabin

    return closest_cabin

for index, row in train_data.iterrows():
    if pd.isna(row['Cabin']):
        assigned_cabin = assign_cabin(row['Pclass'], row['Fare'], average_fares)
        train_data.at[index, 'Cabin'] = assigned_cabin

print(train_data.isnull().sum())