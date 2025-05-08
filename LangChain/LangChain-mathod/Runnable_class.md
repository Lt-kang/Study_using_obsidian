# RunnablePassthrough

## 정의
* no-op(무연산) 체인
* 입력 데이터를 그대로 출력 (그 어떤 가공X)
* chain 사이의 placeholder 역할

## 사용 목적
* 구현되지 않은 부분 임시 연결
* 특정 Runnable 동작을 끊고 싶을 때
* LLM 앞 뒤에 붙은 chain 구성 요소를 테스트할 때

## 예시 코드
```
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# 1. Prompt 정의
prompt = ChatPromptTemplate.from_template("Translate the following English text to French: {text}")

# 2. LangChain LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. RunnablePassthrough 정의
noop = RunnablePassthrough()

# 4. 체인 구성: Prompt → Passthrough → LLM
chain = prompt | noop | llm

# 5. 실행
result = chain.invoke({"text": "Hello, how are you?"})
print(result.content)
```
___

# RunnableParallel

## 정의
* 입력값을 동시에 여러 Runnable로 전달하여 각각의 결과를 병렬로 얻는 class
* 1개의 입력값 -> 다수의 chain -> 다수의 output

## 사용 목적
* 하나의 입력으로 여러 방향으로 처리하여 여러 시각의 결과를 얻고자할 때
    * ex) 입력 -> 감정 분석 + 요약 + 번역 

## 예시 코드
```
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel

# 1. 모델 정의
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 2. 프롬프트 정의
summary_prompt = ChatPromptTemplate.from_template("Summarize this text: {text}")
translate_prompt = ChatPromptTemplate.from_template("Translate this to Korean: {text}")

# 3. 각각의 체인 구성
summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm

# 4. 병렬 실행을 위한 RunnableParallel 구성
parallel_chain = RunnableParallel({
    "summary": summary_chain,
    "translation": translate_chain
})

# 5. 실행
input_text = {"text": "LangChain is a framework for building applications with LLMs via composable components."}
result = parallel_chain.invoke(input_text)

print("✅ Summary:", result["summary"].content)
print("✅ Translation:", result["translation"].content)
```
___

# RunnableMap

## 정의
* 입력값 dict의 각 key에 대해 다른 Runnable을 mapping해서 실행하는 class
* 입력값 dict의 key에 따라 각기 다른 chain이 실행 됨.

## 사용 목적
* input dict key마다 서로 다른 로직(chain)을 적용하고 싶을 때
* input이 다중 필드(dict)일 때

## 예시 코드
```
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableMap

# 모델
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 프롬프트
summary_prompt = ChatPromptTemplate.from_template("Summarize this: {input}")
translate_prompt = ChatPromptTemplate.from_template("Translate to Korean: {input}")

# 체인
summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm

# RunnableMap 구성: key별로 input이 다르게 매핑됨
map_chain = RunnableMap({
    "summary": summary_chain.with_config(tags=["summary"]),
    "translation": translate_chain.with_config(tags=["translate"]),
})

# 실행
input_dict = {
    "summary": {"input": "LangChain simplifies working with LLMs by composing chains."},
    "translation": {"input": "LangChain is a useful framework for LLMs."}
}

result = map_chain.invoke(input_dict)

print("📝 Summary:", result["summary"].content)
print("🇰🇷 Translation:", result["translation"].content)
```

___

# RunnableLambda

## 정의
* 간단한 Python 함수를 LangChain의 Runnable chain에 포함할 수 있도록 해주는 class
* python의 lambda의 Langchain Runnbale version

## 사용 목적
* Runnable 객체로 lambda를 사용할 때

## 예시 코드
```
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 1. 사용자 정의 전처리 함수 (문자열을 대문자로)
uppercase = RunnableLambda(lambda x: {"text": x["text"].upper()})

# 2. 프롬프트 + LLM
prompt = ChatPromptTemplate.from_template("Repeat this: {text}")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. 체인 구성: 대문자 변환 → 프롬프트 → LLM
chain = uppercase | prompt | llm

# 4. 실행
result = chain.invoke({"text": "hello, langchain lambda"})
print(result.content)
```
___

# RunnableBranch

## 정의
* 입력값에 따라 조건에 맞는 runnable chain 실행
* if/elif/else의 LangChain Runnable version


## 사용 목적
* d입력값에 따라 서로 다른 chain을 실행해야할 때

## 예시 코드
```
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 각각에 사용할 프롬프트 체인
prompt_greeting = ChatPromptTemplate.from_template("Say hello to the user.")
prompt_qa = ChatPromptTemplate.from_template("Answer this question: {question}")

# 체인 연결
greeting_chain = prompt_greeting | llm
question_chain = prompt_qa | llm
default_chain = RunnableLambda(lambda x: "Unknown input")

# 분기 체인 정의
branch = RunnableBranch(
    (lambda x: x.get("type") == "greeting", greeting_chain),
    (lambda x: x.get("type") == "question", question_chain),
    default_chain
)

# 실행
print(branch.invoke({"type": "greeting"}).content)
print(branch.invoke({"type": "question", "question": "What is LangChain?"}).content)
```
___

# RunnableSequence

## 정의
* 여러개의 Runnable 객체를 chaining하는 class (pipeline 구축)
* `|` 연산자와 같은 역할. 단, 이는 명시적으로 여러 객체를 chaining할 수 있음.

## 사용 목적
* chaining을 코드 상에서 리스트로 명확히 구성하고 싶을 때
* 동적으로 여러 단계를 조합하고 싶을 때

## 예시 코드
```
from langchain_core.runnables import RunnableSequence

sequence = RunnableSequence([
    chain1,
    chain2,
    chain3
])

result = sequence.invoke(input)
```
___

# RunnableAssign

## 정의
* dict을 입력 받아 여러 Runnable을 실행해서 그 결과를 dict 내 새로운 key-value로 추가하는 chain
* 입력을 가공하지 않고 그대로 두되, 추가 정보를 붙이는 용도

## 사용 목적
* 입력 데이터는 그대로 유지하면서, LLM 결과/분석 등을 필드에 추가로 넣고 싶을 때
* 여러 파생 정보를 동시에 추가하고 싶을 때
* 중간 처리 데이터를 기록해서 후속 체인에서 다시 사용하고 싶을 때

## 예시 코드
```
from langchain_core.runnables import RunnableLambda, RunnableAssign

# 1. Runnable 정의
summarizer = RunnableLambda(lambda x: "요약: " + x["text"][:10] + "...")
length_calc = RunnableLambda(lambda x: len(x["text"]))

# 2. Assign 체인 구성
assign = RunnableAssign({
    "summary": summarizer,
    "length": length_calc
})

# 3. 실행
result = assign.invoke({"text": "LangChain은 LLM을 연결하는 프레임워크입니다."})
print(result)
```
```
{
  'text': 'LangChain은 LLM을 연결하는 프레임워크입니다.',
  'summary': '요약: LangChain...',
  'length': 29
}
```
___