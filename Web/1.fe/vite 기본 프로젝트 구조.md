![[Pasted image 20251011044642.png]]

- `public/`: 정적 파일을 저장하는 폴더
	- `robots.txt`: 검색 엔진 크롤러를 위한 규칙 파일

- `node_modules/`
	- npm을 통해 설치된 모든 패키지와 라이브러리가 저장되는 폴더
	- 직접 수정하지 않으며, `package.json` 기반으로 자동 생성됨

- `src/`: 소스 코드 메인 폴더

- `package.json`: 프로젝트 의존성 관리 및 스크립트 정의
- `package-lock.json`: 정확한 의존성 버전
- `index.html`: 앱의 진입점 html 파일
- `README.md`: 프로젝트 설명 문서
- `vite.config.js`: Vite 빌드 도구 설정 파일
- `eslint.config.js`: 코드 품질 검사를 위한 ESLint 설정


# self-QA
## 1. package.json & package-ock.json

### package.json
의존성 정보와 기본 설정을 정의하는 파일
개발자가 직접 작성하며 프로젝트의 "명세서"  와 같은 역할을 함.

### package-lock.json
npm이 자동으로 생성하는 파일. 설치된 라이브러리의 정확한 version을 lock하기 위한 역할
`npm isntall`을 실행했을 때 완전히 동일한 환경이 복제되도록 보장하는 역할을 한다.

- 특징
	- 모든 의존성의 정확한 version을 기록(하위 의존성까지 전부)
	- 각 패키지 다운로드 경로(url), 무결성 해시값까지 포함
	- 자동 생성/갱신되어 사용자가 수정할 필요 없음
  

## 2. ESLint란?

JavaScript / TypeScript 코드의 문법, 스타일, 오류를 자동으로 검사하는 도구
> “코드가 돌아가긴 하지만, 이렇게 쓰면 버그가 날 수도 있어요.”  
> “이건 팀의 스타일 가이드에 안 맞아요.”  
> “이 변수는 선언했는데 안 썼어요.”  
> 이런 걸 자동으로 잡아주는 **코드 감시자**라고 생각하면 됩니다.

- 특징
	- 문법 오류 잡기
	- 사용하지 않는 변수 감지
	- 일관된 코드 스타일 유지 (팀 스타일 가이드)
	- 그 외에도 React 플러그인을 추가하면 React 전용 검사도 가능
