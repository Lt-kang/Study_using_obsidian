# Embedding_layer

## 핵심개념
### 어째서 Embedding layer를 학습하고 나면 유사한 단어들끼리 가까이 모이게 되는가?
Distributional Hypothesis(분포 가설): **같은 자리에 자주 등장하는 단어는 비슷한 의미일 가능성이 높다**라는 통계 패턴을 학습하는 것.

```
"apple" → appears with "fruit", "sweet", "eat", "red"
"banana" → appears with "fruit", "sweet", "eat", "yellow"
→ 둘 다 같은 context에서 자주 나옴 → 비슷한 임베딩 학습됨
```

## 수학적 원리 (Word2Vec 기준)
$$Loss = -LogP(context | center\_word) = -logSoftmax(embedding(center) - embedding(context))$$
* 중심 단어와 주변 단어의 내적(dot product)을 높이고, 다른 단어와의 내적은 낮추도록 학습함.
* 같은 context 끼리 내적(벡터 유사도)이 커지도록 학습됨
-> 결국 유사한 문맥의 단어들이 벡터 공간상에서 가까운 위치에 있게 됨


## Embedding 학습 방식들
|방식|대표 모델|특징|
|--|--|--|
|GloVe|Global Vectors|전체 코퍼스의 통계적 공기행렬 활용
|FastText|Facebook AI| subword 단위 embedding (OVV 대응이 강함)
|ELMo|AllenNLP|문맥 기반, 양방향 LSTM 사용
|BERT Embedding|Google|Transformer 기반 문맥 embedding
|Static vs Contextual|-|Wrod2Vec, GloVe -> Static / BERT, ELMo -> Contextual
