SystemMessage
HumanMessage
AIMessage

___


# SystemMessage

## 정의
* ai의 행동을 정의하는 system message 객체를 생성.

## 사용 목적
* 보통 대화의 가장 첫부분에 위치함.
* ai의 행동을 정의할 때


## 예시 코드
```
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(
        content="You are a helpful assistant! Your name is Bob."
    ),
    HumanMessage(
        content="What is your name?"
    )
]

# Define a chat model and invoke it with the messages
print(model.invoke(messages))
```
___

# HumanMessage

## 정의
* 사용자 입력 message 객체

## 사용 목적
* chain에 입력될 사용자 입력 message 객체임.
* 주로 memory 혹은 history 객체와 함께 사용됨.

## 예시 코드
```
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(
        content="You are a helpful assistant! Your name is Bob."
    ),
    HumanMessage(
        content="What is your name?"
    )
]

# Instantiate a chat model and invoke it with the messages
model = ...
print(model.invoke(messages))
```

___

# AIMessage

## 정의
* chat model이 사용자 입력으로부터 반환한 답변
* 답변 뿐만이 아닌 tool calls, usage metadata와 같은 Langchain fields도 함께 반환함.

## 사용 목적
* memory 혹은 history 객체와 함께 사용됨.
* model output 외에도 사용자가 직접 custom할 수 있음. ex) few-shot learning

## 예시 코드
```
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# LLM 모델 설정
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)

# Few-shot 예시 구성
messages = [
    SystemMessage(content="너는 친절한 수학 선생님이야."),
    
    # Few-shot 예시 1
    HumanMessage(content="2 더하기 2는 뭐야?"),
    AIMessage(content="2 더하기 2는 4야."),

    # Few-shot 예시 2
    HumanMessage(content="10에서 3을 빼면 뭐야?"),
    AIMessage(content="10에서 3을 빼면 7이야."),

    # 이제 진짜 질문
    HumanMessage(content="15 곱하기 3은 뭐야?")
]

# 응답 생성
response = chat(messages)
print(response.content)
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


# 

## 정의

## 사용 목적


## 예시 코드

