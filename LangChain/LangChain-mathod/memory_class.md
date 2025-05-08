ConversationBufferMemory
ConversationSummaryMemory
VectorStoreRetrieverMemory
___


# ConversationBufferMemory

## 정의
* 대화 전체를 순차적으로 buffer에 저장해서 LLM에게 context를 유지시켜주는 역할
* 내부적으로 `ChatMessageHistory` 객체를 사용하여 Human / AI Message를 순서대로 저장.

## 사용 목적
* 사용자와 LLM 간의 대화 흐름을 기억해서 문맥 유지하는 데 사용.
* agent / chain에서 이전 대화 내용을 참조할 수 있게 도와줌.
* 가장 일반적인 Memory class

## 예시 코드
```
> Entering new ConversationChain chain...
Prompt after memory:
The following is a friendly conversation between a human and an AI. 
The AI is talkative and provides lots of specific details from its context.

Human: Hi, I'm Kang!
AI: Hello Kang! Nice to meet you.

Human: What do you remember about me?
AI: You just told me your name is Kang!
```
```
> Entering new ConversationChain chain...
Prompt after memory:
The following is a friendly conversation between a human and an AI. 
The AI is talkative and provides lots of specific details from its context.

Human: Hi, I'm Kang!
AI: Hello Kang! Nice to meet you.

Human: What do you remember about me?
AI: You just told me your name is Kang!
```
___


# ConversationSummaryMemory

## 정의
* `ConversationBufferMemory`의 summary version
* LLM을 사용해 대화 내용을 요약하고 이후 대화에 context로 제공함.
* 요약만 저장하므로 메모리 효율이 좋으며, 긴 대화에서도 토큰 초과를 방지할 수 있음.

## 사용 목적
* 토큰을 최적화 + 긴 대화 지원 + 문맥 유지

## 예시 코드
```
from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# 요약용 LLM (요약 생성에 사용됨)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Summary Memory 생성
summary_memory = ConversationSummaryMemory(
    llm=llm,
    return_messages=True
)

# 체인에 메모리 연결
conversation = ConversationChain(
    llm=llm,
    memory=summary_memory,
    verbose=True
)

# 대화 예시
conversation.predict(input="Hi, I'm Kang. I live in Seoul and love hiking.")
conversation.predict(input="What did I just tell you about myself?")
```
___

# VectorStoreRetrieverMemory

## 정의
* 대화 내용 / 문서 등을 vectorize하여 vector db에 저장하고 이후 관련 문맥을 retrieval해서 LLM에 전달하는 memory
* embedding 기반 문맥을 저장 / 유사도 기반으로 불러옴

## 사용 목적
* 문맥 검색 + 장기 기억 구현 + 토큰 최적화 + vector db 사용
* 기억을 summary/buffering 하지 않고, embedding 기반 중요한 정보만 추출하고 싶을 때
* 사용자에 대한 정보(이름 / 관심사 / 과거 질문 등)를 장기 기억처럼 유지하고 싶을 때
* RAG 챗봇의 대화 맥락을 기억할 때

## 예시 코드
```
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# 벡터 저장소 생성
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_texts([], embedding)

# Retriever 생성
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# VectorStore 기반 Memory 생성
memory = VectorStoreRetrieverMemory(retriever=retriever,
                                    store_memory=True)

# 대화용 체인 생성
llm = ChatOpenAI(temperature=0)
conversation = ConversationChain(llm=llm, memory=memory)

# 대화 입력
conversation.predict(input="My name is Kang and I love Python.")
conversation.predict(input="What is my name?")
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

