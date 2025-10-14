RunnableWithMessageHistory
BaseChatMessageHistory

___

# BaseChatMessageHistory

## 정의
* message history를 save / load / delete 기능을 공통으로 정의한 abstract base class
* `ChatMessageHistory` 구현체는 이 `BaseChatMessageHistory`를 상속 받아야함

## 사용 목적
* 다양한 저장소(memory, redis, mongodb, sqlite 등)에 message를 저장하고 불러오기 위한 공통 interface
* LangChain의 memory에서 message storage로 확장성 있는 구조 설계 가능
* `RunnableWithMessageHistory`, `ConversationBufferMemory` 등이 내부적으로 이 클래스를 사용함

## 예시 코드
```
class FileChatMessageHistory(BaseChatMessageHistory):
    storage_path:  str
    session_id: str

   @property
   def messages(self):
       with open(os.path.join(storage_path, session_id), 'r:utf-8') as f:
           messages = json.loads(f.read())
        return messages_from_dict(messages)

   def add_messages(self, messages: Sequence[BaseMessage]) -> None:
       all_messages = list(self.messages) # Existing messages
       all_messages.extend(messages) # Add new messages

       serialized = [message_to_dict(message) for message in all_messages]
       # Can be further optimized by only writing new messages
       # using append mode.
       with open(os.path.join(storage_path, session_id), 'w') as f:
           json.dump(f, messages)

   def clear(self):
       with open(os.path.join(storage_path, session_id), 'w') as f:
           f.write("[]")
```
___

# RunnableWithMessageHistory

## 정의
* Runnable 객체에 Message 기반 대화 이력(memory)를 연동시켜주는 wrapper class
* 내부적으로 `chat_history`, 이전 message를 자동으로 주입해서 문맥 유지형 agent/chain 실행이 가능.

## 사용 목적
* Agent / Chain을 실행할 때 과거 대화 기록을 자동으로 삽입해서 문맥 유지
* `ChatMessageHistory` 기반의 memory를 연결할 수 있음
* `Runnable` 객체라면 어떤 chain에도 적용 가능
* LangServe 등 endpoint 단위로 memory를 분리하고 싶을 때 사용.

## 예시 코드
```
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory

# 기본 체인 구성
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])
llm = ChatOpenAI()
chain = prompt | llm | StrOutputParser()

# 세션별로 메모리 관리 함수 정의
def get_message_history(session_id: str) -> ChatMessageHistory:
    if session_id not in memory_store:
        memory_store[session_id] = ChatMessageHistory()
    return memory_store[session_id]

memory_store = {}  # 세션별 히스토리 저장용

# 체인에 메모리 기능 부여
runnable_with_memory = RunnableWithMessageHistory(
    runnable=chain,
    get_message_history=get_message_history,
    input_messages_key="input",   # input 필드가 user 메시지
    history_messages_key="chat_history",  # 내부적으로 message history key로 사용됨
)

# 체인 실행 (세션 ID를 붙이면 같은 문맥 유지)
response = runnable_with_memory.invoke(
    input={"input": "What is your name?"},
    config={"configurable": {"session_id": "kang-session"}}
)

print(response)
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
