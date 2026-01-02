# Distribution graph
>데이터가 어떻게 퍼져 있는지를 보여줌
## Histogram
- 연속형 데이터 분포를 구간(bin)으로 나눠 표현
- 정규분포 여부, skewness 파악에 필수

## Box Plot
- 중앙값, 사분위수, 이상치를 한 번에 표현
- 여러 그룹 비교에 매우 강력

## Violin Plot
- Pox plot + KDE 결합
- 분포의 모양까지 보고 싶을 때

## Density Plot (KDE)
- 히스토그램을 부드러운 곡선으로 표현
- 분포 비교에 적합

## Rug Plot
- 개별 데이터 위치를 선으로 표시
- KDE/histogram 보조용


# Relationship graph
>변수 간 상관관계 / 패턴을 보여줌
## Scatter Plot
- 두 변수의 관계 확인(선형/비선형)
- 가장 기본적이면서 가장 중요한 그래프

## Bubble Chart
- Scatter + 점크기로 3번째 변수 표현


## Pair Plot
- 모든 쌍의 scatter + 분포를 한 번에
- EDA의 왕


## Hexbin Plot
- 점이 너무 많을 때 격자로 밀도 표현
- 대용량 데이터에 적합

## Joint Plot
- Scatter + 주변 분포(Histogram/KDE)


# Comparison graph
>값의 크기 차이를 비교
## Bar Chart
- 범주형 데이터 비교의 기본

## Grapued Bar Chart
- 그롭 간 비교 (카테고리 x 카테고리)

## Stacked Bar Chart
- 전체 대비 구성 비율 표현

## Dot Plot
- 막대를 점으로 대체 -> 깔끔한 비교

## Lollipop Chart
- Bar chart의 시각적 개선 버전


# Composition(비율/구성) graph
>전체 중 각 부분이 차지하는 비중
## Pie Chart
- 단순한 비율 표현

## Donut Chart
- Pie chart의 가독성 개선 버전

## Treemap
- 계층 구조 + 비율 표현
- 대규모 카테고리에 적합

## Sunburst Chart
- 원형 계층 구조 시각화

## Waffle Chart
- 픽셀 단위 비율 표현(직관적)


# Time Series graph
>시간 흐름에 따른 변화
## Line Chart
- 시계열의 기본

## Area Chart
- 누적 변화 강조

## Stacked Area Chart
- 시간에 따른 구성 변화

## Timeline
- 사건(Event) 중심 시간 표현

## Candlestick Chart
- 금융 데이터 전용(OHLC)


# Multivariate graph
>3개 이상 변수를 동시에
## Heatmap
- 값의 크기를 색으로 표현
- 상관행렬 필수 도구

## Parallel Coordinates
- 고차원 데이터 패턴 비교

## Radar Chart
- 항목별 점수 비교

## 3D Scatter Plot
- 3차원 관계 탐색

## Contour Plot
- 3D 데이터를 2D 등고선으로 표현


# Spatial / Geo graph
>위치 정보 포함 데이터
## Choropleth Map
- 지역별 값 색상 표현

## Geo Scatter Map
- 지도 위 점 표현

## Spatial Heatmap
- 위치 밀도 시각화

## Cartogram
- 값에 따라 지형 왜곡


# Network & Flow
>연결, 이동, 관계 구조

## Network Graph
- node-edge 관계

## Sankey Diagram
- 흐름의 크기 표현

## Chord Diagram
- 그룹 간 상호작용

## Alluvial Diagram
- 시간에 따른 흐름 변화


# 불확실성/통계 결과 시각화
>신뢰도, 오차, 분포 추정

## Error Bar Plot
- 평균 ± 오차

## Confidence Interval Plot
- 추정의 신뢰 범위

## Forest Plot
- 메타분석, 효과 크기 비교

## Ridgeline Plot
- 여러 분포를 층층이 비교



# 특수/고급 시각화
>연구/산업/ML에 자주 등장

## Decision Tree Plot
- 모델 구조 설명

## SHAP / Feature Importance Plot
- 모델 해석

## PCA Biplot
- 차원 축소 + 변수 영향

## t-SNE / UMAP
- 고차원 데이터 군집 시각화

