
# ORM에 대해서
- ORM(Object Relational Mapping)이란?
	- 객체 지향 프로그래밍 언어(Python)와 관계형 데이터 베이스(SQL) 간의 데이터를 변환해주는 도구(기술)
		- python > class와 object로 데이터를 다룸
		- DB > Table과 record로 데이터를 다룸
		- 이 둘을 자동으로 연결/변환 하는 기술이 ORM
		
- ORM을 사용하는 이유
	- SQL 직접 작성 없이 Python 코드로 DB 조작 가능
	- SQL injection 방지
	- 생산성 증가
	- 유지보수성 용이

- FastAPI에서의 ORM
	- FastAPI 자체 기능은 없으며 SQLAlchemy 등의 외부 라이브러리를 통해 ORM을 사용함.
	


# Primary Key / Foreign Key
## Primary Key
- 정의
	- DB Table에서 각 row을 유일하게 식별할 수 있는 칼럼
- 특징
	- 값이 중복될 수 없음. (유일성)
	- NULL 값을 가질 수 없음
	- 하나의 Table에 반드시 하나만 존재해야 함
- 용도
	- 데이터의 식별자(ID) 역할
	- 다른 테이블과의 관계 설정 시 기준이 됨

## Foreign Key
- 정의
	- 다른 테이블의 primary key를 참조하는 칼럼
- 특징
	- 두 테이블 간의 **관계**를 표현할 때 사용
	- 부모 테이블의 primary key 값만 저장 가능
- 용도
	- 데이터의 연결 및 무결성 유지
- 기타 특징
	- 1:N / N:1 / N:M 등 다양한 관계로 설정할 수 있음


# 역참조(backref)란?
- 두 테이블(모델)이 관계를 맺을 때, 한쪽에서 반대 방향 객체를 쉽게 접근할 수 있도록 해주는 기능
	- 참조키는 일방향
	- 역참조는 양방향
- FastAPI에서는 relationship 메서드에서 backref 인자값을 사용함
- 1:N / N:M 관계에서도 사용 가능


# FastAPI에서 alembic을 사용하는 이유는?
- alembic이란?
	- DB migration tool
	- SQLAlchemy ORM과 함께 쓰임
	- 데이터베이스 schema(테이블 구조/칼럼)의 변경 사항에 대해 버전관리 및 관련 변경 사항을 쉽게 반영할 수 있게 도와주는 툴
	
- DB migration 사용하는 이유
	- DB Table은 처음 만든 그대로 유지되지 않음. 이후로도 계속해서 column을 추가하고 제거함
	- 서비스가 커질수록 DB 구조는 계속 바뀜.
	- 이에 따라 DB Table에 대한 version control이 필요

- alembic을 사용하는 이유
	- DB Table 변경 이력을 코드로 남김
	- - `alembic revision --autogenerate -m "Add email column to users"`  
    같은 명령어로 변경 사항 파일 생성
    - `alembic upgrade head`로 실제 DB에 반영

- 기타사항
	- FastAPI > 백엔드 웹 프레임워크
	- SQLAchemy > ORM 모델 작성
	- Alembic > DB Table version Control Tool


# 리비전(Revision) 이란?
- Alembic이 관리하는 DB Schema 변경 내역을 기록하는 Version file
- DB 구조에 어떤 변화가 일어났는지, 기록하는 스냅샷


# @contextlib.contextmanager
- `@contextlib.contextmanager`은 Python에서 with문(Context manager)을 간편하게 만들 수 있게 해주는 데코레이터
- 즉, with문을 깔끔하게 만들어주는 데코레이터


# Typing vs pydantic
## `typing` 이란?
- 파이썬 표준 라이브러리
- Type Hint Tool
- 변수/함수/클래스 등에서 명시적으로 힌트를 줄 수 있음
- **런타임에서는 아무런 제약/검증을 하지 않음**

## `pydantic`이란?
- 외부 라이브러리(**FastAPI에서는 거의 필수**)
- 데이터 검증 / 파싱 / 직렬화 / 역직렬화를 위해 사용
- 런타임에서 실제로 type validation 및 형 변환까지 수행
- 주로 API 개발에서, 외부에서 들어오는 데이터가 정확히 원하는 타입/형식인지 검사할 때 사용


# 직렬화(Serialization)
- 데이터(객체/클래스)를 **저장**하거나 전송할 수 있는 형식(문자열, 바이트 등)으로 **변환**하는 것
- json / xml / binary 등 네트워크 전송, 파일 저장에 적합한 형식으로 바꿈
- 실무 예시
	- Python object를 json으로 바꿔서 http 응답으로 내보냄
	- db에 저장하거나 파일로 기록

# 역직렬화(Deserialization)
- **직렬화된 데이터를 다시 원래의 객체나 데이터 구조로 복원하는 것**
- 즉, 저장하거나 네트워크로 받은 데이터를 코드에서 사용할 수 있게 되돌리는 과정
- 실무 예시
	- api 요청에서 받은 json data를 python object로 변환
	- 저장된 파일을 읽어 코드에 활용
****

___
model (DB model / pydantic model)
route  
의존성 주입 
schema  (pydantic)
crud  

예외 처리 및 에러 핸들링
인증/인가 (JWT/OAuth2)
설정 관리 (config / .env / pydantic.BaseSettings)
미들웨어
Test


```
app/
├── main.py           # FastAPI 엔트리포인트
├── models/           # ORM 모델
├── schemas/          # Pydantic 모델
├── crud/             # CRUD 함수/비즈니스 로직
├── routes/           # 라우터(API endpoint)
├── core/             # 설정, 의존성, 미들웨어 등
├── services/         # (선택) 서비스 계층
├── exceptions/       # 예외처리
└── tests/            # 테스트 코드
```
___

## 4. 요약

### 꼭 필요한 구성(핵심)
- **DB Model**
- **Pydantic Model (schema)**
- **Route**
- **의존성 주입
- **CRUD**
    
### 실무에서 더 필요한 축 (추천)
- 서비스/비즈니스 계층
- 예외처리
- 인증/인가
- 설정 관리
- 미들웨어
- 테스트
- 문서 자동화
- 운영 자동화

___

```
FastAPI의 `Depends`는 매개변수로 전달받은 함수를 호출하여 그 결과를 리턴한다.
```

```
Pydantic은 API의 입출력 항목을 다음과 같이 정의하고 검증할수 있다.

- 입출력 항목의 갯수와 타입을 설정
- 입출력 항목의 필수값 체크
- 입출력 항목의 데이터 검증
```
