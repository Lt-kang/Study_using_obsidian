- `async/await` 구문
	- python 비동기 프로그래밍을 위한 핵심 문법. 
	- 동시성(Concurrency)을 효율적으로 처리하기 위해 도입. 
	- **I/O bound 작업**(ex. api 호출, 파일 읽기, 네트워크 요청)에 효과적임.

- 비동기 프로그래밍이란?
	- 느린 작업을 기다리는 동안, 다른 작업을 먼저 수행할 수 있도록 하는 방식.


## 기본 개념 요약
|개념|설명|
|---|---|
|`async def`|비동기 함수 정의|
|`await`|다른 비동기 함수 호출 시 사용|
|`asyncio`|Python 기본 비동기 프레임워크|
|`coroutine`|`async def`로 정의된 함수 객체|
|`event loop`|비동기 작업을 스케줄링하는 시스템|


## 실제 예시
### `asyncio.gather`: 여러 작업을 병렬로 실행
```
async def task(name, delay):
    print(f"{name} 시작")
    await asyncio.sleep(delay)
    print(f"{name} 완료")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1)
    )

asyncio.run(main())
```
```
A 시작
B 시작
B 완료
A 완료
```

### `asyncio.create_task`: 작업 예약 후 나중에 기다림
```
async def background_job():
    await asyncio.sleep(1)
    print("백그라운드 완료")

async def main():
    task = asyncio.create_task(background_job())
    print("메인 로직")
    await task  # 실제 기다리기

asyncio.run(main())
```

## ETC

### `await`는 어디서만 쓸 수 있을까?
- `await`는 반드시 `async def`함수 안에서만 사용할 수 있음.


### `coroutine was never awaited` 오류
비동기 함수를 호출만 하고 `await`를 하지 않으면 발생함.

#### 오류
```
async def my_func():
    ...

my_func()  # ❌ 이렇게 하면 coroutine 객체만 반환
```

#### 정상
```
await my_func()  # ✅ 직접 await
# 또는
asyncio.run(my_func())  # ✅ 메인 함수 실행 시
```

## 대표 라이브러리
|목적|라이브러리|
|---|---|
|HTTP 클라이언트|`aiohttp`, `httpx`|
|WebSocket|`websockets`|
|FastAPI 서버|`FastAPI`, `Starlette`|
|파일 I/O|`aiofiles`|

## 결론: `async/await`는 언제 쓰는가?

- 💻 **I/O가 많은 작업**: API, 파일, DB, 네트워크 등    
- ⏱ **대기 시간이 많은 코드**: `sleep`, `wait`, `read`
- 🚀 **다수 작업을 동시에 처리하고 싶을 때**