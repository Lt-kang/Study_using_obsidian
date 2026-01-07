# 원시 pcd (3d 시각화)
## 개념
- x, y, z 좌표를 그대로 3D 공간에 표시
- intensity / ring / class / height 등을 색상으로 표현

## 도구
- open3D / PCL / CloudCompare
- MeshLab
- Potree
- RViz

## 장점
- 공간 구조 이해에 가장 직관적
- 센서 문제 및 이상치(outlier) 확인에 유리

## 단점
- 대용량 데이터 -> 성능 부담
- 분석용 보다는 탐색 & 디버깅에 가까움

## 추천 상황
- 센서 캘리브레이션 검증
- ground / object 분리 품질 확인
- pitch/roll 문제 디버깅


# BEV(Bird's Eye View) / Height Map
## 개념
- (x, y) 평면으로 투영
- z -> height / max / mean / min
- intensity -> pixel value

## 장점 
- 2D 이미지라 빠르고 직관적
- CV 모델&통계 분석과 궁합 좋음
- Semantic Segmentation / Auto-labeling에 필수

## 단점
- z축 정보 요약(생략)
- 고가 구조물 입체감 손실

## 추천 상황
- semantic segmentation
- HD Map
- 품질 지표 계산(coverage, density)

# 단면(Cross-section) / Slice 시각화
## 개념
- 특징 x/y 구간을 잘라 z분포를 확인
- elevation profile 형태

## 장점
- 지면 기울기 / 연석(curbstone) / 구조물 높이 분석에 탁월
- pitch / bias 문제 파악에 매우 좋음

## 추천 상황
- road slope 분석
- ground fitting 결과 검증
- height spike 디버깅

# 통계 기반 시각화 (Histogram / Heatmap)
## 개념
- height / intensity / density 분포
- voxel / grid 단위 통계

## 장점
- 대용량 요약에 강함
- 데이터 품질 관리(QA)에 필수

## 추천 상황
- 프레임별 품질 비교
- 센서 상태 모니터링
- 이상치 자동 감지 기준 설정