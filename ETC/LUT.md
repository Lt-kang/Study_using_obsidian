# LUT(Look-Up Table)
- 정의: 입력값과 대응되는 출력값으로 빠르게 변환하기 위해 미리 만들어진 **mapping table**
- 역할: 매번 계산을 하지 않고, 단순히 테이블 참조 만으로 결과를 얻음.
	- 연산 속도 향상
	- 복잡한 함수 적용 가능
- 형태: matrix로 구현되며 `index = input`, `value = output` 구조
```
# input intensity: 0~255
# LUT: 256 크기의 배열
LUT[100] = 200  # 입력 100 → 출력 200
```


# LUT의 종류
## 1. Intensity LUT
- grayscale(0~255)을 변환함.
	- Gamma 보정: `LUT[x] = 255 * (x/255)^y`
	- 히스토그램 평활화 결과를 LUT로 저장 후 적용
- 대표적인 메서드: `cv2.LUT`

## 2. Color LUT
- 입력: RGB -> 출력: 변경된 RGB
	- 특정 색을 다른 색으로 치환
	- Heatmap LUT (ex. `cv2.COLORMAP_JET`, `cv2.COLORMAP_HOT`)
- 대표적인 메서드: `cv2.applyColorMap`

## 3. Geometric LUT
- 입력 좌표(x, y)를 출력 좌표(x', y')으로 mapping
- 이미지 왜곡 보정, remap 등에 사용
- 대표적인 메서드: `cv2.remap`

## 4. Custom LUT
- 특정 규칙이나 수학적 함수 기반으로 직접 정의
	- 임계값 기반 이진화 LUT


# Geometric LUT에 대해서

## 주요 사용 목적
- 이미지의 위치/형태를 바꾸는 기하학적 변환(회전, 이동, 왜곡 보정 등)을 빠르게 적용하기 위함.
- ex) 4channel -> topview / fisheye image를 flat image로 왜곡 보정

## OpenCV에서의 Geometric LUT
```
dst = cv2.remap(src, map_x, map_y, interpolation)
```
- `dst`: 결과 image
- `src`: 원본 image
- `map_x`, `map_y`: 각각 x, y LUT(float32)
- interpolation: 보간 방법(`cv2.INTER_LINEAR`, `cv2.INTER_NEAREST`)

## LUT 구조
- `map_x`: X좌표에 대한 mapping table
- `map_y`: Y좌표에 대한 mapping table
- `map_x`, `map_y`는 동일한 shape
```
dst(y, x) = src(map_y[y, x], 
                map_x[y, x])

* pixel = img[y, x] 이기 때문에 map_y를 먼저 입력됨.
```

## 어째서 remap에 interpolation이 필요한가?
- `cv2.remap`과 같은 메서드의 경우 src coords에 float가 입력될 수 있음.
  아래에서 설명할 Backward mapping을 사용하기 때문.
```
dst(y, x) <- src(y, x)
```
- 이때 pixel은 항상 grid 형태로만 존재하기 때문에 src가 float로 존재할 경우 src의 인접한 pixel을 참고하여 조합해서 적용해야함.(즉, 보간을 사용)


## 어째서 dst(y, x)는 float가 나올 수도 있는가?
- 좌표 변환(회전, scale, 원근 변환, 보정 등)을 하다보면 input이 integer라도 output이 float가 될 수 있음.
- 정직하게 src <-> dst pixel끼리 1:1 매칭을 하는게 아니라 src 혹은 dst에서 matrix를 통한 선형 변환으로 좌표를 변환하기 때문에.
  이 때 선형 변환시 무조건 정수가 나오리란 보장이 없음.
  ex) 회전 변환시 삼각함수가 사용되는데 삼각함수는 -1 ~ 1 사이의 값을 갖으므로 정수값만 갖는 pixel 좌표와 곱할 경우 실수가 나올 수 있음.


## 변환에 대한 접근 방식
### Forward mapping
- `src(x, y)`를 계산하여 `dst(x', y')`를 채움.
- 실제로는 잘 사용하지 않는 방식
- 문제점
	- 연산 후 dst에서 빈 pixel이 생김. 
	- 혹은 하나의 src가 여러 dst에 중복으로 들어감.

### Backward mapping (OpenCV 방식)
- "dst의 각 pixel이 원본의 어디서 왔을까?"를 추적함.
- 즉, LUT를 src의 특정 픽셀이 dst의 특정 픽셀로 옮겨지는 것에 대한 table을 생성하는 게 아니라
  dst의 특정 픽셀이 src의 어느 픽셀과 mapping되는지에 대한 table을 생성함.
  `dst(x, y)`가 `src`의 어떤 `(u, v)`에 대응되는지
- 이때 `(u, v)`는 실수 좌표가 됨.

## interpolation의 종류
- interpolation의 기본 전제
  보간의 대상은 dst pixel의 rgb 값임.
  보간에 사용되는 데이터는 src pixel의 rgb 값이며
  사용할 src pixel의 범위는 보간 종류에 따라 다름.
  
- INTER_NEAREST
	- 최근접 pixel을 선택
	- `(20.3, 10.7) -> (20, 11)`

- INTER_LINEAR
	- 주변 4개 pixel의 가중 평균을 통해 선택

- INTER_CUBIC
	- 주변 16개 pixel을 사용해서 가중합

- INTER_LANCZOS4
	- 주변 8x8 = 64 pixel 사용


## ETC
- LUT는 기본적으로 pixel -> pixel 이지만
  Geometric LUT는 coords -> coords mapping임.
- input-output mapping은 반드시 1:1이 아님. 1:1, 1:N, N:1 모두 만들 수 있음.
  (물론 1:1이 가장 이상적인 형태지만 실제로는 N:1이 가장 흔함.)
	- 해상도 축소의 경우 같은 입력을 여러 출력에 공유하기 때문에 **1:N mapping**
	- 보간 때문에 여러 입력 -> 하나의 출력이 기본 **N:1 mapping**
- LUT를 사용하면 속도에 이점을 얻는다. 
  단, LUT를 memory에 올려야 하기 때문에 memory 사용량이 크다.

