# index.ts vs index.tsx
index.ts
- 해당 페이지의 진입점 (export만)
- ptyhon의 __init__.py

index.tsx
- 해당 페이지의 진입점 (react component)



# 폴더 규칙
- pages/
	- 여러 feature를 조합하는 곳(feature 배치)
	- url과 연결
	- layout 구성
- features/
	- 유저가 할 수 있는 행동
		- ex. 로그인 / 회원가입 / 댓글 작성 / 좋아요 클릭 / 결제 요청
		- ex. 비즈니스 로직 / 상태 관리 / api 호출 / 성공&실패 처리 / 해당 기능의 UI
- shared/
	- 어디에 속하는지 명확히 말하기 어려운 기능
- routes/
	- 라우팅 정의 & 규칙 & 네비게이션


# ETC

- features는 보통 `입력 > 처리 > 결과`로 완결된다.
- files?.IMAGES
	- ?는 옵셔널 체이닝
	- files가 null 이거나 undefined이면 에러를 내지 말고 그냥 undefined로 반환
	- 읽기 전용임.
		- `const files?.IAMGES = ...` 이런거 불가능

