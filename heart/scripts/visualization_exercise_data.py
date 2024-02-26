import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

heart_data = pd.read_csv('../data/heart.csv')

# 1
# Creating a count plot for HeartDisease vs ExerciseAngina
# plt.figure(figsize=(10, 6))
# sns.countplot(x='HeartDisease', hue='ExerciseAngina', data=heart_data)
# plt.title('Exercise Induced Angina vs Heart Disease')
# plt.xlabel('Heart Disease')
# plt.ylabel('Count')
# plt.legend(title='Exercise Induced Angina', labels=['No', 'Yes'])
# plt.show()

# 2
# Creating a box plot for HeartDisease vs Oldpeak
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='HeartDisease', y='Oldpeak', data=heart_data)
# plt.title('Oldpeak vs Heart Disease')
# plt.xlabel('Heart Disease')
# plt.ylabel('Oldpeak')
# plt.show()

# 3
# Counting ST_Slope for each HeartDisease status
slope_colors = {'Up': '#66b3ff', 'Flat': '#ff9999', 'Down': '#99ff99'}
hd_st_slope = heart_data[heart_data['HeartDisease'] == 1]['ST_Slope'].value_counts()
no_hd_st_slope = heart_data[heart_data['HeartDisease'] == 0]['ST_Slope'].value_counts()

# Setting up the figure for the subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Pie charts for ST_Slope in each HeartDisease status
axes[0].pie(hd_st_slope, labels=hd_st_slope.index, autopct='%1.1f%%', startangle=140, colors=[slope_colors[slope] for slope in hd_st_slope.index])
axes[0].set_title('ST Slope in Individuals with Heart Disease')

axes[1].pie(no_hd_st_slope, labels=no_hd_st_slope.index, autopct='%1.1f%%', startangle=140, colors=[slope_colors[slope] for slope in no_hd_st_slope.index])
axes[1].set_title('ST Slope in Individuals without Heart Disease')

# Adjust layout and show plot
plt.tight_layout()
plt.show()
