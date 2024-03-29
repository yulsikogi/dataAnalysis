# Titanic Dataset - train.csv Overview

## 1. 데이터셋 소개
Titanic 데이터셋은 1912년 타이타닉호의 침몰과 관련된 승객 및 승무원의 정보를 담고 있습니다. 이 데이터는 승객의 생존 여부를 예측하는 머신 러닝 모델을 개발하는 데 주로 사용됩니다.

## 2. 데이터 구조
총 데이터 행 수: 891
총 데이터 열 수: 12

열(특성) 설명
PassengerId: 승객의 고유 식별번호
Survived: 생존 여부 (0 = 사망, 1 = 생존)
Pclass: 승객의 객실 등급 (1 = 1등석, 2 = 2등석, 3 = 3등석)
Name: 승객의 이름
Sex: 승객의 성별
Age: 승객의 나이
SibSp: 함께 탑승한 형제, 자매 또는 배우자의 수
Parch: 함께 탑승한 부모 또는 자녀의 수
Ticket: 티켓 번호
Fare: 탑승 요금
Cabin: 객실 번호
Embarked: 탑승 항구 (C = Cherbourg, Q = Queenstown, S = Southampton)

## 3. 기초 통계량
승객 평균 나이: 29.7세
평균 요금: 32.20
대부분의 승객은 3등석에 탑승 (Pclass 3)

## 4. 결측치 정보
Age: 177개의 결측치
Cabin: 687개의 결측치
Embarked: 2개의 결측치

## 5. 초기 분석 및 관찰
나이 데이터에 결측치가 많이 존재합니다. 나이가 생존에 중요한 요소일 수 있으므로, 이 결측치를 적절히 처리하는 것이 중요합니다.
Cabin 열에도 많은 결측치가 있습니다. 객실 위치가 생존율에 영향을 미쳤을 수 있으므로, 이 열의 데이터 처리가 중요합니다.
대부분의 승객이 남성이며, 3등석에 탑승했습니다.

## 6. 결론 및 다음 단계
이 초기 분석을 통해 타이타닉호의 승객 구성과 데이터의 기본적인 특성을 이해할 수 있습니다. 향후 분석에서는 결측치 처리, 변수간의 상관관계 탐색, 생존 예측 모델 개발 등을 진행할 예정입니다.

- 참고 자료
Kaggle Titanic Dataset