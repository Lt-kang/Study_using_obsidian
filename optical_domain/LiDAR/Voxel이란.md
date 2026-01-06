# 기본 개념
- 3차원 공간을 일정한 격자로 나눈 '입체 픽셀(3D pixel)'을 의미
- Pixel = 2D 공간의 최소 단위 (x, y)
- Voxel = Volume + Pixel 3D 공간의 최소 단위 (x, y, z)

![[Pasted image 20260106152318.png]]


# 왜 LiDAR에서 voxel을 사용하는 이유
- LiDAR data는 point의 개수가 많음
- 거리&각도에 따라 밀도가 불균일 함
- 그대로 사용하면 연산량이 매우 큼

## 1. 데이터 압축 / 다운샘플링
- 하나의 voxel 안에 여러 점이 있으면 -> 대표값 1개로 요약
	- 평균 위치 / 최대 height / intensity

## 2. 구조화(regularization)
- CNN / 3D Conv / Sparse Conv 같은 모델은 격자 구조에 적합함
- voxel grid는 정형 데이터 구조 제공

## 3. 노이즈 제거
- 점이 너무 적은 voxel -> outlier로 제거



# point cloud -> voxel (voxelization)
## 개념적 과정
1. 3D 공간을 (dx, dy, dz) 크기의 격자로 분할
2. 각 point가 어느 voxel에 속하는지 계산
3. voxel 단위로 점들을 그룹화

# voxel에 저장하는 정보
- 단순한 공간이 아닌 그 공간 내 점들의 feature를 요약한 정보를 포함하고 있음.
## voxel feature
- point 개수 (density)
- mean / max / min height
- mean of intensity 
- height variance
- centroid

> voxel = 지역적인 통계 요약 단위


# voxel vs point 기반 방법 비교

| 구분    | Voxel 기반          | Point 기반             |
| ----- | ----------------- | -------------------- |
| 구조    | 정형 grid           | 비정형                  |
| 연산    | 빠름 (Conv 가능)      | 느림                   |
| 메모리   | 큼 (빈 voxel 포함)    | 효율적                  |
| 정보 손실 | 있음 (quantization) | 적음                   |
| 예시    | VoxelNet, SECOND  | PointNet, PointNet++ |
> 최근에는 
> * Sparse Voxel
> * Pillar
> * Hybrid(Voxel + point)
> 위와 같은 방식도 많이 사용


> voxel size는 해상도와 연산량의 trade-off 관계



