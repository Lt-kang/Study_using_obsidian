# ThreadPoolExecutor


## 개념
* `ThreadPoolExecutor`는 여러 개의 thread를 pool로 만들어 작업을 병렬 처리 하는 방식
* I/O bound task에 적합함. (file I/O, 웹 요청, DB 처리)

## 기본 사용
```
from concurrent.futures import ThreadPoolExecutor

# 작업 함수 정의
def some_task(n):
    print(f"{n} 작업 중...")
    return n * 2

# ThreadPoolExecutor 사용
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(some_task, i) for i in range(5)]

    for future in futures:
        result = future.result()
        print(f"결과: {result}")
```

## ProcessPoolExecutor 와의 차이
|항목|ThreadPoolExecutor|ProcessPoolExecutor|
|--|--|--|
|처리방식|Thread|Process|
|GIL|영향을 받음 (병렬 cpu 처리 제한)|GIL 우회 (CPU 병렬 처리 가능)|
|적합한 작업|I/O bound|CPU bound|
|생성 비용|가볍고 빠름|상대적으로 무거움|
|메모리 공유|공유 메모리 사용|프로세스 간 메모리 분리(데이터 전달 필요)|


## GIL(Global Interpreter Lock)이란?
* python interpreter가 동시에 하나의 thread만 실행하도록 제한하는 잠금 장치
* GIL에 영향을 받는 `ThreadPoolExecutor`는 실제 병렬 처리가 불가하며, I/O 작업 대기 시간에만 이점이 있음.
* `ProcessPoolExecutor`는 여러 개의 독립적인 프로세스를 생성해서 GIL을 피할 수 있기 때문에 병렬 CPU 작업 가능.



