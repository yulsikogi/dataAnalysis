import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import numpy as np

ab_data = pd.read_csv("../data/AB_NYC_2019_modify.csv")
nyc_map_img = mpimg.imread('../public/images/New_York_City_.png', format='JPG')

# neighbourhood_group에 따라 색상을 다르게 하여 지도에 표시합니다.
# 각 그룹에 대해 다른 색상을 지정합니다.
# colors = {
#     'Bronx': 'green', 
#     'Brooklyn': 'blue', 
#     'Manhattan': 'red', 
#     'Queens': 'orange', 
#     'Staten Island': 'purple'
# }

# # 색상을 할당합니다.
# ab_data['color'] = ab_data['neighbourhood_group'].apply(lambda x: colors[x])

# # 범례를 추가하기 위해 neighbourhood_group 별로 데이터를 분리하여 그래프에 추가합니다.
# plt.figure(figsize=(10,10))
# plt.imshow(nyc_map_img, extent=[-74.258, -73.7, 40.49, 40.92]) # 지도의 경계를 설정합니다.

# # 각 neighbourhood_group 별로 점을 찍어서 범례에 사용할 수 있게 합니다.
# for group, color in colors.items():
#     subset = ab_data[ab_data['neighbourhood_group'] == group]
#     plt.scatter(subset['longitude'], subset['latitude'], zorder=1, alpha=0.5, c=color, s=5, label=group)

# plt.title('Airbnb Listings in NYC by Neighbourhood Group')
# plt.legend(title='Neighbourhood Group')
# plt.xticks([])
# plt.yticks([])

# plt.show()

# # neighbourhood_group 별로 숙소의 개수를 계산합니다.
# neighbourhood_group_counts = ab_data['neighbourhood_group'].value_counts().sort_index()

# # neighbourhood_group 별 평균 가격을 계산합니다.
# neighbourhood_group_prices = ab_data.groupby('neighbourhood_group')['price'].mean().sort_index()

# # 막대그래프 위에 선 그래프를 추가합니다.
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # 막대그래프 (숙소 개수)
# ax1.bar(neighbourhood_group_counts.index, neighbourhood_group_counts.values, color=[colors[group] for group in neighbourhood_group_counts.index], alpha=0.6, label='Number of Listings')
# ax1.set_xlabel('Neighbourhood Group')
# ax1.set_ylabel('Number of Listings')
# ax1.tick_params(axis='y')
# ax1.set_title('Number of Airbnb Listings and Average Price by Neighbourhood Group in NYC')

# # 선 그래프 (평균 가격)
# ax2 = ax1.twinx()  # x축을 공유하는 새로운 축을 생성합니다.
# ax2.plot(neighbourhood_group_prices.index, neighbourhood_group_prices.values, 'r-', lw=2, label='Average Price')
# ax2.set_ylabel('Average Price ($)')
# ax2.tick_params(axis='y', labelcolor='red')

# # 범례
# fig.tight_layout()
# ax1.legend(loc='upper left')
# ax2.legend(loc='upper right')
# plt.show()

price_bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, np.max(ab_data['price'])]
price_bin_labels = ['0-50', '51-100', '101-150', '151-200', '201-250', '251-300', '301-350', '351-400', '401-450', '451-500', '500+']
ab_data['price_group'] = pd.cut(ab_data['price'], bins=price_bins, labels=price_bin_labels, include_lowest=True)

# 가격대별로 색상을 지정합니다.
price_colors = {
    '0-50': 'blue',
    '51-100': 'green',
    '101-150': 'yellow',
    '151-200': 'orange',
    '201-250': 'red',
    '251-300': 'purple',
    '301-350': 'brown',
    '351-400': 'pink',
    '401-450': 'grey',
    '451-500': 'olive',
    '500+': 'cyan'
}

# 색상을 할당합니다.
ab_data['price_color'] = ab_data['price_group'].apply(lambda x: price_colors[x])

plt.figure(figsize=(10,10))
plt.imshow(nyc_map_img, extent=[-74.258, -73.7, 40.49, 40.92]) # 지도의 경계를 설정합니다.
plt.scatter(ab_data['longitude'], ab_data['latitude'], zorder=1, alpha=0.5, c=ab_data['price_color'], s=5)

# 범례를 위한 핸들러를 생성합니다.
legend_handles = [mpatches.Patch(color=color, label=label) for label, color in price_colors.items()]

# 범례를 추가합니다.
plt.legend(handles=legend_handles, title='Price Range ($)', loc='upper right', bbox_to_anchor=(1.25, 1))

plt.title('Airbnb Listings in NYC by Price Range')
plt.xticks([])
plt.yticks([])
plt.show()