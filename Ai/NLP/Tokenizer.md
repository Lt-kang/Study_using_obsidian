# 정의

Tokenizer란?
텍스트(문장)를 작은 단위(Token)으로 쪼개는 역할.
Token의 단위는 **단어, 서브워드, 문자** 등으로 설정함.
Tokenizer의 목적은
embedding layer에 입력하기 이전 token단위로 구분하기 위함임.


# 대표적인 Tokenizer

| 방식                             | 대표 LLM 모델                           | 특징 요약                       |
| ------------------------------ | ----------------------------------- | --------------------------- |
| Byte Pair encoding             | GPT-2 / RoBERTa / LLaMa             | 자주 나오는 문자/서브워드 병합           |
| WordPiece                      | BERT / DistilBERT                   | BPE와 유사하지만 병합 기준이 다름        |
| ULM(Unigram Language Model)    | SentencePiece (ALBERT, XLNet, T5 등) | 확률 기반 서브워드 선택               |
| Character-level Tokenizer      | GPT-Neo 등 특수 목적 모델                  | 모든 문자를 그대로 사용               |
| Byte-level BPE                 | GPT-2, GPT-3                        | Byte 단위로 처리 -> Unicode 무시   |
| SentencePiece (BPE or Unigram) | Google 계열 모델                        | 언어 독립적, preprocessing 없이 사용 |
| Word-level Tokenizer           | 고전 NLP 방식                           | 띄어쓰기 단위로만 나눔 (OOV 이슈 있음)    |


# 각 방식 비교

## BPE (Byte-Pair Encoding)
* 자주 등장하는 쌍을 병합
* 장점: [[OOV(Out of Vocabulary)]] 해결
* 단점: 의미 기준이 아닌 문자 빈도 기반


## WordPiece
* **BERT의 서브워드 토크나이저**
* BPE와 유사하되, 최대 likelihood 기반 병합 사용
* ex) `##ing`, `##ly` 같은 접미사 스타일 서브워드 사용
* BPE와의 차이점
    * BPE는 `running` → `run` `ning`
    * WordPiece는 `running` → `run` `##ning`

  
## (ULM) Unigram Language Model > SentencePiece
* 서브워드 후보군 전체를 확률적으로 평가
* 가장 가능성 높은 분할 조합을 선택
* `international` -> [`intern`, `ation`, `al`] or [`inter`, `national`] 중 높은 확률 선택
* 다중 분할 가능성 고려
* T5 / ALBERT / XLNet 등 사용


## Character-level Tokenizer
* 각 문자 하나하나가 토큰
* 희귀어, 신조어 대응은 가능하지만, 문자 처리량이 증가함.

  
## Byte-level BPE
* GPT-2/GPT-3 에서 사용함
* Unicode 무시, 256 byte 단위에서 토큰화
* 이모지, 특수문자, 다국어 등에 강함


## SentencePiece
* google에서 만든 독립형 tokenizer
* 언어 무관, 공백도 학습에 포함시킴.
* 내부적으로 BPE or Unigram 사용 가능
* 전처리 없이 학습 가능 (Hello world → _Hello _world)


## Word-level Tokenizer
* 띄어쓰기 기준으로 tokenize함. (고전적인 방식)
* [[OOV(Out of Vocabulary)]] 문제가 심각함.

