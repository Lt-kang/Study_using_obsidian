# Dependency(의존성)이란?
* 어떤 코드(함수, 클래스 등)가 다른 코드(외부 자원, 데이터, 설정 등)를 필요로 하는 상황
* 특정 기능을 수행하기 위해 필요한 외부 요소를 의미
	* ex)
	* 데이터 베이스 연결
	* 설정 파일
	* Request 객체
	* 인증/권한 확인
	* 로깅

```
def fetch_data_from_db(db_connection):
    # db_connection은 함수가 의존하는 외부 요소
    return db_connection.query("SELECT * FROM table")
```
* fetch_data_from_db 함수는 db_connection이라는 의존성에 의존하며, 이 연결 객체 없이는 동작하지 못함.
* `fetch_data_from_db` -> `db_connection` 의존 관계



# Dependency Injection(의존성 주입) 이란?
* 코드에서 필요한 의존성을 외부에서 주입하여 관리하는 디자인 패턴
* 주입된 의존성을 통해
	* 코드 재사용성 증가
	* 테스트 용이
	* 의존성 관계를 명확히 정의 가능
* FastAPI에서는 이 의존성 주입을 함수나 경로에 자동으로 주입해주는 방식으로 관리.



# FastAPI에서 의존성 주입 장점
* 코드 재사용성 증가
* 코드 분리
* 유지보수 용이성
* 자동 처리
	* FastAPI가 의존성을 자동으로 주입하고 관리해줌
* 테스트 용이성
	* 의존성을 주입받는 구조에서는 Mock 객체를 사용해 테스트를 쉽게 작성할 수 있음.



# FastAPI에서의 의존성 주입 예시 코드

## 기본적인 의존성 주입
```
from fastapi import FastAPI, Depends

app = FastAPI()

# 의존성 함수 정의
def get_api_key():
    return "my-secret-api-key"

# 경로 함수에서 의존성 주입
@app.get("/items/")
async def read_items(api_key: str = Depends(get_api_key)):
    return {"api_key": api_key}
```
* `get_api_key`: 의존성 함수
* `Depends(get_api_key`: api_key 매개변수에 이 함수의 반환값이 주입됨.


## 데이터베이스 연결 의존성
```
from fastapi import FastAPI, Depends

app = FastAPI()

# 데이터베이스 세션 의존성 정의
def get_db():
    db = {"connection": "database_session"}
    try:
        yield db  # 생성된 세션을 반환
    finally:
        print("DB 세션 종료")  # 요청 완료 후 정리 작업 수행

@app.get("/users/")
async def read_users(db: dict = Depends(get_db)):
    return {"db_connection": db["connection"]}
```
* `get_db`: db 세션 객체 생성
* `yield`: db 세션 객체를 반환하고 요청 완료 후 리소스 해제를 수행함
* `depends(get_db)`: 의존성 주입 부분



## 인증/권한
```
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# 인증 의존성
def verify_token(token: str):
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

# 경로 함수
@app.get("/protected/")
async def protected_route(token: str = Depends(verify_token)):
    return {"message": "Access granted", "token": token}
```
* `verify_token`: 인증을 수행하는 의존성 함수
* `Depends(verify_token))`: 의존성 함수인 `verify_token`의 인자값은 FastAPI [[(작성중)Depends]] 함수를 통해 자동으로 [[(작성중)요청_컨텍스트]]에서 추출하여 전달함.



## 다중 의존성
```
from fastapi import FastAPI, Depends

app = FastAPI()

def dependency_a():
    return "A"

def dependency_b():
    return "B"

@app.get("/multiple/")
async def read_multiple(a: str = Depends(dependency_a), b: str = Depends(dependency_b)):
    return {"a": a, "b": b}
```



# 정리
* `의존성`이란 코드가 동작하기 위해 필요한 외부 자원(데이터베이스, 설정, 인증 등)을 의미함.
* `의존성 주입`이란 필요한 의존성을 외부에서 관리하고 주입 받는 패턴을 의미함.
* FastAPI에서는 `Depends`를 사용해 의존성을 주입하며, 이를 통해 코드 재사용성과 유지보수성을 높힘.
* `의존성 주입`은 인증, 데이터베이스 연결, 테스트 등 다양한 작업에서 강력한 이점을 제공함.