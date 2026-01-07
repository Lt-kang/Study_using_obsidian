# GraphQL이란?
- Facebook이 개발한 API를 위한 query language
- 클라이언트가 원하는 데이터만 정확히 요청할 수 있는 api 방식

# 핵심 개념 3가지
|개념|설명|
|---|---|
|**Query**|데이터를 “조회(Read)”하는 요청. REST의 `GET`과 유사|
|**Mutation**|데이터를 “변경(Create, Update, Delete)”하는 요청|
|**Subscription**|서버에서 데이터가 변경될 때, 실시간으로 푸시 받는 기능 (웹소켓 기반)|

# REST API와의 차이점
|구분|REST API|GraphQL|
|---|---|---|
|**데이터 요청 단위**|여러 엔드포인트(`GET /users`, `GET /posts`)|단 하나의 엔드포인트(`/graphql`)|
|**요청 방식**|HTTP 메서드 (GET, POST, PUT, DELETE 등)|단일 HTTP POST 요청 안에 **Query** 작성|
|**데이터 형태**|고정된 응답 구조|원하는 필드만 선택 가능|
|**Over-fetching 문제**|필요 이상으로 많은 데이터를 받음|필요한 필드만 선택 가능|
|**Under-fetching 문제**|여러 번 요청해야 필요한 데이터를 모두 얻음|한 번의 쿼리로 여러 리소스를 동시에 요청 가능|
