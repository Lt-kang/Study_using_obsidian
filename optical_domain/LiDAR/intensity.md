# Intensity의 정의
- LiDAR sensor의 Laser pulse가 되돌아 왔을 때 return strength(반사 신호 세기)
	- Depth > 시간으로 결정
	- Intensity > 에너지 크기(amplitude)로 결정

# intensity가 결정되는 물리적 요인
- instensity는 여러 요인의 곱으로 결정

## Reflectivity (표면 반사 특성) 
- 아스팔트: 낮음
- 흰 차선: 높음
- 금속: 각도에 따라 극단적
- 유리/검은 물체: 매우 낮음 or 튐

## Distance attenuation (거리)
- Laser pulse의 에너지는 거리 제곱에 비례하여 감소함.
	- 가까움 -> intensity 큼
	- 멀음 -> intensity 감소
- ex)
  멀리 있는 흰 차선 < 가까운 어두운 물체

## Incident angle (입사각)
- Laser pulse가 수직에 가까울수록 반사가 강함
	- 정면 -> intensity 큼
	- 비스듬함 -> intensity 작음

## 센서 내부 보정 & cliping
- 제조사마다 intensity scale이 다름
- 자동 gain / normalization 적용될 수 있음
- saturation 발생 가능
- => 서로 다른 LiDAR 센서 간 intensity 비교는 의미 없음.


# 데이터 레벨에서의 intensity 특성
## scale이 모든 센서 공통이 아님.
- 0~255 / 0~65535 / float 등 sensor마다 다름
	- 그러므로 intensity는 절대 반사율이 아닌
	  **상대적인 신호 세기**로 봐야 합당


## 동일 물체도 위치에 따라 intensity가 변함
- 같은 물체라도
	- 거리
	- 각도
	- ring 번호에 따라 intensity가 달라짐


## noise에 민감
- rain / fog
- 멀리 있는 거리
- grazing angle
	- intensity 신뢰도 급락


## intensity로 시각화 가능한 물체
### PCD
- 차선
- 도로 경계
- 표지판
- **=> 기하보다 재질 정보가 더 강조됨.**

### BEV intensity map
- 차선 segmentation
- 도로 구조 파악
- weak geometry 보완


# 요약
- intensity는 기하 정보 보다는 재질 정보가 더 강조되는 데이터임.