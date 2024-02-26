import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

heart_data = pd.read_csv('../data/heart.csv')


# 1
# Separating the data for plotting
# custom_colors = ['#FF5733', '#33FF57', '#3357FF']
# mean_values = heart_data.groupby(['Sex', 'HeartDisease']).agg({'RestingBP':'mean', 'Cholesterol':'mean', 'FastingBS':'mean', 'MaxHR':'mean'}).reset_index()

# male_with_hd = mean_values[(mean_values['Sex'] == 'M') & (mean_values['HeartDisease'] == 1)]
# male_without_hd = mean_values[(mean_values['Sex'] == 'M') & (mean_values['HeartDisease'] == 0)]
# female_average = mean_values[mean_values['Sex'] == 'F'].groupby('Sex').mean().reset_index()

# # Creating a new dataframe for easy plotting
# plot_data = pd.concat([male_with_hd, male_without_hd, female_average])
# plot_data['Group'] = ['Male with HD', 'Male without HD', 'Average Female']

# # Setting up the figure for subplots
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

# # RestingBP
# sns.barplot(x='Group', y='RestingBP', data=plot_data, ax=axes[0, 0], palette=custom_colors)
# axes[0, 0].set_title('Average RestingBP')
# axes[0, 0].set_ylabel('RestingBP')

# # Cholesterol
# sns.barplot(x='Group', y='Cholesterol', data=plot_data, ax=axes[0, 1], palette=custom_colors)
# axes[0, 1].set_title('Average Cholesterol')
# axes[0, 1].set_ylabel('Cholesterol')

# # FastingBS
# sns.barplot(x='Group', y='FastingBS', data=plot_data, ax=axes[1, 0], palette=custom_colors)
# axes[1, 0].set_title('Average FastingBS')
# axes[1, 0].set_ylabel('FastingBS')

# # MaxHR
# sns.barplot(x='Group', y='MaxHR', data=plot_data, ax=axes[1, 1], palette=custom_colors)
# axes[1, 1].set_title('Average MaxHR')
# axes[1, 1].set_ylabel('MaxHR')

# # Adjust layout and show plot
# plt.tight_layout()
# plt.show()

# 2, 3
# Creating subsets for each group
# male_hd = heart_data[(heart_data['Sex'] == 'M') & (heart_data['HeartDisease'] == 1)]
# male_no_hd = heart_data[(heart_data['Sex'] == 'M') & (heart_data['HeartDisease'] == 0)]
# female_hd = heart_data[(heart_data['Sex'] == 'F') & (heart_data['HeartDisease'] == 1)]
# female_no_hd = heart_data[(heart_data['Sex'] == 'F') & (heart_data['HeartDisease'] == 0)]

# 2
# Counting ChestPainType for each group
# male_hd_cpt = male_hd['ChestPainType'].value_counts()
# male_no_hd_cpt = male_no_hd['ChestPainType'].value_counts()
# female_hd_cpt = female_hd['ChestPainType'].value_counts()
# female_no_hd_cpt = female_no_hd['ChestPainType'].value_counts()

# Setting up the figure for the subplots
# fig, axes = plt.subplots(2, 2, figsize=(14, 14))

# # Pie charts for each group
# axes[0, 0].pie(male_hd_cpt, labels=male_hd_cpt.index, autopct='%1.1f%%', startangle=140)
# axes[0, 0].set_title('Chest Pain Type in Males with Heart Disease')

# axes[0, 1].pie(male_no_hd_cpt, labels=male_no_hd_cpt.index, autopct='%1.1f%%', startangle=140)
# axes[0, 1].set_title('Chest Pain Type in Males without Heart Disease')

# axes[1, 0].pie(female_hd_cpt, labels=female_hd_cpt.index, autopct='%1.1f%%', startangle=140)
# axes[1, 0].set_title('Chest Pain Type in Females with Heart Disease')

# axes[1, 1].pie(female_no_hd_cpt, labels=female_no_hd_cpt.index, autopct='%1.1f%%', startangle=140)
# axes[1, 1].set_title('Chest Pain Type in Females without Heart Disease')

# # Adjust layout and show plot
# plt.tight_layout()
# plt.show()

# Counting RestingECG for each group
# male_hd_ecg = male_hd['RestingECG'].value_counts()
# male_no_hd_ecg = male_no_hd['RestingECG'].value_counts()
# female_hd_ecg = female_hd['RestingECG'].value_counts()
# female_no_hd_ecg = female_no_hd['RestingECG'].value_counts()

# # Setting up the figure for the subplots
# fig, axes = plt.subplots(2, 2, figsize=(14, 14))

# # Pie charts for RestingECG in each group
# axes[0, 0].pie(male_hd_ecg, labels=male_hd_ecg.index, autopct='%1.1f%%', startangle=140)
# axes[0, 0].set_title('Resting ECG in Males with Heart Disease')

# axes[0, 1].pie(male_no_hd_ecg, labels=male_no_hd_ecg.index, autopct='%1.1f%%', startangle=140)
# axes[0, 1].set_title('Resting ECG in Males without Heart Disease')

# axes[1, 0].pie(female_hd_ecg, labels=female_hd_ecg.index, autopct='%1.1f%%', startangle=140)
# axes[1, 0].set_title('Resting ECG in Females with Heart Disease')

# axes[1, 1].pie(female_no_hd_ecg, labels=female_no_hd_ecg.index, autopct='%1.1f%%', startangle=140)
# axes[1, 1].set_title('Resting ECG in Females without Heart Disease')

# # Adjust layout and show plot
# plt.tight_layout()
# plt.show()

grouped_data = heart_data.groupby(['Sex', 'HeartDisease', 'ChestPainType']).agg({'FastingBS':'mean'}).reset_index()

# Adding a new column to identify groups
grouped_data['Group'] = grouped_data['Sex'] + ' ' + grouped_data['HeartDisease'].map({0: 'without HD', 1: 'with HD'})

# Setting up the figure for the plot
plt.figure(figsize=(15, 6))

# Bar plot for average FastingBS by group and RestingECG
sns.barplot(x='Group', y='FastingBS', hue='ChestPainType', data=grouped_data, palette='Set2', ci=None, estimator=np.mean)
plt.title('Average FastingBS by ChestPainType in Each Group')
plt.xlabel('Group')
plt.ylabel('Average FastingBS')
plt.legend(title='ChestPainType', loc='upper right')

# Show plot
plt.show()