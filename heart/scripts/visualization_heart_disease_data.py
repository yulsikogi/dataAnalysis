import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

heart_data = pd.read_csv('../data/heart.csv')

# 1. Age plot
# Creating age bins
bins = np.arange(20, heart_data['Age'].max() + 10, 10)
heart_data['AgeGroup'] = pd.cut(heart_data['Age'], bins, right=False)

# Creating a count plot for AgeGroup with hue as HeartDisease
# plt.figure(figsize=(10, 6))
# sns.countplot(x='AgeGroup', hue='HeartDisease', data=heart_data)
# plt.title('Heart Disease Frequency for Age Groups')
# plt.xlabel('Age Group')
# plt.ylabel('Frequency')
# plt.legend(title='Heart Disease', labels=['No', 'Yes'])
# plt.xticks(rotation=45)
# plt.show()

# # 2. Sex plot
# # Creating a count plot for Sex with hue as HeartDisease
# plt.figure(figsize=(10, 6))
# sns.countplot(x='Sex', hue='HeartDisease', data=heart_data)
# plt.title('Heart Disease Frequency by Sex')
# plt.xlabel('Sex')
# plt.ylabel('Frequency')
# plt.legend(title='Heart Disease', labels=['No', 'Yes'])
# plt.show()

# # 3. HeartDisease plot
# # Pie chart for overall HeartDisease presence
# heart_disease_counts = heart_data['HeartDisease'].value_counts()

# # Creating the pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(heart_disease_counts, labels=['No Heart Disease', 'Heart Disease'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
# plt.title('Proportion of Individuals with and without Heart Disease')
# plt.show()

# 4. 
# Creating separate dataframes for males and females
male_data = heart_data[heart_data['Sex'] == 'M']
female_data = heart_data[heart_data['Sex'] == 'F']

# Setting up the figure for the subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

# Plot for Males
sns.countplot(x='AgeGroup', hue='HeartDisease', data=male_data, ax=axes[0])
axes[0].set_title('Heart Disease Frequency for Age Groups in Males')
axes[0].set_xlabel('Age Group')
axes[0].set_ylabel('Frequency')
axes[0].legend(title='Heart Disease', labels=['No', 'Yes'])
axes[0].tick_params(axis='x', rotation=45)

# Plot for Females
sns.countplot(x='AgeGroup', hue='HeartDisease', data=female_data, ax=axes[1])
axes[1].set_title('Heart Disease Frequency for Age Groups in Females')
axes[1].set_xlabel('Age Group')
axes[1].set_ylabel('Frequency')
axes[1].legend(title='Heart Disease', labels=['No', 'Yes'])
axes[1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()
plt.show()
