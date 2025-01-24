# Response Model이란?
* fastapi에서 응답의 데이터를 구조화하고 검증하기 위해 사용됨.
* `Pydantic`을 사용하여 정의함.
* 클라이언트에 반환되는 데이터의 형식을 명확히 규정하는 데 사용.


# 주요 목적
* 응답 데이터의 구조 정의: 클라이언트로 반환될 데이터의 타입과 구조를 명시함.
* 데이터 검증: 서버가 반환하는 데이터가 응답 모델에 적합한지 확인하며 오류나 부적절한 데이터를 방지함.
* 보안 및 데이터 필터링: 데이터 중 일부 민감한 정보를 제외하고 클라이언트에게 반환할 수 있음.


# 예제 코드
## 기본 응답 모델
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 요청 모델
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# 응답 모델
class ItemResponse(BaseModel):
    name: str
    price: float

@app.post("/items/", response_model=ItemResponse)
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}
```
* `Item`: 클라이언트로부터 요청이 들어오는 데이터 구조
* `ItemResponse`: 클라이언트에게 반환되는 응답 데이터 구조


##  필터링
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 요청 모델
class User(BaseModel):
    username: str
    password: str

# 응답 모델
class UserResponse(BaseModel):
    username: str

@app.post("/users/", response_model=UserResponse)
async def create_user(user: User):
    # 응답에서 password는 제외
    return user

```
* 클라이언트로부터 `username`과 `password`를 입력 받지만 반환은 `username`만 반환함.

