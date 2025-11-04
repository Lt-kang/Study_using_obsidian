# LLM vs NLP preprocessing compare

## 비교
* LLM에서도 **Text Cleansing**은 여전히 중요
* Stopword Removal / POS Tagging / Stemming & Lemmatization 은 사용하지 않음
    * 학습 데이터의 맥락 속에서 직접 학습하기에 `Stemming` 불필요
    * LLM은 문장 내에서 단어 의미를 문맥적으로 처리 가능. (Embedding Layer) 그러므로 `Lemmatization` 불필요
* 고급 토크나이저(BPE / WordPiece)를 중심으로 처리
* 데이터 품질 관리 중요 (중복, 오염, 비속어)


|구분|NLP|LLM|
|--|--|--|
|Tokenization|형태소 분석기 or 특정 규칙 기반 토큰화|BPE, WordPiece, SentencePiece, Byte-level BPE 등의 tokenizer 사용|
|Stopword removal|제거|제거하지 않음. 모든 단어/문장 구조가 의미가 있으며 모델이 알아서 맥락을 이해하기 때문|
|Stemming & Lemmatization|사용|사용하지 않음. LLM은 문맥 기반으로 의미를 파악하기 때문
|POS tagging|명시적 사용|LLM은 내부에서 문맥으로 품사를 유추함
|Vectorization|BoW, TF-IDF, Word2Vec|사용하지 않음. Embedding layer에서 자동으로 생성됨
|text Cleansing|특수 문자 등 제거|LLM 또한 기본적인 정제는 적용함


## NLP와 LLM의 전처리가 다른 이유
* LLM은 Transformer 구조를 이용하여 어휘 정제 없이도 문맥을 이해할 수 있음.
* Stopword 또한 맥락에 따라 중요한 단서가 될 수 있기에, 제거할 경우 model 성능이 떨어질 수 있음.
* Stemming / Lemmatization을 하지 않는 이유는, LLM이 내부적으로 품사/어간 정보를 추론해낼 수 있기 때문.


## ETC
* LLM에서의 Text Cleaning
    * HTML 태그 / 깨진 텍스트 / 불필요한 유니코드 등 제거

* LLM에서 사용하는 Tokenizer
    * GPT > Byte-level BPE
    * BERT > WordPiece
    * T5 > SentencePiece

* LLM 데이터 품질 작업
    * 중복 제거
    * 너무 짧거나 너무 긴 문장 제거
    * 인종차별/욕설/비속어 제거 (Content filtering)

* 언어 통일 처리
    * Multi-lang data에서는 언어별 전처리/언어 태그 부여


