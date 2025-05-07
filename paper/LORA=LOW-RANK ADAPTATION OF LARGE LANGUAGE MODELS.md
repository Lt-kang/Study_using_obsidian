- LoRA: Low-Rank Adaptation: 모델의 가중치는 고정시킨 채 트랜스포머 아키텍처의 각 층에 훈련이 가능한 low-rank metrics를 삽입함으로써, 파인튜닝 시 필요한 파라미터 수를 크게 줄임.

* LoRA는 **사전학습된 가중치를 고정(freeze)** 한 채로, **변경되는 밀집층(dense layer)** 의 가중치 변화에 대해 **랭크 분해된 행렬**(rank decomposition matrices)을 학습합니다.


### LoRA는 왜 쓰는가?
1. 기존 fine-tune에서는 model의 parameters를 gpu에 올려서 학습해야했기에 상당히 큰 vram이 필요했다. 하지만 LoRA는 pretrained-model의 parameters는 고정된 채 Low-rank만 tuning하기 때문에 vram을 절약할 수 있다.
2. 또한 기존 fine-tune된 model을 저장할 경우에는 기존 parameters까지 전부 저장해야해서 용량이 컸지만 LoRA의 경우 Low-rank metrics만 저장하면 되기 때문에 저장 공간 또한 절약할 수 있다.
3. LoRA는 단순한 선형구조이다. 그렇기 때문에 추론시 시간이 지연되지 않는다!! (기존 모델 추론 시간과 거의 비슷하다.)

![[Pasted image 20250401012309.png]]



- LoRA는 반드시 LLM에서만 사용되는 것은 아님! 대표적으로 Stable Diffusion에서도 LoRA가 많이 사용됨.
- 

ref
Li et al. (2018a), Aghajanyan et al. (2020)
