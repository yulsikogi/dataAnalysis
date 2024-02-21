import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv("../data/train_modified.csv")

# 성별에 따른 생존율 막대 그래프
# survival_by_gender = train_data.groupby('Sex')['Survived'].mean()
# survival_by_gender.plot(kind='bar')
# plt.title('Survival Rate by Gender')
# plt.show()

# Pclass별 생존율 계산
# survival_rate_pclass = train_data.groupby('Pclass')['Survived'].mean()
# survival_rate_pclass.plot(kind='bar', color='skyblue')
# plt.title('Survival Rate by Pclass')
# plt.xlabel('Pclass')
# plt.ylabel('Survival Rate')
# plt.xticks(rotation=0)
# plt.show()

# Cabin별 생존율 & 평균 요금 계산
# train_data['Cabin_First'] = train_data['Cabin'].apply(lambda x: x[0])

# survival_rate_cabin = train_data.groupby('Cabin_First')['Survived'].mean()
# average_fare_cabin = train_data.groupby('Cabin_First')['Fare'].mean()

# ## 막대 그래프 (생존율) 생성
# ax = survival_rate_cabin.plot(kind='bar', color='tomato', width=0.4)
# plt.title('Survival Rate and Average Fare by Cabin Section')
# plt.xlabel('Cabin Section')
# plt.ylabel('Survival Rate')
# plt.xticks(rotation=0)

# ## 선 그래프 (평균 요금) 생성
# average_fare_cabin.plot(kind='line', marker='o', secondary_y=True, ax=ax, color='blue')
# plt.ylabel('Average Fare')

# plt.show()

# 등석을 그룹으로 나눈 후 Cabin별 생존율 & 평균 요금 계산
train_data['Cabin_First'] = train_data['Cabin'].apply(lambda x: x[0])
grouped_data = train_data.groupby(['Pclass', 'Cabin_First'])
survival_rate = grouped_data['Survived'].mean()
average_fare = grouped_data['Fare'].mean()

# Pclass 개수만큼 서브플롯 생성
fig, axes = plt.subplots(nrows=train_data['Pclass'].nunique(), ncols=1, figsize=(10, 15))

# 각 Pclass에 대해 서브플롯 생성
for (pclass), ax in zip(train_data['Pclass'].unique(), axes.flatten()):
    pclass_data = survival_rate.xs(pclass, level='Pclass')
    pclass_fare_data = average_fare.xs(pclass, level='Pclass')

    # 막대 그래프 (생존율)
    pclass_data.plot(kind='bar', ax=ax, color='tomato', width=0.4, position=1)
    ax.set_title(f'Pclass {pclass} - Survival Rate and Average Fare')
    ax.set_xlabel('Cabin Section')
    ax.set_ylabel('Survival Rate')
    
    # 선 그래프 (평균 요금)
    pclass_fare_data.plot(kind='line', marker='o', secondary_y=True, ax=ax, color='blue')
    ax.right_ax.set_ylabel('Average Fare')

plt.tight_layout()
plt.show()
