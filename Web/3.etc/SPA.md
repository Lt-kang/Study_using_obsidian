# SPA(Single Page Application)
- 페이지가 한번만 로드되는 웹 애플리케이션
- 즉, 사용자가 다른 화면으로 이동할 때마다 새 HTML을 요청하지 않고, 로드된 페이지 내에서 JS가 동적으로 html을 교체하는 방식
- 대표적인 프레임워크
	- React + React Router
	- Vue + Vue Router
	- Angular


# 동작방식
1. client가 server에 page 요청
2. server는 client에게 `index.html`과 js 번들을 보냄
3. client browser는 js(React, Vue, Angular 등)를 실행해서 화면을 렌더링
4. 이후 페이지 이동시
	1. js가 url만 변경하고 필요한 데이터만 받아서 dom 일부만 갱신
	   (server에 새로운 html 요청X)


## 동작방식(예시 / React)
```
사용자 접속
↓
서버 → index.html + bundle.js 전달
↓
React Router가 라우팅 제어
↓
페이지 이동 시 API(fetch)로 데이터만 교체
↓
DOM 일부만 갱신 → 부드러운 전환

```

# SPA의 장/단점
## 장점
- 빠른 전환 속도와 부드러운 UI/UX
- fe 중심 개발구조
- client 상태 관리 용이
	- Redux / Zustand / Recoil 등으로 상태 공유
- 컴포넌트 단위 개발로 생산성 향상
- React Native 등과 코드 일부 공유 가능

## 단점
- SEO(검색엔진)이 약함
	- 이는 초기 html이 비어있으며 js가 실행되어야 컨텐츠가 출력됨.
	  그렇기에 검색엔진 봇이 데이터를 수집해갈 정보가 부족함.
- 초기 로딩 느림
	- js 번들이 커서 로딩 속도 느림.
- 보안 취약점 주의 필요 - [[SPA-보안취약이유]]
	- client에서 routing과 rendering이 이루어짐.
- 브라우저 히스토리 관리 복잡
	- URL 변경 시 별도 처리 필요(React Router 등)
- 초기 데이터 패칭 로직 필요
	- 첫 렌더링 시 데이터 불러오기 지연 가능


# SPA 추천 시점

## 적합한 상황
- 내부 관리자 도구 / 대시보드 / CRM/ERP 등
- 로그인 후 사용하는 웹 앱형 서비스(SEO 중요도 낮을 경우)
- 실시간 UI 업데이트, 그래프, 테이블 중심 interaction

## 부적합한 상황
- SEO 중요도가 높은 공개 컨텐츠형 사이트(블로그 / 커머스 / 뉴스)
- SNS 공유시 미리보기(OG 태그)가 필요한 경우
	- 이런 경우 SSR/SSG 기반인 NextJS와 같은 프레임워크가 더 적합함.


# SPA 서비스 예시
|서비스|특징|
|---|---|
|**Notion / Slack / Figma 웹**|완전한 SPA, 새로고침 없이 페이지 전환|
|**Google Drive / Gmail**|JS로 모든 화면 제어|
|**React 기반 사내 관리자 페이지**|서버와 JSON API 통신만 함|


# 요약
- 한 번만 로드되는 페이지 내에서 JS가 모든 걸 처리하는 앱형 웹사이트
- UX는 빠르지만 SEO에는 약하고 SSR보다 초기 로딩이 무거움
