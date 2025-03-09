# Text Recognition

이 글은 데이터 전처리, 모델 학습, fine-tuning, evaluation, prediction을 포함한
PaddleOCR text recognition 작업에 대한 종합적인 가이드 입니다.

# 1. Data Preparation
## 1.1. Prepare the Dataset

PaddleOCR은 2개의 data formats을 지원합니다.
* `lmdb`: LMDB format(LMDBDataSet)
* `General Data`: text files (SimpleDataSet)

기본 학습 데이터 경로는 `PaddleOCR/train_data` 입니다.

그 외 경로를 사용하려 한다면 아래 명령어를 통해
symbolic path를 생성하여 사용해주세요.

create symbolic path
`mklink /d <path/to/paddle_ocr>/train_data/dataset <path/to/dataset>`

___

## 1.2. Custom Dataset
이 가이드의 Dataset은 General Dataset(text file)을 사용합니다.

* Training Dataset
학습 image와 label text file은 동일한 폴더에 위치하기를 권장합니다.
자세한 내용은 아래 내용을 확인해주세요.

**Note**: text file의 경우 `\t`을 통해 image path와 label을 분리합니다.
그 외 separator를 사용할 경우 오류가 발생할 수 있으니 유의하시기 바랍니다.

```
" Image Filename                   Image Label "

train_data/rec/train/word_001.jpg   Simple and reliable
train_data/rec/train/word_002.jpg   Making the complex world simpler with technology
...
```

최종적으로 `train_data` 폴더 구조는 아래와 같이 준비해주셔야 합니다.
```
|-train_data
  |-rec
    |- rec_gt_train.txt
    |- train
        |- word_001.png
        |- word_002.jpg
        |- word_003.jpg
        | ...
```

위에서 설명한 구조(1줄에 1개의 이미지 입력) 외에도,
PaddleOCR은 data augmented offline 학습 또한 지원합니다.
batch 당 sample 중복 학습을 회피하기 위해
image path와 동일한 label을 1개의 line에 작성할 수 있습니다.

학습 중, PaddleOCR은 여러개의 image 중 랜덤하게 1개를 선택합니다.
위와 같은 방법을 사용하기 위해서는
아래 양식을 확인해주세요.
```
["11.jpg", "12.jpg"]   Simple and reliable
["21.jpg", "22.jpg", "23.jpg"]   Making the complex world simpler with technology
3.jpg   ocr
```

위 예시해서 "11.jpg"와 "12.jpg"는 `simple and reliable`이라는 동일한 label을 공유 합니다.
이 때 paddleOCR은 학습 중 위 이미지들 중에서("11.jpg", "12.jpg) 랜덤하게 1개를 선택하여 학습에 사용합니다.

* Validation Dataset

training dataset과 유사하게,
validation dataset 또한 모든 image 파일을 label text file(`rec_gt_test.txt`)과 동일한 폴더에 위치 시킵니다.

```
|-train_data
  |-rec
    |- rec_gt_test.txt
    |- test
        |- word_001.jpg
        |- word_002.jpg
        |- word_003.jpg
        | ...
```

___
## 1.3. Data Download
* ICDAR2015

만약 당신이 dataset을 준비하지 않았다면, `ICDAR2015` dataset을 (test 용도로)다운로드 할 수 있습니다.
또한 `DTRB`(benchmarking에 사용할 LMDB format의 dataset을 다운로드 하기 위해)를 참고할 수 있습니다.

만약 당신이 `ICDAR2015` dataset을 사용한다면,
PaddleOCR은 `ICDAR2015` dataset에 사용할 label file을 제공합니다.
아래 경로를 확인해주세요.
```
# Training set label
wget -P ./train_data/ic15_data  https://paddleocr.bj.bcebos.com/dataset/rec_gt_train.txt
# Test Set Label
wget -P ./train_data/ic15_data  https://paddleocr.bj.bcebos.com/dataset/rec_gt_test.txt
```

추가로 PaddleOCR은 data format을 conversion할 수 있는 script 또한 제공합니다.
이 script는 `ICDAR` dataset의 label을 PaddleOCR dataformat으로 변환시켜줍니다.
이 script는 `ppocr/utils/gen_label.py`에 위치하고 있습니다.
아래는 해당 script 사용 예시 입니다.

```
# convert the official gt to rec_gt_label.txt
python gen_label.py --mode="rec" --input_path="{path/of/origin/label}" --output_label="rec_gt_label.txt"
```

아래 이미지 중
(a) 이미지는 원본 image이며
(b) 이미지는 (a) 이미지와 상응하는 label text file 입니다.

* Mulilingual Datasets

multi-language model 학습 방법은 chinese model 학습 방법과 동일합니다.
학습 데이터는 100만개의 합성 데이터로 구성됩니다.
작은 수량의 fonts와 test data는 아래 방법으로 다운로드할 수 있습니다.

(원본 url 참조)

___
## 1.4. Dictionary

모델 학습시 dictionary({word_dict_name}.txt)가 필요합니다.
모든 문자는 dictionary index에 mapping 되어야 합니다.

그러므로, 그러므로 dictionary 내에는 인식하고자하는 모든 문자가 포함되어 있어야 합니다.
또한 {word_dict_name}.txt 작성은 `utf-8` format으로 작성되어야 합니다.

```
l
d
a
d
r
n
```

`word_dict.txt` 파일에서, 각각의 line에 1개의 문자가 작성되어 있으며
해당 문자와 문자의 line number(index)는 서로 mapping된 상태 입니다.
이를테면 위 예시에서 "and"라는 문자열을 index로 표현한다면
[2 5 1]이 됩니다.

PaddleOCR은 여러 국가의 언어 dictionary를 기본으로 포함하고 있습니다.
* 한국어: `ppocr/utils/dict/korean_dict.txt`
* 영어: `ppocr/utils/en_dict.txt`

최근, multilingual model이 시험단계에 있으며
계속해서 새로운 언어를 추가하고 모델을 발전 시켜나갈것입니다.
**타국의 언어/font dictionary 제공 해주신다면 정말 감사하겠습니다.**

만약 필요하다면 dictionary file을 dictionary 폴더 내 위치할 수 있습니다.
만약 dictionary file을 수정할 예정이라면
`configs/rec/rec_icdar15_train.yml` 파일 내
`character_dict_path ` 항목을 당신의 dictionary file 위치로 수정해주세요.
추가로  `character_type`을 `ch`로 설정해주세요. < 이 부분은 더블 체크 필요

* Custom Dictionary
<위에서 설명 완료>

## 1.5. Add Space Category
"공백"을 인식하기 위해서는 YAML file 내 `use_space_char` 옵션을 `True`로 설정해야 합니다.

## 1.6. Data Augmentation
PaddleOCR은 다양한 데이터 증강 방법을 제공하며
모든 방법은 기본적으로 활성화되어있습니다.

기본적인 pertubation(변형/왜곡) 방법은 
`cvtColor`, `blur`, `jitter`, `Gasuss noise`, `random crop`, `perspective`,
`color reverse`, `TIA augmentation` 입니다.

각각의 disturbance(변형/왜곡) 방법은 학습 중 40퍼센트 확률로 선택됩니다.
구체적인 코드는 아래 경로에서 확인할 수 있습니다.
`ppocr/data/imaug/rec_img_aug.py`



___
___
# 2. Training

PaddleOCR은 training, evaluation, prediction에 대해 각각의 scripts를 제공합니다.
해당 section은 `PP-OCRv3` `English` 인식 모델 기준으로 설명됩니다.

## 2.1. Start Training
먼저, 당신은 `icdar2015` dataset으로 fine-tune된 pre-trained model을 다운로드할수 있습니다.
```
cd PaddleOCR/

# Download the pre-trained model of en_PP-OCRv3
wget -P ./pretrain_models/ https://paddleocr.bj.bcebos.com/PP-OCRv3/english/en_PP-OCRv3_rec_train.tar

# Decompress model parameters
cd pretrain_models
tar -xf en_PP-OCRv3_rec_train.tar && rm -rf en_PP-OCRv3_rec_train.tar
```

**Start training:**
```
# GPU training Support single card and multi-card training
# Training icdar15 English data and The training log will be automatically saved as train.log under "{save_model_dir}"

#specify the single card training(Long training time, not recommended)
python3 tools/train.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model=en_PP-OCRv3_rec_train/best_accuracy

#specify the card number through --gpus
python3 -m paddle.distributed.launch --gpus '0,1,2,3'  tools/train.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model=en_PP-OCRv3_rec_train/best_accuracy
```

PaddleOCR 학습-평가의 alternating을 지원합니다.
`configs/rec/rec_icdar15_train.yml` 내 `eval_batch_step` 옵션을 설정하여
학습 중 evaluation 빈도를 설정할 수 있습니다.
기본적으로, 500회 마다 evaluation을 진행합니다.
그리고 evalutaion이 진행되는 동안 best accuracy model은 `output/rec_CRNN/best_accuracy` 경로에 저장됩니다.

만약 evaluation dataset의 크기가 클 경우, 크기에 비례하여 시간이 소모될 것입니다.
이때 evalutaion의 수를 줄이거나 혹은 학습이 끝난 이후 evaluation을 진행하는 방법을 추천 드립니다.

* Tip: `-c` parameter를 사용하여 `configs/rec/` 경로 내 여러모델의 config file을 선택할 수 있습니다. 
rec 알고리즘은 [rec_algorithm](https://paddlepaddle.github.io/PaddleOCR/main/en/algorithm/overview.html)에서 확인해볼 수 있습니다.

Chinese data 학습에 대해서, [ch_PP-OCRv3_rec_distillation.yml](https://github.com/PaddlePaddle/PaddleOCR/blob/main/configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml) 사용을 추천 드립니다.
중국어 dataset에서 다른 알고리즘의 결과를 확인하고 싶다면, 아래 내용을 참고하여 `ch_PP-OCRv3_rec_distillation.yml` 파일을 수정하여 사용하세요.

 
```
Global:
  ...
  # Add a custom dictionary, such as modify the dictionary, please point the path to the new dictionary
  character_dict_path: ppocr/utils/ppocr_keys_v1.txt
  # Modify character type
  ...
  # Whether to recognize spaces
  use_space_char: True


Optimizer:
  ...
  # Add learning rate decay strategy
  lr:
    name: Cosine
    learning_rate: 0.001
  ...

...

Train:
  dataset:
    # Type of dataset，we support LMDBDataSet and SimpleDataSet
    name: SimpleDataSet
    # Path of dataset
    data_dir: ./train_data/
    # Path of train list
    label_file_list: ["./train_data/train_list.txt"]
    transforms:
      ...
      - RecResizeImg:
          # Modify image_shape to fit long text
          image_shape: [3, 48, 320]
      ...
  loader:
    ...
    # Train batch_size for Single card
    batch_size_per_card: 256
    ...

Eval:
  dataset:
    # Type of dataset，we support LMDBDataSet and SimpleDataSet
    name: SimpleDataSet
    # Path of dataset
    data_dir: ./train_data
    # Path of eval list
    label_file_list: ["./train_data/val_list.txt"]
    transforms:
      ...
      - RecResizeImg:
          # Modify image_shape to fit long text
          image_shape: [3, 48, 320]
      ...
  loader:
    # Eval batch_size for Single card
    batch_size_per_card: 256
    ...
```
**prediction/evaluation에서 사용하는 config file은 train에서 사용하는 config file과 일치해야 합니다.**

___

## 2.2. Load Trained Model and Continue Training
trained model을 load하여 학습을 진행할 경우, `Global.checkpoints` parameter를 명시할 수 있습니다.
```
python3 tools/train.py -c configs/rec/rec_icdar15_train.yml -o Global.checkpoints=./your/trained/model
```

**Note:** `Global.checkpoints`의 우선순위는 `Global.pretrained_model`보다 높습니다.
두개의 파라미터를 동시에 명시할 경우 `Global.checkpoints` model이 먼저 load됩니다.
만약 `Global.checkpoints` 모델이 잘못되었을 경우 그 다음 우선순위인 `Global.pretrained_model` 모델이 load됩니다.

___

# 2.3. Training with New Backbone

PaddleOCR의 network는 4개의 부분으로 구성되어 있ㅅ브니다..
(`ppocr/modeling` 경로에서 확인 가능)
```
├── architectures # Code for building network
├── transforms    # Image Transformation Module
├── backbones     # Feature extraction module
├── necks         # Feature enhancement module
└── heads         # Output module
```

데이터가 입력될 경우 각각 4개의 network를 통과하하게 됩니다.
(transforms -> backbones -> necks -> heads)

만약 Backbone을 PaddleOCR 내 구현된 다른 모델로 교체하고 싶을 경우,
config yml file 내 `Backbone` parameter를 수정해주어야 합니다.

그러나 완전히 새로운 Backbone을 사용하고 싶다면, 아래 절차를 숙지해야 합니다.

1. `ppocr/modeling/backbones` 경로에 `backbone.py` 파일을 생성
2. `backbone.py` 에 아래 샘플 코드를 추가
```
import paddle
import paddle.nn as nn
import paddle.nn.functional as F


class MyBackbone(nn.Layer):
    def __init__(self, *args, **kwargs):
        super(MyBackbone, self).__init__()
        # your init code
        self.conv = nn.xxxx

    def forward(self, inputs):
        # your network forward
        y = self.conv(inputs)
        return y
```
3. `ppocr/modeling/backbones/_init_.py` 파일에서 추가한 `backbone.py`을 imoprt 함.

network의 4개 모듈을 추가한 후, config yml file 내 아래와 같이 설정을 함.

```
  Backbone:
    name: backbone
    args1: args1
```
**NOTE:** backbone 관련 자세한 내용은 [알고리즘 doc](https://paddlepaddle.github.io/PaddleOCR/main/en/algorithm/add_new_algorithm.html) 을 참고하세요.

___
## 2.4. Mixed Precision Training

만약 학습 속도를 향상시키고 싶다면, [Auto Mixed Precision Training](https://www.paddlepaddle.org.cn/documentation/docs/en/guides/performance_improving/amp_en.html)을 설정할 수 있습니다.
아래는 단일 머신, 단일 gpu를 사용하는 예시 입니다.
```
python3 tools/train.py -c configs/rec/rec_icdar15_train.yml \
     -o Global.pretrained_model=./pretrain_models/rec_mv3_none_bilstm_ctc_v2.0_train \
     Global.use_amp=True Global.scale_loss=1024.0 Global.use_dynamic_loss_scaling=True
```

___
## 2.5. Distributed Training

멀티 머신, 멀티 gpu를 통한 학습을 한다면, `--ips` 파라미터로 IP address를 설정하거나 `--gpus`파라미터로 gpu id를 설정하세요.
```
python3 -m paddle.distributed.launch --ips="xx.xx.xx.xx,xx.xx.xx.xx" --gpus '0,1,2,3' tools/train.py -c configs/rec/rec_icdar15_train.yml \
     -o Global.pretrained_model=./pretrain_models/rec_mv3_none_bilstm_ctc_v2.0_train
```

**NOTE:** 
1. 멀티 머신 / 멀티 gpu를 사용하여 학습할 경우, 위쪽 커맨드에서 `ips` value를 수정해야 하며 각 머신 간의 통신(ping)이 가능해야 합니다.
2. 각 머신 별로 훈련 커맨드를 실행해주어야 합니다. 각 머신의 ip address를 확인하는 커맨드는 `ipconfig`입니다.
3. 분산 학습의 속도를 높히는 것에 대해서는 [분산 학습 튜토리얼](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/blog/distributed_training.html)을 참고해주세요.

___
## 2.6. Training with Knowledge Distillation

PaddleOCR은 문자 인식에 대해서 Knowledge distillation을 지원 합니다.
관련 내용은 [distillation doc](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/model_compress/knowledge_distillation.html)여기를 확인해주세요.

___
## 2.7. Multi-Language Model Training

PaddleOCR은 여러 언어를 지원합니다.

중국어, 영어, 프랑스어, 독일어, 일본어, 한국어, 라틴어, 아랍어, 키릴(러시아/불가리아), 데바나가리(산스크리터/힌디) 등을 지원합니다.

자세한 내용은 [Multi-language model](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/blog/multi_languages.html)을 확인해주세요.

만약 당신이 위에 나열한 언어를 fine-tuning하고 싶다면, 아래 내용을 읽고 config yml file을 수정해주세요.

* `rec_french_lite_train` file 예시
```
Global:
  ...
  # Add a custom dictionary, such as modify the dictionary, please point the path to the new dictionary
  character_dict_path: ./ppocr/utils/dict/french_dict.txt
  ...
  # Whether to recognize spaces
  use_space_char: True

...

Train:
  dataset:
    # Type of dataset，we support LMDBDataSet and SimpleDataSet
    name: SimpleDataSet
    # Path of dataset
    data_dir: ./train_data/
    # Path of train list
    label_file_list: ["./train_data/french_train.txt"]
    ...

Eval:
  dataset:
    # Type of dataset，we support LMDBDataSet and SimpleDataSet
    name: SimpleDataSet
    # Path of dataset
    data_dir: ./train_data
    # Path of eval list
    label_file_list: ["./train_data/french_val.txt"]
    ...
```

___
## 2.8. Tarining on other platform (Windows/macOS/Linux DCU)

- Window는 `single gpu`학습 및 추론만 지원합니다. 그러므로 `set CUDA_VISIBLE_DEVICES=0`와 `num_workers`는 0으로 설정해주시기 바랍니다.
- macOS는 GPU mode를 지원하지 않습니다. 그러므로 config yml file에서 `use_gpu` 파라미터를 `False`로 설정해주셔야 합니다. 그 외 환경은 Linux GPU 환경과 동일하게 세팅/사용 해주시면 되십니다.
- Linux DCU를 사용하기 위해서는 환경 변수을 `export HIP_VISIBLE_DEVICES=0, 1, 2, 3` 이와 같이 수정해야 합니다. 그 외에는 Linux GPU 환경과 동일하게 진행해주시면 되십니다.

___
## 2.9. Fine-tuning

실제 사용에 있어서 공식적인 (PaddleOCR) pre-trained model을 불러온 이후 자신만의 dataset을 통해 fine-tune 하는 것을 권장 딃니다.
문자 인식에 대한 fine-tuning에 대해서는 [fine-tuning doc](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/model_train/finetune.html)을 참고하시기 바랍니다.

___
# 3. Evaluation and Test

## 3.1. Evaluation

기본적으로 학습시 모델의 parameters는 `Global.save_model_dir` 에 설정한 경로에 저장 됩니다.
성능 지표를 평가할 때에는, `Global.checkpoints` 값을 설정하여 parameters가 저장되도록 해야합니다.
평가에 사용될 dataset은 `configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml` 파일 내 `Eval.dataset.label_file_list` 값을 미리 설정해주어야 합니다.

```
# GPU evaluation, Global.checkpoints is the weight to be tested
python3 -m paddle.distributed.launch --gpus '0' tools/eval.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.checkpoints={path/to/weights}/best_accuracy
```

___
## 3.2. Test

PaddleOCR을 통해 모델 학습을 할 경우, 아래 script를 참고하면 더 빠르게 예측 결과를 획득할 수 있습니다.

기본 예측 이미지는 `infer_img`에 저장되며, 학습된 가중치는 `-o Global.checkpoints`를 통해 지정합니다.

config yml file에 설정한 `save_model_dir`와 `svae_epoch_step` 값에 따라
아래 파라미터들이 저장됩니다.
```
output/rec/
├── best_accuracy.pdopt
├── best_accuracy.pdparams
├── best_accuracy.states
├── config.yml
├── iter_epoch_3.pdopt
├── iter_epoch_3.pdparams
├── iter_epoch_3.states
├── latest.pdopt
├── latest.pdparams
├── latest.states
└── train.log
```

예측 결과 중, `best_accuracy`가 평가 데이터 셋에 대해서 최고의 모델 입니다.
`iter_epoch_x`는  `save_epoch_step` 간격에 따라 저장된 모델 입니다.
`latest`는 가장 마지막 epoch 모델 입니다.

```
# Predict English results
python3 tools/infer_rec.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model={path/to/weights}/best_accuracy  Global.infer_img=doc/imgs_words/en/word_1.png
```

(중략)

예측에 사용된 config file은 반드시 학습에 사용된 config file과 일치해야 합니다.
이를테면 중국어 모델을 학습할 때 아래 config file을 사용했다면
`python3 tools/train.py -c configs/rec/ch_ppocr_v2.0/rec_chinese_lite_train_v2.0.yml`

예측을 할 때에도 동일한 config file을 사용해야 합니다.
`python3 tools/infer_rec.py -c configs/rec/ch_ppocr_v2.0/rec_chinese_lite_train_v2.0.yml -o Global.pretrained_model={path/to/weights}/best_accuracy Global.infer_img=doc/imgs_words/ch/word_1.jpg`

___
___
# 4. Model Export and Prediction

**추론 모델(`paddle.jit.save`로 저장된)**

추론 모델은 모델 구조와 파라미터가 파일에 저장된 상태인 "frozen" 상태 입니다.(더이상 변하지 않는다는 의미로써 frozen)
그리고 이는 보통 예측이나 배포에서 사용 됩니다.
`checkpoint model`은 오로지 모델 파라미터만 저장 되며 학습 재개 혹은 특수한 상황에서만 사용 됩니다.
checkpoint model과 비교를 한다면, 추론 모델은 모델의 구조 정보를 포함하고 있으며
이는 배포, 추론 속도 향상, 유연한 시스템 통합을 효과적으로 수행할 수 있도록 합니다.


문자 인식 모델을 추론 모델로 변환하는 작업은 문자 탐지 모델을 추론 모델로 변환하는 작업과 비슷 합니다.
아래 내용을 참고해주세요.

```
# Enable old IR mode
export FLAGS_enable_pir_api=0

# -c Set the training algorithm yml configuration file
# -o Set optional parameters
# Global.pretrained_model parameter Set the training model address to be converted without adding the file suffix .pdmodel, .pdopt or .pdparams.
# Global.save_inference_dir Set the address where the converted model will be saved.

python3 tools/export_model.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model=en_PP-OCRv3_rec_train/best_accuracy  Global.save_inference_dir=./inference/en_PP-OCRv3_rec/
```

자신의 데이터셋으로 학습한 모델이 다른 dictonary 파일을 사용한 경우, config file의 `character_dict_path`항목을 당신의 dictionary file 경로로 수정해야 합니다.

성공적으로 변환을 마친 이후, 모델이 저장되는 경로에 3가지의 파일이 생성됩니다.
```
inference/en_PP-OCRv3_rec/
    ├── inference.pdiparams         # The parameter file of recognition inference model
    ├── inference.pdiparams.info    # The parameter information of recognition inference model, which can be ignored
    └── inference.pdmodel           # The program file of recognition model
```

**Note:** 새로운 IR(Intermediate Representation) mode로 저장하고 싶다면, 다음 명령어를 참고해주세요.
```
export FLAGS_enable_pir_api=1
python3 tools/export_model.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model=./pretrain_models/en_PP-OCRv3_rec_train/best_accuracy Global.save_inference_dir=./inference/en_PP-OCRv3_rec/
```
성공적으로 변환되었다면 디렉토리에 2개의 파일이 생성되었을겁니다.
```
inference/en_PP-OCRv3_rec/
    ├── inference.pdiparams         # Model parameter file for the inference model
    └── inference.json              # Program file for the inference model
```

### Custom Model Inference
학습 중 text dictionary를 수정한 경우, 추론시에도 custom dictionary 경로를 명시해야 정확한 예측이 가능합니다.
추론시 하이퍼 파라미터 설정에 대해서는 [inference hyperparameters explanation tutorial](https://paddlepaddle.github.io/PaddleOCR/main/en/ppocr/blog/inference_args.html)을 참고해주세요.
```
python3 tools/infer/predict_rec.py --image_dir="./doc/imgs_words_en/word_336.png" --rec_model_dir="./your_inference_model" --rec_image_shape="3, 48, 320" --rec_char_dict_path="your_text_dict_path"
```
___
___
# 5. FQA

**Q1:** 어째서 추론 모델로 변환하기 전/후 예측 결과가 다른가요?
**A1:** 이는 일반적인 이슈 입니다. 보통은 전처리/후처리 파라미터가 학습/추론에 사용하는 것과 각각 다르기 때문에 발생합니다.
이를 해결하기 위해서는, 훈련시 사용한 config file과 추론시 사용한 config file 각각 전처리/후처리/예측 세팅이 일치하는지 확인해봐야 합니다.


