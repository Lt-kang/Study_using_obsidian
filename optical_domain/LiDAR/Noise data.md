# 기초
- 센서 물리 특성
- 환경
- 기하학
- 후처리 과정

위 모든 요소가 결합되어 나타나는 구조적인 오차


# LiDAR Noise란?
- 측정 오차 (measurement error)
- 의미 없는 포인트 (spurious / artifact points)

랜덤하게 보이기도 하지만,
실제로는 특정 조건에서 반복적으로 발생함.



# Noise 유발 원인
## 1. 거리 측정 방식의 한계
LiDAR 대부분 ToF 방식
- laser pulse 발사 -> 반사되어 돌아오는 시간 측정 
- 거리 = 시간 * 빛의 속도 / 2

단,
- 반사 신호가 약함
- 여러 물체에 동시에 반사됨
- 빔이 퍼짐
위와 같은 이유로
정확한 반사 시점을 특정하기 어려워짐


## 2. 환경 요인
- 비 / 안개 / 눈 / 먼지
- 유리 / 물 / 젖은 노면
- 태양광 간섭 (solid-state LiDAR)
-> 이 경우 실제 물체가 아닌 공기 중 입자에서 반사된 포인트가 생성



## 3. 기하학적 요인
- grazing angle (얕은 입사각)
- 멀리 있는 물체
- 얇은 구조물 (전선, 가로등)
-> 레이저가 부분적으로만 반사되거나 엉뚱한 방향으로 산란


# LiDAR Noise 주요 종류

## 1. Random Noise
- 특징
	- 개별 포인트가 미세하게 흔들림
	- 전체적으로 보면 표면이 거침
- 원인
	- 센서 내부 전자 잡읍
	- 거리 해상도 한계
	- clock jitter
- 데이터에서 보이는 현상
	- 평평한 도로가 울퉁불퉁
	- 벽면이 두꺼워짐 (thickness 증가)
- 대응 방법
	- SOR
	- Moving average
	- Voxel downsampling

## 2. Outlier Noise
- 특징
	- 주변과 전혀 관계없는 외딴 포인트
	- 공중에 떠 있는 점
- 원인
	- 먼지 / 비 / 눈
	- 약한 반사체
	- multipath 반사
- 데이터에서 보이는 현상
	- 허공에 점들이 흩어짐
	- 군집과 연결되지 않음
- 대응 방법
	- ROR
	- Density 기반 필터링
	- KNN 기반 제거

## 3. Multipath / Ghost Noise
- 특징
	- 실체 물체 뒤에 유령처럼 복제된 구조
	- 평행한 구조물이 하나 더 생김
- 원인
	- 유리 / 금속 / 물 표면
	- 반사 -> 재반사 -> 센서 복귀
- 데이터에서 보이는 현상
	- 벽 뒤에 또 다른 벽
	- 차량 아래 이상한 점군
- 대응 방법
	- intensity threshold
	- range consistency check
	- 멀티 프레임 누적 검증

## 4. Surface-related Noise
- 특징
	- 경계면에서 포인트가 퍼짐
	- 얇은 물체가 두껍게 인식
- 원인
	- grazing angle
	- beam divergence
	- footprint 크기 증가
- 데이터에서 보이는 현상
	- 연석 / 벽 모서리 / 가드레일이 뭉개짐
- 대응 방법
	- 법선(normal) 기반 필터링
	- angle-aware weighting
	- BEV 투영 시 height aggregation 전략


## 5. Range-dependent Noise
- 특징
	- 거리가 멀수록 noise 증가
	- 포인트 분산 확대
- 원인
	- 신호 감쇠
	- footprint 확대
	- SNR 감소
- 데이터에서 보이는 현상
	- 먼 곳 물체가 흐릿
	- 동일 물체라도 near/far 품질 차이
- 대응 방법
	- distance-based weighting
	- range adaptive threshold
	- far-range downweight


# Noise vs Outlier vs Bias 
| 구분      | 의미              |
| ------- | --------------- |
| Noise   | 작은 랜덤 흔들림       |
| Outlier | 완전히 잘못된 포인트     |
| Bias    | 특정 방향으로 체계적인 오차 |
- Bias는 noise 제거로 해결되지 않음
	- pitch 틀어짐 / sensor calibration 오류


# 실무 관점에서의 정리

## BEV / Height map 관점
- Noise -> Height variance 증가
- Outlier -> spike / hole 생성
- Multipath -> 가짜 장애물

## Auto-labeling / Segmentation 관점
- Noise -> 경계 흐림
- Outlier -> false postive
- Surface noise -> class ambiguity