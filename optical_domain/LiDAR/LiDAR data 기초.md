# LiDAR란 무엇인가?
- Laser pulse를 방출하여 돌아오는 시간을 기반으로 거리(depth)를 계산하는 센서
- 3차원 공간을 직접 측정 가능
- Camera와 차이
	- Camera > 2D
	- LiDAR > 3D (x, y, z)

# LiDAR data의 중요한 부분
- **LiDAR 데이터는 확률적 정확도를 가진다.**

# LiDAR Sensor
- 128채널 LiDAR sensor
  수직 방향(vertical angle)으로 서로 다른 각도를 가진 레이저 빔이 128개 동시에 나간다는 
  의미
- LiDAR sensor는 yaw(수평) 회전을 하면서 여러개의 빔을 쏘면서 3D point cloud를 구성
  
![[Pasted image 20251223173016.png]]
# LiDAR Sensor의 Scan 방식
- 위 -> 아래 회전하면서 점을 하나씩 찍음
	- 이때 차량이 움직이게 되면 포인트를 정확하게 수집하기 어렵기 때문에
	  IMU sensor를 통해 pitch/roll 등의 정보를 수집하여 point를 보정함
	- IMU의 역할
		- 포인트가 찍힌 정확한 시간
		- 그 시점의 자세 변화(각속도)

# LiDAR의 데이터 기본 구조 (Point Cloud)
- LiDAR 데이터는 보통 Point Cloud(PCD) 형태로 표현
- pcd가 가진 정보
	- 3D 공간 좌표(x, y, z)
	- 반사 강도(intensity / 재질, 거리, 각도에 영향을 받음)
	- ring / channel: 몇 번째 레이저에서 쏜 포인트인지
	- tiemstamp: 스캔 시점 정보(일부 센서에만 포함되어있음)

# LiDAR 데이터의 특징
- **비정형 데이터**
- 이미지(pixel)과 같이 grid 형태로 구성되어 있지 않음
- 포인트 밀도가 거리, 각도에 따라 다름.

# LiDAR 데이터의 좌표계 특성
- 기본적으로 센서 기준 좌표계
- 원점: LiDAR 센서 위치
- x, y, z 방향: 제조사마다 다름

# LiDAR 데이터의 물리적 한계
- 완벽한 LiDAR는 없음
	- noise 존재
	- 유리/검은 물체 -> intensity issue
	- rain/flog -> ghost point
	- 지면/물웅덩이 -> multi-path reflection

# LiDAR 데이터의 표현 방식
- Raw Point Cloud
- BEV(Bird's Eye View)
- Range Image (spherical projection)
- Voxel Grid


# pcd 데이터 전처리
## step1. pcd 기초 처리
- 데이터 핸들링
	- pcd / bin / las foramt
	- numpy 기반 point 처리
	- 대용량 point meomory 관리
- 기본 천처리
	- roi crop
	- downsampling (voxel grid)
	- outlier 제거 (sor / ror)
	- height filtering

## step2. 좌표계 & 정합
- 좌표 변환
	- Sensor -> Vehicle -> world
	- Extrinsic (R, t)
	- 상대좌표 vs 절대좌표
- 정합 & 보정
	- plane fitting (RANSAC)
	- ground alignment
	- pitch/roll 보정 추정
	- mutli-frame alignment 개념

이 개념을 이해하지 못할 경우 아래 내용을 설명할 수 없음.
- Z 이상치
- 경사로 오류
- BEV 왜곡

## step3. 표현 변환 (Representation)
- BEV 생성
	- XY grid
	- height / intensity / density map
	- Resolution trade-off
- Range Image
	- Spherical projection
	- vertical angle 기반 row 구성

딥러닝 모델은 대부분 이 표현 위에서 동작


## step4. 통계 & 공간 알고리즘
- 공간 통계
	- KNN / KD-Tree
	- Local density
	- Height variance
- 이상치 탐지
	- Statistical Outlier Removal
	- Local surface smoothness
	- Residual 기반 필터링

왜 이 점이 이상치인가?를 수학적 설명 가능


## step5. ML/DL
- Calssical
	- Clustering (DBSCAN)
	- Ground segmentation
- Deep Learning
	- BEV semantic segmentation
	- 3D object detection
	- Auto-labeling (Teacher-Student)
	- Multisensor fusion (Camera + LiDAR)

Ai Engineer 영역


## step6. 시스템 & 성능
- 성능 최적화
	- numpy vs torch
	- numba
	- multiprocessing / ray
- pipeline
	- batch
	- streaming
	- ETL
	- automation

