# 자연어처리 전처리 단계

## 1. text Cleansing
* 데이터에 포함된 불필요한 문자를 제거해서 모델 학습에 방해되는 요소를 줄여줍니다.
```
import re

text = "안녕하세요!! 😊 오늘 날씨가 정말 좋아요~~ <html>태그</html>"
cleaned = re.sub(r"[^가-힣\s]", "", text)  # 한글과 공백만 남기기
print(cleaned)  # → "안녕하세요 오늘 날씨가 정말 좋아요 태그"
```

___
## 2. Tokenization
* 문장을 의미 있는 단위(단어 or 형태소)로 나누는 작업
* 한글의 경우 **형태소 분석기**가 필요. (KoNLpy > Hannanum / Kkma / Komoran)
```
# 영어
from nltk.tokenize import word_tokenize

sentence = "Natural language processing is fun."
tokens = word_tokenize(sentence)
print(tokens)  # ['Natural', 'language', 'processing', 'is', 'fun', '.']

# 한글
from konlpy.tag import Okt

okt = Okt()
tokens = okt.morphs("자연어 처리는 재미있어요.")
print(tokens)  # ['자연어', '처리', '는', '재미있어요', '.']
```

___
## 3. Stopword Removal
* 모델 학습 및 분석에 큰 의미가 없는 단어 등을 제거합니다.
```
stopwords = ['은', '는', '이', '가', '을', '를', '에', '의', '도']
filtered = [word for word in tokens if word not in stopwords]
print(filtered)  # ['자연어', '처리', '재미있어요', '.']
```

___
## 4. Stemming / Lemmatization
* 단어의 다양한 변형을 기본 형태로 통일하여 모델이 더 일반화할 수 있도록 만듦.
* `Stemming`: 규칙 없이 단순히 어간만 남김
```
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print(stemmer.stem("running"))      # run
print(lemmatizer.lemmatize("running", pos='v'))  # run
```

* `Lemmatization`: 문법적 분석 기반으로 원형을 찾음 (한글의 경우 형태소 분석기로 기본형을 얻을 수 있음.)
```
okt.pos("먹었습니다", stem=True)  # [('먹다', 'Verb')]
```

___
## 5. POS Tagging
* 단어의 품사를 태그로 부여하여 문맥 이해에 도움을 줌.
* 이 역시 한글은 형태소 분석기를 사용할 수 있음.
```
print(okt.pos("자연어 처리는 어렵지 않아요"))  
# [('자연어', 'Noun'), ('처리', 'Noun'), ('는', 'Josa'), ('어렵지', 'Adjective'), ('않아요', 'Verb')]
```


___
## 6. Vectorization
* 모델(컴퓨터)이 이해할 수 있도록 텍스트를 숫자로 변환함.

* 대표적인 Vecorization model
    * BoW (Bag of Words): 단어 빈도
    * TF-IDF: 중요도 반영
    * Word Embedding: 의미 정보 반영(Word2Vec, GloVe)


___
## 7. Vocabulary Filtering
* 너무 자주(혹은 드물게) 나오는 단어를 제거하여 노이즈를 줄임.

```
from collections import Counter

words = ['자연어', '처리', '자연어', '모델', '학습', '모델']
word_counts = Counter(words)
filtered = [w for w in words if word_counts[w] > 1]
print(filtered)  # ['자연어', '처리', '자연어', '모델', '모델']
```


___
## 8. ETC
* 정규 표현식을 사용한 패턴 정리
* 숫자, 영어, 단어 변환 or 제거
* 표제어 사전 또는 사용자 정의 사전 적용
* 철자 교정


___
# 요약
|단계|주요 목적|대표도구|
|--|--|--|
|1. Text Cleaning|불필요한 문자 제거|정규표현식|
|2. Tokenization|단어/형태소 분리|NLTK, KoNLPy, Okt|
|3. Stopword Removal|의미 없는 단어 제거|사용자 정의|
|4. Stemming / Lemmatization|단어 통일화|Stemmer, Lemmatizer, 형태소 분리기(한국어의 경우)|
|5. POS tagging|문맥 분석|Okt.pos|
|6. Vectorization|수치화|BoW, TF-IDF, Embedding|
|7. Vocabulary Filtering|희소성 감소|빈도 필터링|