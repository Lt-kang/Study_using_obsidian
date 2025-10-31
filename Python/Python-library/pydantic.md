https://rudaks.tistory.com/entry/python-pydantic%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

# pydantic 정의
type hinting을 적극 활용하여 data validation test를 진행하는 프레임워크.
런타임 시 data type이 일치하지 않을 경우 오류를 반환함.

# pydantic 주요 특징
1. type validation: 모델에 정의된 데이터 타입에 따라 자동으로 유효성 검사를 함.
2. 자동 형 변환: 전달된 데이터가 정의된 타입과 일치하지 않을 경우 가능한 범위 내에서 자동으로 형 변환을 시도.
3. 필드의 기본값 지원: 필드에 기본값 설정하여 사용자가 데이터를 제공하지 않더라도 유효한 모델을 만들 수 있음.
3. 복잡한 데이터 구조 지원: pydantic은 list, dictonary, duplicated model과 같은 복잡한 데이터 구조를 지원함.

___
___

# 주요 예시코드

## pydantic model 생성
* pydantic을 사용하는 기본적인 방법은 `BaseModel` 클래스를 상속하여 모델을 정의하는 것.
```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user_data = {
    'id': '123',  # 문자열로 제공된 숫자도 자동으로 변환됨
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}

user = User(**user_data)
print(user)
```

___

## data validation test
* 특정 조건을 만족해야 하는 데이터 검사 가능.
* 아래 예시는 email 형식을 검사하는 방법
```
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr  # 이메일 형식이 아닌 데이터는 오류 발생

try:
    user = User(id=1, name='Jane Doe', email='invalid-email')
except ValueError as e:
    print(e)
```

___

## 필드에 대한 세부 설정
* pydantic은 각 필드에 대해 더 세부적인 설정을 할 수 있는 옵션을 제공.
* 필드가 Optional일 경우 혹은 default값을 설정하는 것도 가능

```
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr  # 이메일 형식이 아닌 데이터는 오류 발생

try:
    user = User(id=1, name='Jane Doe', email='invalid-email')
except ValueError as e:
    print(e)
```
___

## numeric field의 range 설정
* Field를 활용하여 숫자형 필드의 입력 허용 범위를 설정 가능

```
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., ge=1, le=100)  # 1 이상 100 이하의 정수만 허용
    age: int = Field(..., ge=0, lt=120)  # 0 이상 120 미만의 정수만 허용
    score: int = Field(default=50, ge=0, le=100)  # 0 이상 100 이하의 정수, 기본값 50

try:
    # 유효한 데이터
    valid_user = User(id=5, age=30, score=85)
    print(valid_user)
    
    # 유효하지 않은 데이터
    invalid_user = User(id=101, age=25)  # id가 범위를 벗어남
except ValueError as e:
    print(e)
```

___

## json schema와 예제 정의
* pydantic은 자동으로 json schema를 생성하여 api 문서화를 도움.
* `Field`를 사용하여 필드에 대한 예제를 정의함.

```
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., example="Smartphone")
    price: float = Field(..., example=699.99)

print(Item.schema_json(indent=2))
```

___

## custom validators
* 기본적인 타입 검사 외에도 pydantic은 각 필드에 대해 사용자 정의 유효성 검사를 추가할 수 있다.
* `@validator` 데코레이터를 사용하여 필드의 값이 특정 조건을 만족하도록 설정

```
from pydantic import BaseModel, validator, field_validator

class Product(BaseModel):
    name: str
    price: float

    # 가격이 0보다 커야 한다는 조건 추가
    @field_validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v

try:
    product = Product(name="Laptop", price=-1000)
except ValueError as e:
    print(e)
```

___

## 클래스 전체에 대한 유효성 검사
* pydantic은 필드 단위의 유효성 검사 외에도 class 전체에 대한 유효성 검사를 지원.
* `@root_validator`를 사용.

```
from pydantic import BaseModel, root_validator, model_validator

class Order(BaseModel):
    item_count: int
    total_price: float

    # 전체 데이터에 대한 유효성 검사
    # mode = before일 경우 pydantic 모델이 파싱되기 전에 필드값을 검사함.
    # after일 경우 파싱 이후 검사.
    @model_validator(mode="before")
    def check_order(cls, values):
        item_count = values.get("item_count")
        total_price = values.get("total_price")
        if total_price < item_count * 10:  # 최소 단가가 10원 이상이어야 함
            raise ValueError("Total price is too low for the item count")
        return values

try:
    order = Order(item_count=5, total_price=40)
except ValueError as e:
    print(e)
```

___

## 상속 및 재사용 가능한 모델
* pydantic 모델은 상속을 통해 쉽게 재사용 가능.
* 기본 모델에 확장하여 새로운 필드를 추가하거나 기존 필드를 수정할 수 있음.

```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class Admin(User):
    access_level: int

admin = Admin(id=1, name="Alice", access_level=5)
print(admin)
```

___

## 동적 모델 생성
* pydantic은 프로그램 실행 중 동적으로 모델을 생성할 수 있는 기능 제공
* 데이터 구조가 동적으로 변할 수 있는 상황에서 유용
```
from pydantic import create_model

# 동적으로 새로운 모델 생성
DynamicModel = create_model("DynamicModel", foo=(str, ...), bar=(int, 42))

instance = DynamicModel(foo="Hello")
print(instance.model_dump())  # {'foo': 'Hello', 'bar': 42}
```

___

## ORM 모드 지원

___

## 컴플렉스 데이터 타입

___

## 데이터 변환 및 직렬화

___

## 성능 최적화

___

## 환경 변수로부터 설정 관리
* 환경 변수에서 설정을 자동으로 불러오는 기능 제공
* `BaseSettings` class 사용하면 애플리케이션에서 환경 설정을 쉽게 관리할 수 있음.
### 환경변수에서 설정 불러오기
```
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int

    model_config = {
        "env_file": "../.env"
    }

config = AppConfig()
print(config.app_name)
print(config.admin_email)
print(config.items_per_user)
```
### 동적 환경 설정
```
from pydantic import BaseSettings

class AppConfig(BaseSettings):
    debug: bool = False
    database_url: str
    secret_key: str

    model_config = {
        "env_prefix": "MYAPP_"
    }

config = AppConfig(_env_file='.env')
print(config.debug)
```
___

## 복잡한 데이터 모델 관리
* 중첩된 데이터 모델을 사용하여 더욱 복잡한 데이터 구조 처리 가능
```
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city: str
    postal_code: str

class User(BaseModel):
    name: str
    address: Address

user_data = {
    "name": "John",
    "address": {
        "city": "New York",
        "postal_code": "10001"
    }
}

user = User(**user_data)
print(user)
```