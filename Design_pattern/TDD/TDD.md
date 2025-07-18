# TDD(Test-Drive Development)
- TDD(Test-Drive Development, 테스트 주도 개발)
- 테스트 코드를 먼저 작성하고, 그 테스트를 통과하는 최소한의 코드를 구현하는, 소프트웨어 개발 방법론

- 순서
	- Test code 작성
	- Test code를 통과하는 code 작성
	- Test code 통과시 해당 code 리팩토링


# TDD (기본 패턴, Red-Green-Refactor)
- Red(실패)
	- 아직 구현되지 않은 기능에 대한 테스트 코드 작성
- Green(성공)
	- 테스트를 통과하는 최소한의 실제 코드 작성
- Refactor(리팩토링)
	- 코드를 더 깔끔하게 다듬음
	- 기능은 그대로 두고, 코드 구조 개선
	- 테스트가 계속 Green일 경우 리팩토링 성공


# TDD의 장점
- 버그를 초기에 발견하고 수정 가능
- 문서 역할: 테스트가 곧 사용 예시
- 리팩토링이 용이해짐
- 필요한 기능만 개발하게 됨(오버 엔지니어링 방지)


# TDD를 실무에서 쓰는 패턴
- Unit Test: 함수, 메서드 등 작은 단위에 적용
- CI/CD pipeline 연계: 모든 커밋마다 자동으로 테스트
- [[Mocking]] 활용: 외부 API, DB 등 의존성 분리


# TDD 오해 및 현실
- TDD는 Test code를 먼저 작성하는 개발 방식이지만
  무조건 모든 테스트를 "완벽하게" 먼저 작성하는 건 아님
  -> 작은 단위로 반복하는 것이 핵심
- Test coverage가 높다고 무조건 좋은 품질은 아니며
  중요한 것은 Test quality
  (적절치 못한 테스트 및 불필요한 테스트 피하기)


# TDD 실무 적용시 현실
- 초기 개발 속도가 느려보임
	- 단, 시간이 지날수록 버그 수정 & 리팩토링에 강함
- 외부 시스템 의존성이 많으면 TDD가 적절치 않아 보임
	- Mocking, Stub, Fake 객체를 잘 활용할 것
- 레거시 코드(기존 코드)에는 TDD 적용이 어려움
	- **코드 리팩토링 -> 테스트 작성** 순으로 접근함


# TDD 관련 실전 기술/개념
### 테스트 분류
- Unit Test
	- 함수/메서드 수준
- Integration Test
	- 여러 모듈이 함께 동작하는지
- Acceptance Test
	- 전체 흐름이 사용자의 요구대로 동작 하는지

### Test Double
- [[Mock]]
	- 호출 내역/동작까지 검증
- [[Stub]]
	- 고정된 값을 반환
- [[Fake]]
	- 간단하게 동작하는 진짜 구현체

### 코드 설계와 TDD
- TDD를 하다 보면 "테스트하기 쉬운 설계(=의존성 분리, 작은 단위 함수, SOLID 원칙)"가 자연스럽게 익혀짐.



# 정리
- TDD는 "테스트 먼저, 구현 나중, 반복적 개선"하는 개발 패턴
- **Red-Green-Refactor** 루프가 핵심
- 더 나은 품질과 안정성을 가져옴