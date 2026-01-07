# snippet_2
```
@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }
```

## status_code
- HTTP 응답 코드를 명시적으로 지정하는 역할
- 서버가 어떤 결과를 반환했는지 표준화된 숫자로 알려주는 기능

## code snippet에서의 status_code 의미
- api endpoint에서 post 요청이 성공적으로 처리될 경우, 201 status code를 반환하겠다는 의미
- status_code의 반환값은 1개만 설정 가능(요청이 성공적으로 처리 되었을 경우에 대한 설정)
- `Exception`발생시에 대한 처리
	```
	from fastapi import HTTPException
	
	@todo_router.post("/todo", status_code=201)
	async def add_todo(todo: Todo):
	    if not todo.item:
	        raise HTTPException(status_code=400, detail="item은 필수입니다.")
	    # 정상 로직...
	```
	```
	@todo_router.get("/todo/{todo_id}")
	async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
	    for todo in todo_list:
	        if todo.id == todo_id:
	            return {
	                "todo": todo
	            }
	    raise HTTPException(
	        status_code=status.HTTP_404_NOT_FOUND,
	        detail="Todo with supplied ID doesn't exist",
	    )
	```
	- 위와 같이 if문과 `HTTPException`을 통해 Exception에 대한 status_code를 반환할 수 있습니다.

- 정상 응답에 대한 status code도 지정 가능
	```
	from fastapi import Response
	
	@todo_router.post("/todo")
	async def add_todo(todo: Todo, response: Response):
	    if some_condition:
	        response.status_code = 202
	        return {"message": "Accepted"}
	    # 기본은 200 OK로 반환
	    return {"message": "OK"}
	```
	