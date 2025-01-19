
# 요약
* GET: 데이터 조회
* POST: 데이터 생성
* PUT: 데이터 수정
* DELETE: 데이터 삭제


# GET
* 서버에서 데이터를 **조회**할 때 사용.
* 서버의 상태나 데이터를 변경하지 않음.
```
from fastapi import FastAPI 
app = FastAPI() 

@app.get("/items/{item_id}") 
async def read_item(item_id: int): 
    return {"item_id": item_id}
```


# POST
* 서버에 새로운 데이터를 생성 혹은 제출할 때 사용.
* 클라이언트는 서버에 데이터를 보내고 서버는 이를 처리함.
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item '{item.name}' created successfully"}
```

# PUT
* 서버에 이미 존재하는 데이터를 수정/업데이트할 때 사용.
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}
``` 


# DELETE
* 서버에서 특정 데이터를 삭제할 때 사용.
* 클라이언트는 삭제를 요청하고 서버에서는 요청을 처리(삭제)함.
```
from fastapi import FastAPI

app = FastAPI()

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}
```