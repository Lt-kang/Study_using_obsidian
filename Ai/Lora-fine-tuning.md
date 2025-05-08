# 1. ✅ 예시: 계산기와 위키 검색을 사용하는 Agent
```
from langchain.agents import initialize_agent, Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper

# 툴 정의 (DuckDuckGo, 계산기)
search = DuckDuckGoSearchRun()
tools = [
    Tool(name="Search", func=search.run, description="Useful for web search."),
]

# LLM (OpenAI 예시)
llm = ChatOpenAI(temperature=0)

# Agent 초기화
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 실행
agent.run("지금 한국의 대통령은 누구야?")
```

___

# 2. QLoRA vs LoRA
LoRA: 기존 LLM 파라미터를 freeze한 채, 일부 weight에만 low-rang marix를 추가하는 학습 방식
QLoRA: LoRA 기반 학습이지만 base 모델을 4-bit로 quantization하여 훨씬 더 작은 vram으로 학습 가능.


## 📊 QLoRA vs LoRA 요약 비교

|항목|LoRA|QLoRA|
|--|--|--|
|Base model precision|FP16, BF16|4-bit quantized (int4)|
|Adapter precision|FP16 / BF16|FP16 / BF16|
|VRAM 사용량|적음|매우 적음|
|성능|Full fine-tuning에 근접|LoRA 수준 유지|
|구현 복잡도|낮음|약간 높음 (bnb, quantization_config 필요)|
|대표 라이브러리|peft|peft + bitsandbytes|


## LoRA config 설정
```
# LoRA config 
from peft import LoraConfig

lora_config = LoraConfig(
    r=64,
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
    )
```

## QLoRa config 설정
```
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model

# 1. QLoRA용 양자화 설정
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16  # 또는 float16
)

# 2. 모델 로딩 (4bit quantized)
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",  # 또는 다른 모델
    quantization_config=bnb_config,
    device_map="auto"
)

# 3. LoRA 설정 그대로 사용 가능
lora_config = LoraConfig(
    r=64,
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# 4. LoRA 적용
model = get_peft_model(model, lora_config)
```

___

# 3. QLoRA 환경에서 RAM 최적화 전략

## Datasets 라이브러리 효율적으로 사용하기
```
from datasets import load_dataset

# 1. streaming으로 RAM 절약
dataset = load_dataset("your_dataset", split="train", streaming=True)

# 2. map 할 때 batched=True + remove_columns
dataset = dataset.map(your_preprocess_fn, batched=True, remove_columns=["text", "label"])
```
|전략|설명|
|------|------|
|`streaming=True`|전체 데이터를 RAM에 올리지 않고, 한 줄씩 처리|
|`remove_columns`|사용하지 않는 열 제거하여 RAM 절약|
|`batched=True`|처리 횟수 줄여 속도 개선 + 메모리 효율|


## Tokenizer 사용시 메모리 최적화
```
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf", use_fast=True)

# 1. padding, truncation 설정 필수
def tokenize_fn(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

```
|전략|설명|
|------|------|
|`trauncation=True`|긴 텍스트로 인한 OOM 방지지|
|`padding="max_length"`|batching 정렬 최적화화|
|`max_length` 제한|메모리 관리 핵심!|


## Trainer 구성시 RAM 고려 세팅
```
from transformers import TrainingArguments

training_args = TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    fp16=True,
    bf16=False,  # bfloat16은 GPU에서만 작동, CPU RAM에 영향 없음
    dataloader_num_workers=2,  # 너무 높이면 RAM 과부하
    logging_steps=10,
    save_steps=500,
    save_total_limit=2,
    report_to="none",
)
```
|전략|설명|
|------|------|
|`gradient_accumulation`|batch size 대신 누적 계산|
|`dataloader_num_workers`|많으면 빠르지만 RAM을 많이 씀 (2~4 추천)|
|`save_total_limit`|체크 포인트로 RAM/disk 낭비 방지|


## Quantization 설정 최적화
```
BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
```
✅ RAM 절약 효과
* `double_quant=True`: 2단계 양자화로 RAM + VRAM 모두 절약  
* `nf4`: 일반적 NLP에 적합한 비손실 4bit quant  
* `compute_dtype=bfloat16`: 연산 효율 + 낮은 precision


## 학습 중 메모리 최적화
```
# Gradient Checkpointing 활성화
model.gradient_checkpointing_enable()

# Compile 또는 TorchDynamo (선택사항)
torch.compile(model)  # PyTorch 2.0 이상에서만
```
|효과|설명|
|--|--|
|Checkpointing|중간 결과 저장 안 하고 다시 계산 (RAM 사용량↓, 속도↓)
|torch.compile|그래프 최적화로 메모리 사용량 줄일 수 있음 (PyTorch 2.0)


## ✅ 정리 요약

| 전략 | 설명 |
|------|------|
| datasets streaming 사용 | 전체 로딩 대신 한 줄씩 처리 |
| Tokenizer truncation | 무한 메모리 점유 방지 |
| Dataloader num_workers 감소 | RAM 사용량 급감 |
| Gradient checkpointing | RAM/VRAM 둘 다 줄일 수 있음 |
| BitsAndBytesConfig 세팅 최적화 | 메모리 효율적 모델 로딩 가능 |


___

# 4. LoRA에서 rank는 항상 2의 제곱수만 써야할까?

```
LoraConfig(
    r=64,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
```

정답: 아니다! 하지만 2의 제곱수를 사용하는게 가장 효과적이다.

Loraconfig의 `r`파라미터(rank)는 어떤 수 든 입력할 수 있다.  
하지만 GPU 연산 구조상, maxtrix multiply 연산에서 2의 제곱수 크기가 더 빠르고 효율적이다!  
`CUDA`, `cuBLAS`, `TensorCore`는 2 4 8 16 32 등 **aligned size** 일 때 연산 최적화가 잘된다!  
그렇기에 학습 속도 및 메모리 효율 면에서 2의 제곱 수가 선호된다.

___

# 5. Aligned size가 뭐야?

메모리나 연산 단위가 하드웨어에서 가장 효율적으로 처리될 수 있도록 **정렬된 크기(aligned size)** 를 말함.  

4번 질문에서 연계로 계속 답변하자면
gpu의 텐서 연산 유닛은 한번에 16개의 float값을 병렬로 처리한다고 가정했을 때  
입력 벡터의 길이가 17이라면??

앞 16개는 한 번에 처리되고 나머지 1개는 따로 처리됨.   
이때 1개만 따로 처리되는 유닛에서 15개의 슬롯은 유휴 상태(idle cycle)임.(낭비 발생)

즉, 이를테면 input data를 32개의 float를 처리한다고 할 때  
`r`을 17로 설정한다면  
16 - 1 - 15 총 세번의 연산이 필요하지만  

`r`을 16으로 설정한다면  
16 - 16 두번의 연산만 진행됨.  


**물론 gpu 아키텍처에 따라 다를 수 있어**   
이를테면 작은 연산을 여러 작업과 fuse 시킨다던가
데이터 배열을 aligned memory block으로 재정렬 한다던가 등





## 🧠 요약 한 줄
GPU 텐서 유닛은 정해진 크기 단위로 연산하며, 이 크기에 안 맞으면 성능 낭비가 발생한다.


