# 0. EDA 목표
- 모델링 전략을 결정하기 위한 정보 수집
- 사용할 feature / 버릴 feature 판단
- 전처리 방향 결정


# 1. 문제 정의 시각화

## 먼저 확인할 부분
|항목|질문|
|---|---|
|Task|Classification / Regression / Ranking|
|Target|연속형? 범주형?|
|Metric|RMSE? AUC? F1?|
|Data Size|행 수 / feature 수|
|Type|Tabular / Image / Text / Time / Mixed|

- Metric이 바뀌면 EDA 포인트도 바뀐다.
	- RSME -> outlier 중요
	- AUC -> class separation 중요


# 2. target 자체를 먼저 시각화한다
- target 분포를 모르면 모델 선택이 불가능하기 때문

## 어떤 부분을 봐야할까?
- 회귀(Regression)
	- Histogram / Box plot
	- 이상치 존재 여부
	- log transform 필요성

- 분류(Classification)
	- class 불균형 여부
	- baseline accuracy 추정

>여기서 이미 전략 50% 결정됨


# 3. Feature 개별 분석 (Univariate Analysis)
>이 feature 혼자 봤을 때 어떤 놈인가?

## 수치형 feature
- histogram
- skewed? long tail?
- 이상치가 많은가?

## 범주형 feature
- Bar chart
- Cardinality (카테고리 수)
- 희소 카테고리 존재?

## 결측치
- Feature별 missing ratio bar chart
- 특정 feature만 결측 많은지

## 판단 포인트
- 이 feature는 scaling 필요?
- clip / transform 필요?
- 그냥 버릴까?



# 4. Feature <-> Target 관계 분석
>이 feature가 타겟을 설명하는가?


## 수치형 feature <> target
- Scatter plot
- box plot (target binning)

## 범주형 feature <> target
- feature distribution by class
- KDE by class

>여기서 확인되어야 하는 부분
>선형? 비선형?
>threshold 효과?
>class separation 가능성?


# 5. Featrue 간 관계 (Multicollinearity 탐색)
## 목적
- 중복 feature 탐색
- 파생 feature 아이디어

## 도구
- Correlation heatmap
- pair plot (feature 수 적을 때)

>여기서 팁
>Tree 모델이면 상관관계가 덜 중요함
>Linear 모델이면 매우 중요함


# 6. Train / Test 차이 확인 (Leakage 탐지)

- Train vs Test feature distribution 비교
- KS test / 시각적 비교 필요

>차이가 클 경우?
>Public LB 과적합 위험
>CV 전략 변경 필요



# 7. 간단한 모델 + Feature Importance

## 사용 모델
- LightGBM / XGBoost
- Baseline model

## 보는 것
- 중요 feature
- 기대와 다른 결과

> EDA의 연장선이라 볼 수 있음



# 8. Kaggle 초보가 반드시 가져야 할 EDA 사고방식

## 올바른 방향
- 이 feature는 모델에 쓸 가치가 있는가?
- 이상치가 metric에 영향을 주는가?
- 비선형 모델이 필요한가?


# 9. 최소 EDA 체크리스트

-  Target distribution 확인
-  Missing value 분석
-  Feature vs Target 관계
-  Feature correlation
-  Train/Test shift
-  Baseline model + importance


