# OOV(Out of Vocabulary)란?

## 정의
* Vocabulary 내 없는 단어
* UNK 토큰으로 치환되며 의미가 손실되어 정상적인 출력이 어려움.

## 현대 NLP의 OOV 해결법
* Byte-Pair-Encoding
    * 전체 단어가 없더라도 서브워드 단위로 분해하여 의미 손실을 최소화 함.

* WordPiece
    * "strawberries" → ["straw", "##ber", "##ries"] (BERT 스타일)

* Unigram Language Model
    * 가장 자연스러운 서브워드 조합을 확률적으로 선택