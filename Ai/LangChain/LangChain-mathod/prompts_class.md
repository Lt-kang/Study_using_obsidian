# MessagesPlaceholder

## 정의
* 채팅 대화 메시지를 프롬프트에 삽입할 수 있도록 만드는 placeholder
* memory 객체가 placeholder에 message를 채워 넣음.

## 사용 목적
* memory(`ConversationBufferMemory`)등을 사용할 때
* Agent나 ChatChain이 대화 context를 기억하게 만들고 싶을 때


## 예시 코드
```
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# 1. Memory 설정
memory = ConversationBufferMemory(return_messages=True)

# 2. Prompt 구성
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# 3. LLM 연결
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 4. Chain 생성
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# 5. 대화 수행
print(chain.invoke({"input": "안녕"}))
print(chain.invoke({"input": "LangChain이 뭐야?"}))
```
___


# ChatPromptTemplate

## 정의
* Chat 모델(OpenAi, Claude)과 대화할 때 사용되는 프롬프트 메시지 집합을 템플릿 형태로 구성할 수 있게 해주는 class
* LLM에게 대화형 메시지(system / human / ai)를 구조적으로 전달하기 위해 사용

## 사용 목적
* LLM에게 system / human / ai / placeholder message를 전달하기 위해 사용
* 멀티턴 프롬프트, 커스터마이징 가능한 메시지 패턴 구성
* memory나 tools와 쉽게 연동됨

## 예시 코드
```
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 유용한 한국어 AI 어시스턴트야."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])
```
___


# PromptTemplate

## 정의
* `jinja2` 혹은 `f-string` 스타일로 템플릿을 작성하고 변수값을 주입하여 동적으로 문자열 생성 가능하게 하는 class

## 사용 목적
* prompt 재사용
* parameter 기반 prompt 구성
* prompt version 관리 및 template화 가능


## 예시 코드
```
from langchain.prompts import PromptTemplate

# 프롬프트 템플릿 정의
prompt = PromptTemplate(
    input_variables=["language", "topic"],
    template="Write a short essay in {language} about the topic: {topic}."
)

# 템플릿에 변수값 주입하여 프롬프트 생성
final_prompt = prompt.format(language="English", topic="Artificial Intelligence")
print(final_prompt)
```
___

# FewShotPromptTemplate

## 정의
* few-shot learning을 위해 사용되는 prompt template class
* 예시들을 자동으로 포함시켜서 LLM이 그 패턴을 학습한 후, 새로운 입력에 대해 예측할 수 있도록 하는 template

## 사용 목적
* LLM에게 예시를 제공해서 정답의 패턴을 학습 시킴.
* `PromptTemplate` + `examples` = `FewShotPromptTemplate`

## 예시 코드
```
FewShotPromptTemplate(
    examples: List[Dict[str, str]],           # 예시들 (input-output 쌍)
    example_prompt: PromptTemplate,           # 각각의 예시를 출력할 포맷
    prefix: str = "",                         # 예시들 앞에 붙는 서문
    suffix: str = "",                         # 마지막 user 입력 템플릿
    input_variables: List[str],               # suffix에서 사용할 변수
    example_separator: str = "\n\n"           # 예시들 사이 구분자
)
```
```
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# 예시들
examples = [
    {"word": "happy", "emoji": "😊"},
    {"word": "sad", "emoji": "😢"},
    {"word": "fire", "emoji": "🔥"},
]

# 각 예시 출력 포맷
example_prompt = PromptTemplate(
    input_variables=["word", "emoji"],
    template="Word: {word}\nEmoji: {emoji}"
)

# 전체 FewShotPromptTemplate 정의
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Translate the following words into emojis:\n",
    suffix="Word: {input}\nEmoji:",
    input_variables=["input"],
    example_separator="\n\n"
)

# 실제 프롬프트 생성
final_prompt = prompt.format(input="love")
print(final_prompt)
```
___


# SystemMessagePromptTemplate

## 정의
* Chat model에 전달되는 System Message를 template 형태로 정의할 수 있는 class

## 사용 목적
* Chat model에 System Message를 전달 함.

## 예시 코드
```
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# System 메시지 템플릿 정의
system_template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# Human 메시지 템플릿 정의
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 전체 ChatPromptTemplate 구성
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])

# 프롬프트 생성
final_messages = chat_prompt.format_messages(
    input_language="English",
    output_language="Korean",
    text="Nice to meet you"
)

# 결과 확인
for msg in final_messages:
    print(f"{msg.type}: {msg.content}")
```
```
system: You are a helpful assistant that translates English to Korean.
human: Nice to meet you
```
___

# HumanMessagePromptTemplate

## 정의
* chat model에 전달되는 Humun Message를 template 형태로 정의할 수 있는 class

## 사용 목적
* chat model에 Humun Message를 전달함.

## 예시 코드
```
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# 시스템 메시지 템플릿
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a helpful assistant that answers questions truthfully."
)

# 사용자 메시지 템플릿
human_prompt = HumanMessagePromptTemplate.from_template(
    "What is the capital of {country}?"
)

# 전체 ChatPromptTemplate 구성
chat_prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    human_prompt
])

# 포맷팅된 메시지 생성
messages = chat_prompt.format_messages(country="France")

# 메시지 출력
for msg in messages:
    print(f"{msg.type}: {msg.content}")
```
```
system: You are a helpful assistant that answers questions truthfully.
human: What is the capital of France?
```
___

# AIMessagePromptTemplate

## 정의
* Chat model에 전달되는 AI Message를 template 형태로 정의할 수 있는 class

## 사용 목적
* chat model에 AI Message를 전달함.

## 예시 코드
```
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate

# 시스템 메시지: AI 역할 설명
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a helpful assistant that answers factual questions."
)

# 사용자 메시지 예시
human_prompt = HumanMessagePromptTemplate.from_template(
    "What is the capital of Japan?"
)

# AI 응답 예시
ai_prompt = AIMessagePromptTemplate.from_template(
    "The capital of Japan is Tokyo."
)

# 새로운 사용자 질문 템플릿
followup_prompt = HumanMessagePromptTemplate.from_template(
    "What is the capital of Germany?"
)

# 전체 프롬프트 조합
chat_prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    human_prompt,
    ai_prompt,
    followup_prompt
])

# 메시지 구성
messages = chat_prompt.format_messages()

# 결과 출력
for msg in messages:
    print(f"{msg.type}: {msg.content}")
```
```
system: You are a helpful assistant that answers factual questions.
human: What is the capital of Japan?
ai: The capital of Japan is Tokyo.
human: What is the capital of Germany?
```
___

# 

## 정의

## 사용 목적


## 예시 코드

___

# 

## 정의

## 사용 목적


## 예시 코드

___

# 

## 정의

## 사용 목적


## 예시 코드

___

# 

## 정의

## 사용 목적


## 예시 코드

___

# 

## 정의

## 사용 목적


## 예시 코드

___

