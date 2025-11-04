# NLP Flow
```
1️⃣ Text Preprocessing (Tokenization)
   ↓
2️⃣ Feature Extraction (Tokenization + Embedding 역할)
   ↓
3️⃣ Modeling (통계적 or 머신러닝 기반)
   ↓
4️⃣ Evaluation / Inference
```

# 1. Text Preprocessing
## 목표
- 텍스트를 기계가 다룰 수 있게 정제하는 단계
- Tokenization

## 작업
- Lowercasing
- Stopword 제거
	- "the", "a" 등
- Lemmatization / Stemming
	- ex. runs -> run
- POS Tagging (품사 태깅)
- Named Entity Recognition (고유명사 인식)
- Tokenization (문장을 단어 단위로 쪼개기)


# 2. Feature Extraction
## 목표
- 텍스트를 숫자로 표현하기
- Tokenization + Embedding Layer
	- 단, Classical NLP에서는 Embedding layer가 아니라 featrue extraction step이라 부름.

## 작업
- BoW (Bag-of_Words)
	- 각 단어의 출현 횟수를 벡터로 표현
- TF-IDF (Term Frequency - Inverse Document Frequency)
	- 단어의 중요도를 반영한 벡터 표현
- n-gram
	- 단어 조합을 고려 (ex. New Work)
- Word2Vec / GloVe / FastText
	- 단어의 의미를 벡터 공간에서 학습(신경망 기반)


# 3. Modeling
## 목표
- Featrue를 이용해 작업 수행
- Model layer

## 작업
- 통계적 모델: Naive Bayes, Logistic Regression, SVM
- Sequence 모델: Hidden Markove Model(HMM), Conditional Random Field(CRF)
- Neural 전환기: RNN, LSTM (여기서부터 신경망)


# 4. Evaluation / Inference
- Accuracy, Precision, Recall, F1-score
- BLEU, ROUGE (번역/요약 등)



# 요약
|구분|Classical NLP 용어|Neural NLP 용어|
|---|---|---|
|Tokenizer|Tokenization|Tokenizer|
|Embedding|Feature Extraction (BoW, TF-IDF, Word2Vec 등)|Embedding Layer|
|Model|Statistical / ML Model|Neural Network Layer|

## 종합 흐름 요약
```
Raw Text
   ↓
Preprocessing (Tokenization, Lemmatization)
   ↓
Feature Extraction (BoW, TF-IDF, Word2Vec)
   ↓
Modeling (Naive Bayes, SVM, CRF, LSTM)
   ↓
Evaluation (Accuracy, BLEU, Perplexity)
```