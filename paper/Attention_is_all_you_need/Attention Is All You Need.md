# Abstract
기존의 Sequence transduction model들은 encoder-decoder를 포함하는 복잡한 순환신경망([[RNN]]) 혹은 합성곱 신경망([[CNN]])에 기반을 두고 있습니다.
가장 성능이 좋은 모델 또한 encoder와 decoder를 [[attention mechanism]]으로 연결하기도 합니다.

해당 논문에서는 순환 구조, 합성곱을 완전히 제거한 attention 메커니즘만을 기반으로 하는 모델인 Transformer를 제안합니다.

두 가지 기계 번역 과제에 대한 실험에서, Transformer는 성능 면에서 더 우수할 뿐만 아니라
병렬화가 용이하고 학습에 필요한 시간 또한 크게 감소하였습니다.
Transformer는 WMT 2014 영어-독일어 번역 **과제에서** [[BLEU]] 점수 28.4를 기록하였습니다.(이는 기존 최고 성능 대비 2점 이상 높은 결과 입니다.)
WMT 2014 영어-프랑스어 번역 과제에서는 단일 모델 기준 [[BLEU]] 점수 41.8을 달성했으며, 이는 8개의 GPU에서 3.5일 동안 학습한 결과로, 기존 최고 모델 대비 훨씬 적은 학습 비용을 요구합니다.

또한 Transformer가 영어 구문 분석(English constituency parsing) 등 다른 작업에서도 대규모 및 제한된 데이터 모두에서 잘 일반화되는 것을 보였습니다.


# 1. Introduction
[[RNN]], [[LSTM]], [[GRU]] 등의 언어 모델링과 기계 번역(Seq2Seq)과 같은 시퀀스 모델링 및 변환 문제에서 SOTA 모델에 달성하였습니다.
이후 수많은 연구들이 순환 언어 모델과 encoder-decoder 구조의 한계를 뛰어넘기 위해 노력해 왔습니다.

순환 모델은 본질적으로 순차적인 (연산) 특성 때문에, 학습 예제 내에서 **병렬화가 어렵고**, 시퀀스가 길어질수록 **메모리 제약**으로 인해 예제 간 batch size가 제한됩니다. 최근 연구에서는 연산 분해 기법과 조건부 연산을 통해 계산 효율성을 크게 높이고, 후자의 경우 성능도 개선했습니다.
그러나 **순차적 연산이라는 근본적인 제약은 여전히 남아 있습니다.**

[[attention mechanism]]은 다양한 작업에서 강력한 시퀀스 모델링 및 변환 모델의 필수 요소가 되었으며,
입력 또는 출력 시퀀스 내에서 거리와 상관없이(RNN 계열 모델과는 반대로) 의존성을 모델링 할 수 있게 해줍니다.
그러나 대부분의 경우, **[[attention mechanism]]은 순환 신경망과 함께 사용되고 있습니다.**

해당 논문은 순환 구조를 완전히 제거하고, 입력/출력 간의 전역적 의존성을 오직 [[attention mechanism]]에만 의존하여 학습하는 Transformer라는 모델 아키텍처를 제안합니다.
Transformer는 훨씬 더 높은 수준의 병렬화가 가능하며, 8개의 P100 GPU에서 12시간만 학습해도 새로운 번역 품질의 SOTA를 달성할 수 있습니다.


# 2. Background
생략


# 3. Model Architecture
![[Pasted image 20250529141925.png]]
**Encoder**는 입력 시퀀스 $(x_{1}, x_{2}, x_{3} ... x_{n})$을 연속적인 표현의 시퀀스 $z = (z_{1}, ... z_{n})$ 으로 변환 합니다.
이 $z$를 바탕으로 **Decoder**는 출력 시퀀스 $(y_1, ... y_m)$ 을 한 번에 하나씩 생성합니다.
각 단계에서 모델은 auto-regressive하게, 즉 이전에 생성된 심볼들을 다음 심볼 생성 시 추가 입력으로 사용합니다.

Transformer는 위의 전체 구조를 따르되, 인코더와 디코더 모두에 대해 `stacked self-attention`과 `point-wise`, `fully connected layers`을 사용합니다.

___
## 이해를 위한 추가 내용
- **Encoder**
	- 자연어 문장을 컴퓨터가 이해할 수 있는 Vector로 변환해주는 역할
- **Decoder**
	- Encoder에서 생성된 Vector를 받아서, 출력 Vector(자연어로 변환됨.)으로 변환해주는 역할
- **auto-regressive**
	- 출력 문장을 한번에 다 만드는 게 아니라, 한 단어씩 차례대로 만든다는 의미!
	  !!!) 이래서 streamlit-lanchain 프로덕트에서 stream 단위로 답변을 출력할 수 있는거구나
	- 이전에 만든 단어들을 참고해서 다음 단어를 만들어냄.
	- ex)
	  1. Decoder가 Encoder의 정보를 확인하여 "저는"을 생성함.
	  2. "저는"을 참고해서 "저는 학생"을 생성함. (Encoder 정보 + "저는")
	  3. 그 다음, "저는 학생"을 참고해서 "저는 학생입니다"를 생성함. (encoder 정보 + "저는 학생")
	  - 이 모든 과정에서 Encoder의 정보는 계속해서 참고함!
  - **Positional encoding**
	  - Transformer는 RNN/CNN과 달리 입력 시퀀스의 순서(위치) 정보를 직접 알 수 없음.
		  - RNN > 순차적 처리
		  - CNN > 커널 이동
		  - Transformer > attention 메커니즘으로 한 번에 병렬 연산
	  - 그래서, 토큰의 "순서" 정보를 인공적으로 embedding vector에 더해줌 (Positional Encoding)
	  - 각 토큰 embedding vector에 pos에 대한 고유값(sin/cos function)을 더함
	  - 이로써 모델이 "첫 번째 단어", "세 번째 단어"처럼 위치 정보를 파악할 수 있게 됨.
	  $$PE_{(pos,2i)}=sin⁡(pos/10000^{2i/d_{model}})$$$$PE{(pos,2i+1)}=cos⁡(pos/10000^{2i/d_{model}})$$
	- Encoder Block의 PE
		- encoder가 입력 시퀀스에서 단어들의 순서 정보를 인식할 수 있게 해줌.
		- attention layer에서 어떤 단어가 어디 위치에 있는지 구분 가능
	- Decoder Block의 PE
		- 지금깢 생성한 출력 토큰에 대해 위치 정보 사용
		- Encoder의 PE와 달리 Decoder에는 마스킹이 추가로 들어감
		- 생성할 때마다 아직 생성되지 않은 "미래 위치"는 마스킹해서 어텐션 불가
___

# 3.1 Encoder and Decoder Stacks
### Encoder
### Decoder
