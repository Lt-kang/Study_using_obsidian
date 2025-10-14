# AI Message는 사람이 제어하지 않을까?

* 일반적으로 AI Message는 AI 응답만을 기록하지만 사용자가 제어가 가능함.
* 제어 목적으로는 아래와 같음.
    * LLM에게 답변 예시를 제공하기 위한 few-shot
    * test/debug

___

# `Memory`와 `History` 둘의 관계는?

* Memory가 더 상위 개념. Memory class 내부적으로 History class를 사용함.
* Memory: 대화의 전체 컨텍스트 상태를 관리하는 상위 개념
    * `ConversationBufferMemory`, `ConversationSummaryMemory`
    * 입/출력 추적, context 주입, 자동 저장
    * chain / agnet 실행 시 자동으로 context 주입
* History: 실제 대화 message들의 list를 저장하고 불러오는 객체
    * `ChatMessageHistory`, `RedisChatMessageHistory`, `BaseChatMessageHistory`
    * message add / query / delete
    * message load / save


___

# Memory에서 `buffer` / `summary` / `window` 의 의미
* buffer: 모든 메시지를 순서대로 계속 저장
* summary: 중요한 내용만 요약해서 저장
* Window: 가장 최근 대화 몇 개만 유지


