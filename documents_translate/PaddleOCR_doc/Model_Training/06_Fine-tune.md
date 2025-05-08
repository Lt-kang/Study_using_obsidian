# 1. Background and meaning

PaddleOCr으로부터 제공된 PP-OCR 시리즈 모델들은 일반적인 환경에서 훌륭한 성능을 보입니다.
그리고 대부분의 case에서 문자탐지 및 인식 문제를 해결할 수 있습니다.

특정 도메인 영역에서,
당신이 더 좋은 모델을 획득하길 바란다면, 당신은 PP-OCR의 탐지/인식 모델들을 fine-tune을 통해서 더 개선 시킬 수 있습니다.

핵심 포인트는 아래와 같습니다.
1. PP-OCR의 사전 학습된 모델은 뛰어난 일반화 성능을 가지고 있습니다.
2. 동일한 도메인 데이터에 대해서 탐지 500건 / 인식 5천건 이상의 데이터가 주어진다면 PP-OCR의 성능을 향상시킬 수 있습니다.
3. fine-tune을 할 때, 실제 환경에서 수집된 데이터를 추가하면 모델의 정확도/일반화 성능을 향상시킬 수 있습니다.  (과적합 방지)
4. 문자 탐지에 대해서, text의 영역을 최대한 작게 맞춘 data일수록 탐지 능력이 향상됩니다.
5. fine-tune을 할 때, 하이퍼 파라미터를 적절히 조정하는 것이 더 좋은 모델을 얻는 방법 입니다.
   * `real general scene data` = 일반 환경(범용적인)에서 실제로 수집된 이미지 데이터

___
___
# 2. Text detection model fine-tuning

## 2.1. Dataset
* `Dataset`: text detection model의 fine-tune을 하는데 있어서 데이터셋은 최소 5천 장 이상을 준비하기를 권장합니다.
* `Dataset annotation`: `single-line text annotation` format, 실제 단어 의미와 label을 매칭 시켜주셔야 합니다.
이를테면 "김 철수"라는 이름이 있을 때 "김"과 "철수"는 서로 떨어져 있는 단어이지만 하나의 의미기 때문에, label을 "김 철수"로 해주며 동시에
labeling 또한 하나의 semantic으로 지정해주셔야 합니다.

___
## 2.2. Model 
정확도와 일반화 성능이 아주 우수한 모델인 PP-OCRv3 model 을 사용하기를 권장 드립니다.
```
config file
ch_PP-OCRv3_det_student.yml
ch_PP-OCRv3_det_distill_train.tar
```

* Note: PP-OCRv3 pre-trained model을 사용할 경우, 해당 폴더에 존재하는 `student.pdparams` 파일을 사전 학습 모델로 사용해야 하며,
student model만 사용해야 합니다.

___
## 2.3. Training hyperparameter

fine-tune을 진행할 때, 가장 중요한 하이퍼 파라미터는 pre-training model path `pretrained_model`, `learning_rate`, `batch_size` 입니다.
```
Global:
  pretrained_model: ./ch_PP-OCRv3_det_distill_train/student.pdparams # pre-training model path
Optimizer:
  lr:
    name: Cosine
    learning_rate: 0.001 # learning_rate
    warmup_epoch: 2
  regularizer:
    name: 'L2'
    factor: 0

Train:
  loader:
    shuffle: True
    drop_last: False
    batch_size_per_card: 8  # single gpu batch size
    num_workers: 4
```
위 config file에서 반드시 `pretrained_model`을 `student.pd.params`로 지정해주어야 합니다.

pp-OCR의 기본 config file은 8개의 gpu로 학습을 하는 시나리오 기준이며, pre-trained model은 불러오지 않습니다.
따라서 사용자에 맞게 하이퍼 파라미터 수정을 필요로 합니다.

이를테면,
* 단일 gpu를 사용하며 single gpu batch_size = 8일 경우 총 batch_size는 8이므로 learning rate는 `1e-4`를 권장드립니다.
* 단일 gpu를 사용하지만 메모리 제한으로 인해 single gpu batch_size = 4일 경우 총 batch_size는 4이므로 learning rate는 `5e-5`를 권장드립니다.

___
## 2.4. Prediction hyperparameter

학습이 완료된 모델을 내보내고 추론할 때, 
작은 영역의 텍스트의 탐지 성능을 증가시키기 위해 예측된 이미지의 스케일을 조정할 수 있습니다.
바로 아래 하이퍼 파라미터(DBNet 추론에 사용된)들 입니다.

| Hyper-parameter     | type  | default | meaning                                    |
| ------------------- | ----- | ------- | ------------------------------------------ |
| det_db_thresh       | float | 0.3     |                                            |
| det_db_box_thresh   | float | 0.6     |                                            |
| det_db_unclip_ratio | float | 1.5     | `Vatti clipping` 확장 계수, 이 값을 통해 텍스트 영역을 확장 |
| max_batch_size      | int   | 10      | batch size                                 |
| use_dilation        | bool  | False   | 더 나은 탐지 결과를 위해 분할 결과를 확장할지에 대한 내용          |
| det_db_score_mode   | str   | "fast"  |                                            |

___
___
# 3. Text recognition model fine-tuning

## 3.1. Dataset
* `Dataset`: dictionary이 변경되지 않는다면, 파인튜닝에 사용할 데이터셋은 최소 5,000개의 텍스트 인식 데이터를 준비하기를 권장합니다.
  만약 dictionary가 변경되었다면(추천하지는 않지만), 더 많은 양의 데이터를 필요로 합니다.
* `Data distribution`: 실제로 사용할 시나리오와 최대한 비슷한 분포를 갖는 것을 권장합니다. 실제 장면에 짧은 텍스트가 많이 포함되어 있따면, 학습 데이터에 짧은 텍스트를 더 많이 포함하는 것을 권장합니다. 실제 시나리오에서 공백 인식이 중요할 경우, 학습데이터에 공백이 포함된 텍스트를 더 추가할 것을 권장합니다.
* `Data synthesis`: 특정 문자 인식 오류가 발생하는 경우, 해당 문자에 대한 데이터셋을 기존 데이터셋에 추가한 뒤 낮은 learning rate로 fine-tune을 하는 것을 권장합니다. 원본 데이터와 신규 데이터간의 비율인 10:1에서 5:1 사이가 적절합니다. 이는 단일 장면에서 너무 많은 데이터로 인해 발생할 수 있는 모델 과적합 방지를 위함 입니다. 동시에, 말뭉치의 단어 빈도수 균형을 맞춰야 하며, 자주 사용되는 단어의 빈도가 너무 낮아지지 않도록 해야 합니다.

TextRenderer 도구를 활용하여 특정 문자를 생성할 수 있으며, 합성 예시에 대해서는 [data synthesis](https://paddlepaddle.github.io/PaddleOCR/main/en/applications/%E5%85%89%E5%8A%9F%E7%8E%87%E8%AE%A1%E6%95%B0%E7%A0%81%E7%AE%A1%E5%AD%97%E7%AC%A6%E8%AF%86%E5%88%AB.html)를 참고해주세요.
합성 데이터 말뭉치는 실제 사용 시나리오에 최대한 가까운 방식으로 구성되어야 하며, 폰트와 배경의 다양성을 확보해야 실제 장면과 유사해져 모델 성능 향상에 도움이 됩니다.

* `Common Chinese and English data`: 학습 시, 일반적인 실제 데이터를 학습 데이터에 추가할 수 있습니다. 그리고 이는 일반화 성능 향상에 도움이 됩니다. (이를테면, fine-tuning 시, dictionary 변경 없이 LSVT, RCTW, MTWI 등의 실제 데이터를 추가하는 것)

## 3.2. Model

`PP-OCRv3` 모델 사용을 권장합니다. 
- config file: `ch_PP-OCRv3_rec_distillation.yml`
- pre-trained model: `ch_PP-OCRv3_rec_train.tar`
- 정확도와 일반화 성능이 가장 우수한 모델 입니다.

추가로 `PP-OCR` 시리즈 버전을 확인하려면 [PP-OCR Series MOdel Library](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/model_list.html)를 확인해 주세요.

`PP-OCRv3`모델은 GTC 전략을 사용합니다. SAR branch는 많은 수의 파라미터들을 가지고 있습니다. 훈련 데이터가 간단한 scene일 경우, 모델이 과적합되기 쉬워 파인튜닝 성능이 저하될 수 잇습니다.
따라서 GTC 전략을 제거하는 것이 권장됩니다. 
config file은 다음과 같이 수정합니다.
```
Architecture:
  model_type: rec
  algorithm: SVTR
  Transform:
  Backbone:
    name: MobileNetV1Enhance
    scale: 0.5
    last_conv_stride: [1, 2]
    last_pool_type: avg
  Neck:
    name: SequenceEncoder
    encoder_type: svtr
    dims: 64
    depth: 2
    hidden_dims: 120
    use_guide: False
  Head:
    name: CTCHead
    fc_decay: 0.00001
Loss:
  name: CTCLoss

Train:
  dataset:
  ......
    transforms:
    # remove RecConAug
    # - RecConAug:
    #     prob: 0.5
    #     ext_data_num: 2
    #     image_shape: [48, 320, 3]
    #     max_text_length: *max_text_length
    - RecAug:
    # modify Encode
    - CTCLabelEncode:
    - KeepKeys:
        keep_keys:
        - image
        - label
        - length
...

Eval:
  dataset:
  ...
    transforms:
    ...
    - CTCLabelEncode:
    - KeepKeys:
        keep_keys:
        - image
        - label
        - length
...
```

## 3.3. Training hyper-parameter

## 3.4. Training optimization

학습 과정은 하룻밤 사이에 이루어지지 않습니다.
학습 평가의 한 단계를 완료한 후에는, 실제 장면에서 현재 모델의 오인식 사례(badcase)를 수집하고 분석하여, 학습 데이터의 비율을 목적에 맞게 조정하거나 합성 데이터를 추가하는 것이 권장 됩니다.
이러한 과정을 여러번 차례 반복 학습함으로써 모델 성능이 지속적으로 최적화 됩니다.

학습 중에 사용자 정의 사전을 변경하는 경우, FC 층의 마지막 레이어 파라미터가 로드되지 않아 초기 반복(iteration) 단계에서도 Accuracy가 0이 되는 것은 정상입니다.
걱정하지 마세요.
사전 학습된 모델을 로드하면 여전히 모델 수렴 속도를 높일 수 있습니다.









