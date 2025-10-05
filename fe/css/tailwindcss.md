# 1. 기초 문법

## 1-1. 색상
| 속성       | 예시                  | 설명             |
| -------- | ------------------- | -------------- |
| 배경색      | `bg-blue-500`       | 파란색 배경         |
| 텍스트 색    | `text-red-500`      | 빨간색 텍스트        |
| 테두리 색    | `border-green-400`  | 연두색 테두리        |
| hover 효과 | `hover:bg-blue-600` | 마우스 올리면 진한 파란색 |
```
<div class="bg-blue-500 text-white p-4">
  파란 배경, 흰색 글씨
  p는 padding의 약자
  명도는 50이 가장 밝으며 900이 가장 어두움 그 외 수치는 작동하지 않음.
</div>
```

## 1-2. 폰트
|속성|예시|설명|
|---|---|---|
|폰트 크기|`text-sm` `text-lg` `text-2xl`|텍스트 크기|
|폰트 두께|`font-light` `font-bold` `font-extrabold`|굵기|
|정렬|`text-left` `text-center` `text-right`|정렬|
|대소문자 변환|`uppercase` `lowercase` `capitalize`|대문자/소문자|

```
<p class="text-xl font-bold text-center uppercase">
  HELLO WORLD
</p>
```

## 1-3. 크기(padding, margin, width, height)
| 속성            | 방향                                  | 예시                         | 설명    |
| ------------- | ----------------------------------- | -------------------------- | ----- |
| `p` = padding | `t`=top, `b`=bottom, `x`=좌우, `y`=상하 | `p-4` `pt-2` `px-6`        | 안쪽 여백 |
| `m` = margin  | 동일                                  | `m-4` `mt-2` `mx-auto`     | 바깥 여백 |
| width         | -                                   | `w-32` `w-full` `w-screen` | 너비    |
| height        | -                                   | `h-16` `h-full` `h-screen` | 높이    |
```
<div class="w-32 h-16 bg-gray-200 p-4 m-2">
  박스
  p-1 = 4px = 0.25rem
</div>
```

# 2. Flexbox & Grid
## 2-1. Flexbox
| 속성       | 예시                                                 | 설명        |
| -------- | -------------------------------------------------- | --------- |
| Flex 선언  | `flex`                                             | flex 컨테이너 |
| 방향 설정    | `flex-row` `flex-col`                              | 가로, 세로 방향 |
| 정렬 (주축)  | `justify-start` `justify-center` `justify-between` | 가로 정렬     |
| 정렬 (교차축) | `items-start` `items-center` `items-end`           | 세로 정렬     |
```
<div class="flex justify-between items-center p-4 bg-gray-100">
  <div>왼쪽</div>
  <div>오른쪽</div>
</div>
```

## 2-2. Grid
| 속성      | 예시                          | 설명        |
| ------- | --------------------------- | --------- |
| Grid 선언 | `grid`                      | grid 컨테이너 |
| 열 개수 설정 | `grid-cols-2` `grid-cols-3` | 열 갯수      |
| 간격 설정   | `gap-2` `gap-4`             | 칸 사이 간격   |
```
<div class="grid grid-cols-3 gap-4">
  <div class="bg-red-300 p-2">1</div>
  <div class="bg-green-300 p-2">2</div>
  <div class="bg-blue-300 p-2">3</div>
</div>
```

# 3. 반응형 디자인 (Responsive)

|접두사|기준 화면 크기|
|---|---|
|`sm:`|640px 이상|
|`md:`|768px 이상|
|`lg:`|1024px 이상|
|`xl:`|1280px 이상|
|`2xl:`|1536px 이상|

```
<div class="bg-red-500 sm:bg-yellow-500 md:bg-green-500 lg:bg-blue-500 xl:bg-purple-500 p-4">
  화면 크기에 따라 배경색이 바뀝니다.
</div>
```