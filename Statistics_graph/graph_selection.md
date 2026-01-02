
# 핵심
- 그래프 선택 = 데이터 문제를 시각 언어로 번역하는 과정


## 이 그래프로 무엇을 알고 싶은가?
|질문 유형|의미|
|---|---|
|분포|값이 어떻게 퍼져 있는가?|
|비교|어떤 게 더 큰가/작은가?|
|관계|변수 간 연관성이 있는가?|
|변화|시간에 따라 어떻게 변하는가?|
|구성|전체 중 비율은 어떻게 되는가?|
|공간|위치에 따라 패턴이 있는가?|

# 그래프 매핑 테이블
## A. 분포를 보고싶다
|데이터|추천 그래프|
|---|---|
|단일 연속형|Histogram|
|그룹 비교|Box plot|
|분포 모양 강조|Violin / KDE|
|이상치 강조|Box plot|

## B. 크기를 비교하고 싶다
|상황|추천 그래프|
|---|---|
|범주형 비교|Bar chart|
|값 차이 강조|Dot plot|
|그룹 간 비교|Grouped bar|
|누적 구성|Stacked bar|

## C. 관계를 보고 싶다
|데이터 규모|추천|
|---|---|
|소규모|Scatter|
|대규모|Hexbin|
|다변수 탐색|Pair plot|
|분포 포함|Joint plot|

## D. 시간에 따른 변화를 보고 싶다
|목적|그래프|
|---|---|
|추세|Line|
|누적 변화|Area|
|구성 변화|Stacked area|
|이벤트 중심|Timeline|


## E. 비율/구성을 알고 싶다
|상황|추천|
|---|---|
|항목 ≤ 5|Pie / Donut|
|항목 많음|Bar|
|계층 구조|Treemap|
|흐름 구조|Sunburst|


## F. 공간적 패턴을 보고 싶다
|데이터|그래프|
|---|---|
|지역 단위|Choropleth|
|좌표 데이터|Geo scatter|
|밀도|Spatial heatmap|




# 요약 (데이터 분석/AI 기준)
- **EDA 단계**
    - Histogram → Box → Scatter → Heatmap
        
- **파라미터 튜닝 / Optuna**
    - Scatter + Color / 3D surface
        
- **LiDAR / CV**
    - Spatial heatmap / BEV / Residual histogram
        
- **모델 평가**
    - Error distribution / Confidence interval / SHAP plot


