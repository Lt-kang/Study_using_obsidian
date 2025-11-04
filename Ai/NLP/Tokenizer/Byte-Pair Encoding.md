# Byte-Pair Encoding

# 개념
Byte-Pair Encoding(이하 BPE)는 원래 데이터 압축 알고리즘에서 유래된 기법.  
NLP에서는 희소한 단어들을 더 작은 단위(sub-word)로 분해/결합하여 고정된 어휘 집합(vocabulary)을 만드는데 사용됨.

LLaMa / GPT / RoBERTa 등 모델에서 사용되는 서브워드 토크나이저 중 하나

* `데이터 압축`과 `서브워드 토크나이징`의 핵심 아이디어는 유사함 > "자주 등장하는 패턴을 효율적으로 표현한다."

* BPE의 목적 > 반복되는 문자 쌍 압축
    * 자주 등장하는 Text를 하나의 심볼로 치환하면서 데이터를 줄임
    * ex) abcabcd -> `abc`를 `X`로 치환 -> XXd


# Byte-Pair Encoding을 사용하는 이유
* `OOV`(Out-of_vocabulary) 문제 해결을 위해 사용 > 단어를 서브워드 단위로 분해하면 처음 등장한 단어도 의미있게 사용 가능
    * ex) vocabulary 내 `초코`와 `아이스크림`은 있지만 `초코 아이스크림`은 없을 경우 새로운 단어(`초코 아이스크림`)이 등장하더라도 Tokenize 가능.

* 희소성 문제 해결 > 자주 등장하는 단어는 병합, 드물게 등장하는 단어는 작은 단위로 분리
* 고정된 vocab 크기 유지 가능 > 전체 단어 수가 아닌 서브워드 조합으로 처리


# 장점과 단점
|장점|단점|
|--|--|
|희귀 단어 처리 가능|의미 단위 고려 없이 병합됨|
|어휘 크기 조절이 쉬움|형태소 분석보다 정밀함이 부족함|
|빠른 전처리 가능|같은 의미 단어라도 다르게 분해될 수 있음|


# Python 구현
```
from collections import defaultdict, Counter

# 초기 단어 리스트 (각 단어 끝에 </w> 추가 → 단어 경계 표시용)
corpus = ['low', 'lowest', 'newer', 'wider']
vocab = {}

# 각 단어를 문자 단위로 나누고, 마지막에 </w> 붙임
for word in corpus:
    tokens = " ".join(list(word)) + " </w>"
    vocab[tokens] = vocab.get(tokens, 0) + 1

def get_stats(vocab):
    """ 문자쌍(바이그램) 빈도 계산 """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, vocab):
    """ 가장 자주 등장한 쌍을 병합 """
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        # 병합 대상 쌍만 공백 없이 치환
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

# 학습 과정 실행
num_merges = 10  # 병합 횟수 제한
for i in range(num_merges):
    print(f"\nStep {i+1}:")
    pairs = get_stats(vocab)
    if not pairs:
        break
    best_pair = max(pairs, key=pairs.get)
    print(f"Most frequent pair: {best_pair}")
    vocab = merge_vocab(best_pair, vocab)
    print("Updated vocab:")
    for word in vocab:
        print(f"  {word} → {vocab[word]}")
```

# Paper
[Gage, Philip (1994). "A New Algorithm for Data Compression"](https://dl.acm.org/doi/10.5555/177910.177914)  
**핵심**["Neural Machine Translation of Rare Words with Subword Units" (Sennrich et al., 2015)](https://arxiv.org/abs/1508.07909)  
[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)



# HuggingFace
[HuggingFace `tokenizers` 라이브러리](https://github.com/huggingface/tokenizers)