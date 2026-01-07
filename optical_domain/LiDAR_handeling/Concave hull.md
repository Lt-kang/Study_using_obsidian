![[Pasted image 20260107142227.png]]

# Concave hull이란?
- 점들의 실제 분포 형태를 따라가는 '오목한' 영역
- 실제 영역보다 큰 영역이 반환되는 [[Convex hull]]을 보완하려는 개념


# 특징
- Convex Hull은 수학적으로 유일하지만, Concave Hull은 그렇지 않음
	- 그렇기에 실무에서는 Alpha shape으로 구현
	- Alpha shape이란?
		- Delaunay Triangulation 기반으로 "너무 큰 삼각형은 제거"해서 얻는 경계
		- Alpha란?
			- 거리 스케일을 의미함.
			- "이 정도 거리까지는 같은 구조로 묶어도 된다."
		- Alpha값에 대해서

|상황|원인|
|---|---|
|hull이 Convex처럼 됨|α 너무 큼|
|hull이 조각조각|α 너무 작음|
|구멍 너무 많음|점 밀도 불균일|
|노이즈 따라 요철|α 작고 노이즈 많음|



