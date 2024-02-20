# 타이타닉 생존자 데이터 분석하기
- 데이터 분석의 첫걸음 타이타닉 생존자 데이터 분석해보기.

## 데이터 셋
1. gender_submission
2. test
3. train

## 순서
### 데이터 탐색 및 이해 (Exploratory Data Analysis, EDA)
- train 데이터셋 분석
    - 먼저 train 데이터셋을 로드하고, 데이터의 구조와 기본 통계를 확인.
    - 여기에는 승객의 나이, 성별, 티켓 클래스, 생존 여부 등의 정보가 포함.
- 변수 확인
    - 각 변수(특성)의 의미를 이해하고, 어떤 변수가 생존 예측에 중요할 수 있는지 가설을 세움.
    - 예를 들어, 성별, 나이, 티켓 클래스 등이 중요한 요인.
- 결측치 확인
    - 데이터에 결측치가 있는지 확인하고, 결측치 처리 방법(삭제, 평균으로 대체 등)을 고려.
- 데이터 시각화
    - 데이터를 시각화하여 각 변수 간의 관계, 분포, 생존자와 비생존자 간의 차이 등을 탐색.
    - Matplotlib, Seaborn 등의 라이브러리를 사용.

### 데이터 전처리 및 특성 공학 (Feature Engineering)
- 데이터 정제
    - 결측치 처리, 이상치 제거 등을 수행.
- 특성 공학
    - 새로운 특성을 생성하거나 기존 특성을 변형하여 분석에 유용한 형태로 만듦.
    - 예를 들어, 이름에서 호칭을 추출하거나, 가족 구성원 수를 계산하는 등의 작업.
- 범주형 변수 처리
    - 성별, 승선지 등 범주형 변수를 숫자로 변환합니다.
    - 원-핫 인코딩(one-hot encoding)이나 레이블 인코딩(label encoding)을 사용할 수 있습니다.

### 모델링 및 평가
- 데이터 분할
    - train 데이터셋을 훈련용과 검증용으로 분할.
- 모델 선택 및 훈련
    - 로지스틱 회귀, 결정 트리, 랜덤 포레스트 등 다양한 분류 알고리즘을 사용해 모델을 훈련.
- 성능 평가
    - 정확도, 정밀도, 재현율, F1 점수 등을 계산하여 모델의 성능을 평가.
- 하이퍼파라미터 튜닝
    - 모델의 성능을 최적화하기 위해 하이퍼파라미터를 조정.

### 테스트 및 제출
- test 데이터셋 처리
    - train 데이터셋에 적용한 전처리 및 특성 공학을 test 데이터셋에도 동일하게 적용.
- 최종 모델로 예측
    - 훈련된 최종 모델을 사용하여 test 데이터셋의 생존 예측을 수행합니다.
- 제출 형식 확인 및 제출
    - gender_submission 파일은 제출 형식의 예시.
    - 이 형식에 맞춰 예측 결과를 제출.

## 요점
- 이번 분석을 통해 데이터 분석 능력 향상 및 시각화, 그리고 생존율 예측과 같은 분석을 시도하기.