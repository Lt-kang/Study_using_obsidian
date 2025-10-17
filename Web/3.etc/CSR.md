# CSR(Client-Side Rendering)
- Client browser에서 JavaScript로 HTML을 렌더링 하는 방식
- server는 client에게 html 틀과 js 번들만 보내고 js 실행 후 화면을 완성함.
- 특징
	- 장점: SPA처럼 부드러운 전환, UX 좋음
	- 단점: 첫 로딩이 느리며 검색엔진(SEO)에 불리함
	  -> CSR은 검색엔진이 JS를 실행하지 않으면 내용 인식 어려움

# 동작 과정
1. Client가 server에 page 요청
2. server는 client에 `index.html`과 JS 번들 전송
3. client browser에서 js 실행 후 html 생성(렌더링)


# 사용처
- 로그인 후 내부 시스템 / 대시보드 / SaaS 관리자 페이지 등
- SEO가 필요 없는 앱형 서비스





