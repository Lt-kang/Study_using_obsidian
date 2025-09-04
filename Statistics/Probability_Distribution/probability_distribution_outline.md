# 확률분포의 개념
- 정의: 확률변수([[Random Variable]]])가 취할 수 있는 모든 값과 그 값이 나타날 확률 사이의 관계를 나타낸 것
- **어떤 사건이 일어날 가능성을 수학적으로 정리한 함수**


# 확률분포의 역할
- 현실 세계의 불확실성을 수학적으로 모델링
- 데이터 분석 / 통계 추론 / 머신러닝 / 금융 공학 / 공학적 신뢰성 분석 등 다양한 분야에서 활용
- 예측과 의사결정을 체계적으로 할 수 있도록 해줌


# 확률분포의 종류
- 이산확률분포([[Discrete Distribution]])
- 연속확률분포([[Continuous Distribution]])

## 이산확률분포 (Discrete Distribution)
- 이산형 확률변수일 때 사용
- 대표적인 예
	- 베르누이 분포([[Bernoulli Distribution]])
	- 이항 분포([[Binomial Distribution]])
	- 포아송 분포([[Poisson Distribution]])

## 연속확률분포 (Continuous Distribution)
- 연속형 확률변수일 때 사용
- 특정 값이 나올 확률은 0이고, 구간에 대한 확률을 확률밀도함수로 계산
- 대표적인 예
	- 정규 분포([[Normal Distribution]])
	- 지수 분포([[Exponential Distribution]])
	- 균등 분포([[Uniform Distribution]])


# 확률분포의 핵심 요소
## 확률질량함수(PMF)
- 이산확률변수의 각 값에 대응하는 확률
- $P(X = x)$

## 확률밀도함수(PDF)
- 연속확률변수의 밀도 함수
- $P(a ≤ X ≤ b) = \int_{a}^{b}{f(x)dx}$  

## 분포함수(CDF)
- 확률변수가 특정 값 이하일 확률
- $F(x) = P(X ≤ x)$
