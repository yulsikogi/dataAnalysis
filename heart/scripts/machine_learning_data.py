import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np


heart_data = pd.read_csv('../data/heart.csv')

heart_data_encoded = pd.get_dummies(heart_data)

features = [
    'Age', 'FastingBS', 'Oldpeak', 'Sex_F', 'Sex_M',
    'ExerciseAngina_N', 'ExerciseAngina_Y', 'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up'
]
selected_data = heart_data_encoded[features]

# 타겟 변수 분리
X = selected_data  
y = heart_data_encoded['HeartDisease']

# 데이터를 훈련 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. 랜덤 포레스트 모델 생성 - 과적합(Overfitting)
# 하이퍼파라미터 수정 전
# 훈련 세트 정확도: 0.9822888283378747
# 테스트 세트 정확도: 0.7391304347826086
# 수정 후
# 훈련 세트 정확도: 0.896457765667575
# 테스트 세트 정확도: 0.8152173913043478
model = RandomForestClassifier(
    n_estimators=150, 
    max_depth=8, 
    min_samples_split=6, 
    min_samples_leaf=3, 
    max_features='sqrt', 
    random_state=42
)

# 교차 검증을 사용한 모델 평가
scores = cross_val_score(model, X_train, y_train, cv=5)
print("교차 검증 정확도:", np.mean(scores))

# 모델 훈련
model.fit(X_train, y_train)

# 훈련 세트에서의 성능 평가
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 훈련 세트에 대한 정밀도, 재현율, F1 점수 계산
precision_train = precision_score(y_train, y_train_pred)
recall_train = recall_score(y_train, y_train_pred)
f1_train = f1_score(y_train, y_train_pred)

# 테스트 세트에 대한 정밀도, 재현율, F1 점수 계산
precision_test = precision_score(y_test, y_test_pred)
recall_test = recall_score(y_test, y_test_pred)
f1_test = f1_score(y_test, y_test_pred)

# 테스트 세트에서의 성능 평가
print("훈련 세트 정확도:", accuracy_score(y_train, y_train_pred))
print("테스트 세트 정확도:", accuracy_score(y_test, y_test_pred))
print("훈련 세트 정밀도:", precision_train)
print("훈련 세트 재현율:", recall_train)
print("훈련 세트 F1 점수:", f1_train)
print("테스트 세트 정밀도:", precision_test)
print("테스트 세트 재현율:", recall_test)
print("테스트 세트 F1 점수:", f1_test)

# 2. 로지스틱 모델 생성
# 훈련 세트 정확도: 0.8610354223433242
# 테스트 세트 정확도: 0.8260869565217391
# 모델 생성 및 훈련
# logreg = LogisticRegression(max_iter=1000)
# logreg.fit(X_train, y_train)

# # 훈련 세트와 테스트 세트에서의 성능 평가
# y_train_pred = logreg.predict(X_train)
# y_test_pred = logreg.predict(X_test)

# train_accuracy = accuracy_score(y_train, y_train_pred)
# test_accuracy = accuracy_score(y_test, y_test_pred)

# print(f"훈련 세트 정확도: {train_accuracy}")
# print(f"테스트 세트 정확도: {test_accuracy}")

# 3. 결정 트리 생성 - 과적합(Overfitting)
# 훈련 세트 정확도: 0.9822888283378747
# 테스트 세트 정확도: 0.7282608695652174
# 모델 생성 및 훈련
# decision_tree = DecisionTreeClassifier(random_state=42)
# decision_tree.fit(X_train, y_train)

# # 모델 평가
# train_accuracy = decision_tree.score(X_train, y_train)
# test_accuracy = decision_tree.score(X_test, y_test)

# print(f'훈련 세트 정확도: {train_accuracy}')
# print(f'테스트 세트 정확도: {test_accuracy}')