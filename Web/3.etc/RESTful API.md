# RESTful API란?
- 설계원칙(architecture style) 중 하나
- REST(Representational State Transfer) 원리를 따르는 API

# REST란?
- 웹의 자원을 일관된 규칙으로 다루는 방법
- URL을 통해 **무엇을** 다루고, HTTP 메서드를 통해 **어떻게**다룰지 표현함

| 개념                     | 설명                                              | 예시                              |
| ---------------------- | ----------------------------------------------- | ------------------------------- |
| **리소스(Resource)**      | 접근하려는 데이터의 대상                                   | `/users`, `/posts`, `/products` |
| **표현(Representation)** | 그 리소스를 어떤 형식으로 주고받는가                            | JSON, XML 등                     |
| **상태(State)**          | 클라이언트가 요청 시마다 필요한 상태를 포함해서 전송 (서버는 상태를 저장하지 않음) | “Stateless” 구조                  |

# RESTful API의 장점
- 표준화된 HTTP 방식으로 이해하기 쉬움
- 서버와 클라이언트의 역할이 명확하게 분릳됨.
- 확장성과 유연성에 좋음
- json을 이용해 가볍게 통신이 가능함

# RESTful API의 핵심 원칙
|원칙|설명|
|---|---|
|**1️⃣ 클라이언트-서버 구조 (Client-Server)**|클라이언트는 UI, 서버는 데이터와 로직을 담당 (역할 분리)|
|**2️⃣ 무상태성 (Stateless)**|각 요청은 독립적이며, 서버는 클라이언트의 상태를 저장하지 않음|
|**3️⃣ 캐시 가능성 (Cacheable)**|응답은 캐시 가능해야 하며, HTTP 헤더 등을 통해 이를 명시할 수 있어야 함|
|**4️⃣ 계층화 시스템 (Layered System)**|중간에 로드밸런서, 프록시 등 여러 계층이 존재할 수 있음|
|**5️⃣ 일관된 인터페이스 (Uniform Interface)**|URI와 HTTP 메서드를 일관성 있게 사용해야 함|


# RESTful API의 설계 규칙 예시
|작업|HTTP 메서드|예시 URI|설명|
|---|---|---|---|
|조회(Read)|**GET**|`/users`|모든 사용자 조회|
|조회(Read)|**GET**|`/users/1`|ID=1인 사용자 조회|
|생성(Create)|**POST**|`/users`|새로운 사용자 생성|
|수정(Update)|**PUT**|`/users/1`|ID=1인 사용자 전체 수정|
|일부 수정(Patch)|**PATCH**|`/users/1`|ID=1인 사용자 일부 수정|
|삭제(Delete)|**DELETE**|`/users/1`|ID=1인 사용자 삭제|

# RESTful 하지 않은 경우
|비RESTful|RESTful|
|---|---|
|`/getUserInfo?id=1`|`/users/1`|
|`/createUser`|`/users` (POST)|
|`/updateUser/1`|`/users/1` (PUT/PATCH)|
