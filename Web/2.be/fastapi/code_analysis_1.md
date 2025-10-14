
# snippet_1

```
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }

class TodoItem(BaseModel):
    item: str
    
    class Config:
        schema_extra = {
            "example": {
            "item": "Read the next chapter of the book"
        }  
    }
```

## class 내 Config class는 뭘까?
- Pydantic의 `BaseModel` 안에 내부 클래스로 선언해서 사용하는 **설정용 클래스**

## BaseModel의 Config class 에서 자주 사용되는 옵션
- `orm_mode`
	- ORM 객체도 자동으로 반환해줌 (FastAPI에서 DB 연동시 필요)
	```
	class Config:
	    orm_mode = True
	```
	
- `allow_population_by_field_name = True`
	- 별칭(`alias`)이 있는 필드도 실제 필드 이름으로 값을 할당 가능하게 함.
	```
	class Config:
	    allow_population_by_field_name = True
	```
	
- `schema_extra`
	- Swagger/OpenAPI 문서에 보여줄 example data 지정
	- `example`키로 예시 데이터를 넣어주면, Swagger UI 같은 API 문서 화면에서 "예시"로 자동 출력 됨.
	- 실제 데이터 검증에는 사용하지 않으며, **문서화에만 영향을 줌.**
	```
	from enum import Enum
	class StatusEnum(str, Enum):
	    ACTIVE = "active"
	    INACTIVE = "inactive"
	class User(BaseModel):
	    status: StatusEnum
	    class Config:
	        use_enum_values = True	
	```
	
- `use_enum_values`
	- Enum 타입 필드를 응답할 때 실제 값(value)만 반환
	```
	from enum import Enum
	class StatusEnum(str, Enum):
	    ACTIVE = "active"
	    INACTIVE = "inactive"
	class User(BaseModel):
	    status: StatusEnum
	    class Config:
	        use_enum_values = True
	```

- `anystr_strip_whitespace`
	- String 입력 값의 앞뒤 공백 자동 제거
	```
	class Config:
	    anystr_strip_whitespace = True
	```

- `extra`
	- 모델에 정의되지 않은 추가 필드가 들어올 때 **허용/거부/무시** 여부를 결정
		- `forbid`: 추가 필드가 있으면 에러 발생
		- `ignore`: 무시함
		- `allow`: 허용함
	```
	class Config:
	    extra = "forbid"
	```

- `json_encoders`
	- 특정 타입(datetime, Decimal)을 json으로 변환할 때 커스텀 인코딩 함수 지정
	```
	from datetime import datetime
	class Config:
	    json_encoders = {
	        datetime: lambda v: v.strftime('%Y-%m-%d')
	    }
	```

- `fields`
	- 특정 필드의 OpenAPI 문서 정보를 세부적으로 지정
	```
	class Config:
	    fields = {
	        'id': {'description': '고유 식별자', 'example': 1},
	        'item': {'description': '할 일 내용', 'example': '책 읽기'}
	    }
	```

- `validate_assignment`
	- 모델 인스턴스를 만든 뒤 필드 값을 변경할 때도 자동 검증 실행
	```
	class Config:
	    validate_assignment = True
	```

# 추가 내용
[pydantic config doc](https://docs.pydantic.dev/latest/api/config/) 참고
