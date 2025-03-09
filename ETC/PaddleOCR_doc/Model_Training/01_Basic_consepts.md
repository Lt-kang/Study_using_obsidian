# Model Training
이 글은 모델 학습 및 튜닝에 있어서 필수적인 내용을 담은 글입니다.
동시에, 학습 데이터의 구조와 fine-tuning에 사용할 데이터를 어떻게 준비할지에 대해서도
소개하고 있습니다.


# 1. Yml Configuration
PaddleOCR은 network 학습과 parameters를 제어하기 위해 configuration file을 사용합니다.
해당 파일은 model, optimizer, loss function, 전처리, 후처리 parameters 등을 설정할 수 있습니다.
PaddleOCR은 configuration으로부터 parameters를 읽으며 학습 과정을 구축합니다.
Fine-tuning 또한 configuration file을 수정함으로써 간편하게 수행할 수 있습니다.

전체 Configuration file 설명은 [여기](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/blog/config.html#loss-ppocrlosses)를 참조 하십시오.


## 2. Basic Concepts
모델 학습 과정에서 일부 hyper-parameters 수동으로 지정하여 최소 비용으로 최적의 결과를 얻을 수 있습니다. 데이터의 양이 다르면 필요한 hyper-parameters도 달라질 수 있습니다.  
자신의 데이터에 맞춰 model을 fine-tuning하려면 몇 가지 참고할 수 있는 parameters 조정 전략이 있습니다.


## 2.1 Learning Rate
Learning Rate는 neural networks 학습에 있어서 중요한 파라미터 중 하나 입니다.
이는 loss function의 최적해(optimal solution)으로 이동하는 gradient의 step size를 결정합니다.
PaddleOCR에서는 configuration files를 통해 다양한 Learning Rate 학습 전략을 제공합니다.

이를테면
```
Optimizer: 
   ... 
   lr: 
      name: Piecewise 
      decay_epochs : [700, 800] 
      values : [0.001, 0.0001] 
      warmup_epoch: 5
```
`Piecewise` 는 단계별 일정한 감쇠를 의미합니다.
learning stages 마다 learning rate가 각기 다르게 설정됩니다. 
(각 stage에서는 동일한 learning rate 사용)

`warmup_epoch`는 첫 5번의 epochs 동안 learning rate가 0부터 `base_lr`까지 점진적으로 상승하는 것을 의미합니다.
(원래는 learning_rate.py 코드를 제공했으나 url이 정상적으로 연결되지 않아서 적지 않음.)


## 2.2 Regularization
정규화는 over-fitting을 피할 수 있는 효과적인 방법 중 하나 입니다.
PaddleOCR은 L1 정규화와 L2 정규화를 제공 합니다.
L1, L2 정규화는 가장 널리 사용되는 정규화 방법 입니다.
L1 정규화는 정규화 항(parameter의 절대값의 합)을 Loss function에 추가 합니다.
L2 정규화는 정규화 항(parameter의 제곱의 합)을 Loss function에 추가 합니다.
이를 config file에 적용하는 아래와 같습니다.
```
Optimizer:
  ...
  regularizer:
    name: L2
    factor: 2.0e-05
```

## 2.3 Evaluation Indicators

#### (1) Detection stage
먼저, Detection frame과 label frame의 IOU를 평가 합니다.
만약 IOU가 특정 임계값(certain threshold)보다 크다면, 탐지가 정확하다고 판단합니다.
detection frame과 label frame은 일반적인 target detection frame과 다릅니다.
그리고 두 frame은 polygon으로 표현됩니다.




#### (2) Recognition stage



#### (3) End-to-end statistics

