# WorkPiece

## 핵심 개념
* 자주 등장하는 단어 > 하나의 토큰
* 희귀한 단어 > 여러개의 서브워드로 분해

> ex)
> "unhappiness" → ["un", "##happi", "##ness"]
* `##`는 이전 토큰과 결합됨을 의미하며, 새로운 단어의 시작이 아님을 나타냄.


## WordPiece 작동 방식
1. 초기 vocab: 알파벳, 숫자, 특수문자, 기타 등등
2. 데이터에 등장하는 서브워드 빈도 계산
3. 서브워드를 병합하여 vocab 업데이트
    * 병합 기준: 최대 likelihood
4. 최종 vocab size가 될 때까지 반복

## WordPiece 예시

|입력한 단어|토크나이징 결과|
|--|--|
|playing|play, ##ing|
|unhappy|un, ##happi|
|electricity|electr, ##icity|
|tokenizer|token, ##izer|

## WordPiece 장점/단점

* 장점
    * OOV 해결: 희귀한 단어도 서브워드 조합으로 처리 가능
    * 어휘 크기 조절 가능
    * 말뭉치에 맞는 최적의 서브워드 생성 가능
* 단점
    * BPE보다 연산량이 큼
    * 토크나이저 학습이 복잡함.
    * 사전에 학습된 vocab이 고정됨

    

## Paper
[Original WordPiece 논문 (Google, 2016) "WordPiece: Subword Regularization for Neural Machine Translation"](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37842.pdf)

["BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"](https://arxiv.org/abs/1810.04805)