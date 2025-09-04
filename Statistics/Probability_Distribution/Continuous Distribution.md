# 연속확률분포

# 정의
- 확률변수가 실수(Real number)의 연속적인 값을 가질 때의 확률분포
- 어떠한 구간 안에서 무한히 많은 실수 값을 가질 수 있음.
- 예시
	- 사람의 키(170.1cm, 170.11cm, 170.111cm ...)


# 특징
- **특정 값의 확률은 0**
	- 연속적으로 무한히 많은 값이 있기 때문에
	- $P(X = a) = 0$
	- 그렇기 때문에 구간 확률로 계산
	- $$ P(a ≤ X ≤ b) = \int_a^b{f(x)dx}$$
- 확률밀도함수(PDF, [[Probability Density Function]])
	- 연속형 확률변수의 분포를 나타내는 함수 
	- $$f(x) ≥ 0, \int_{-\infty}^{\infty}{f(x)dx}=1 $$
- 누적분포함수 (CDF, [[Cumulative Distribution Function]])
	- $F(x) = P(X ≤ x)$
	- 항상 0이상 1이하며, 단조 증가


# 종류
- 정규분포([[Normal Distribution]])
- 균등분포([[Uniform Distribution]])
- 지수분포([[Exponential Distribution]])
- 카이제곱분포([[chi-squared Distribution]])
- t 분포([[t Distribution]])
- F 분포([[F Distribution]])
- 감마분포 등


# 시각화 그래프
- PDF
- CDF
- hist plot
- KDE