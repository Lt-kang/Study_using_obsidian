# Precision

## 정의
* True로 예측한 결과 중 실제로 True인 비율


## 공식
$$\frac{TP}{TP + FP}$$


## 해석
1. 0~1 사이의 값이 출력되며 1에 가까울수록 좋은 성능


## 특징
1. False Postive에 민감하여 FP이 늘어나면 Precision이 감소함. 그에 따라 False Positive가 최소화 되어야 하는 모델에서 사용됨.
2. Recall과 상충 관계.


## 한계
1. Precision만으로는 모델의 전반적인 성능 평가가 어려움.
2. True 클래스만 고려하며 False 예측 정확도는 반영하지 않음.


## 사용 예시
* 이진분류 모델
* False Positive가 중요한 상황에서 사용
  * 스팸 필터링
  * 질병 진단

