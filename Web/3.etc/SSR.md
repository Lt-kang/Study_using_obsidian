# SSR(Server-Side Rendering)
- 서버가 HTML을 와성한 상태로 보내고, 브라우저는 그걸 바로 보여줌.
- 이후 js가 로드되어 상호작용 기능을 붙임.


# 동작 과정
1. client가 server에 페이지 요청
2. server가 data를 가져와 HTML 생성
3. 완성된 HTML을 browser로 전달 -> 즉시 rander
4. js load 후 react 앱 활성화(Hydration)


# 특징
- 장점: 초기 로딩 빠름, SEO 친화적
- 단점: 서버 부하. 요청마다 렌더링 시간 발생


# 사용처
- 블로그 / 커머스 / 뉴스 등 검색 유입이 중요한 서비스
- 로그인을 안 한 사용자 비중이 높고, 초기 켄턴츠 노출이 핵심인 경우


