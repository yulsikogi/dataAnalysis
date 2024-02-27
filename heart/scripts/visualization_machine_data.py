import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, auc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# 1. 랜덤 포레스트 모델 생성
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

# 1. 혼동 행렬 시각화
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues', ax=ax)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title(title)

plot_confusion_matrix(y_test, y_test_pred, "Confusion Matrix for Test Set")

# 2. ROC 곡선 및 AUC 점수
def plot_roc_curve(y_true, y_scores, title):
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)
    auc_score = auc(fpr, tpr)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (area = %0.2f)' % auc_score)
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")

y_test_scores = model.predict_proba(X_test)[:, 1]
plot_roc_curve(y_test, y_test_scores, 'ROC Curve for Test Set')

# 3. 특성 중요도 시각화
def plot_feature_importance(model, features):
    importances = model.feature_importances_
    indices = np.argsort(importances)

    plt.figure(figsize=(8, 6))
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')

plot_feature_importance(model, features)

plt.show()