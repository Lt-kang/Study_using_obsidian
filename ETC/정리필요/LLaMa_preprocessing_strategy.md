# LLaMa preprocessing 

## 1. Text Cleaning
* 중복 제거
    * 같은 내용이 여러번 포함될 경우 overfitting 위험이 있으므로 유사 문서 제거
    * 중복 유사도 제거 기준: **MinHash / Locality Senstive Hashing / Cosine Similarity, Jaccard Similarity**

* 깨진 문자 / HTML tag / 컨트롤 문자 제거
    * `\x00`, `<div>`, `\u200b` 등의 노이즈 문자 제거

* 긴 공백, 특수 기호 반복 제거
    * `!!!!!!!!`, `------`, `******` 같은 비자연스러운 패턴 제거

* Non-language Text 제거
    * 코드 / 로그파일 / 숫자 나열 / 바이너리 디코딩 등은 제외되거나 별도 처리


## 2. filtering Bad Samples
* Language Identification
    * 원하지 않는 언어 제거 (ex. 영어 모델일 경우 한국어 제거)
    * FastText 기반 언어 감지 사용.

* 길이 필터링
    * 너무 짧거나 너무 긴 문장은 학습에 도움이 안되므로 삭제
    * ex. 10 token 이하 / 2048 token 초과 문장 제외

* 비속어 / 유해 컨텐츠 필터링
    * Toxic, offensive, harmful 콘텐츠 제거
    * 자체 정의한 금지어 리스트
    * HuggingFace Datasets 기반 필터링 사용.

* Low Quality Corpus Filtering
    * 품질 낮은 데이터셋(ex. reddit, forum scraps)은 필터링하거나 가중치를 낮게 부여


## 3. domain balancing
* 학습 데이터가 특정 도메인에 과하게 치우지지 않도록 분포를 조정
* ex) Wikipedia 10%, Books 20%, Web Crawl 50%, Academic 20% 등으로 구성.


## Sub-word tokenizer
* BPE(Byte-Pair Encoding) 기반 SentencePiece tokenizer 사용
    * LLama 2 > 32k vocabulary BPE 기반 tokenizer 사용.
    * Byte-level으로 동작하므로 표제어/어간 추출 없이 다양한 형태 처리 가능.


___
# 5️⃣ 관련 논문 / 공식 자료 링크
## 📄 논문
LLaMA 1: https://arxiv.org/abs/2302.13971  
“LLaMA: Open and Efficient Foundation Language Models”

LLaMA 2: https://arxiv.org/abs/2307.09288  
“LLaMA 2: Open Foundation and Fine-Tuned Chat Models”

## 📂 모델/토크나이저 코드
HuggingFace Tokenizers: https://github.com/huggingface/tokenizers  
Meta LLaMA GitHub (공식 코드 비공개 → 리팩 버전):
https://github.com/facebookresearch/llama