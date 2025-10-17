
# 핵심 차이 비교
| 항목        | requests                                  | httpx                                                                    |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------ |
| 동기/비동기    | 동기 전용                                     | 동기 + **비동기**(async/await) 모두 지원                                          |
| HTTP 버전   | HTTP/1.1                                  | **HTTP/2 지원**(옵션 설치 `httpx[http2]`)                                      |
| 타임아웃 기본값  | 기본 **무한대**(꼭 직접 지정 권장)                    | 기본 **5초**(connect/read/write/pool 세분화)                                   |
| 세션/커넥션 풀  | `Session`                                 | `Client` (동기) / `AsyncClient` (비동기)                                      |
| 타입 힌트     | 부분적/제3자 stubs                             | **광범위한 타입 힌트** 내장                                                        |
| 예외 계층     | `requests.exceptions.RequestException` 중심 | `httpx.RequestError`, `httpx.HTTPStatusError`(raise_for_status) 등 명확히 분리 |
| HTTP/2 성능 | 미지원                                       | **멀티플렉싱**로 다수 요청에 유리(서버/네트워크 상황 따라 체감)                                   |
| 압축/인코딩    | gzip/deflate, brotli(추가 패키지)              | 동일(+ brotli 추가 패키지 시)                                                    |
| 프록시/인증    | 광범위한 예제/에코시스템                             | 유사 수준, **SOCKS** 등 옵션(예: `httpx[socks]`)                                 |
| 리트라이      | urllib3 `Retry`로 어댑터 구성                   | 내장 리트라이 없음 → **백오프 라이브러리** 권장                                            |
| 생태계/채택    | 매우 널리 사용, 안정적                             | 빠르게 성장, **FastAPI/Starlette** 진영과 궁합 좋음                                  |

# requests

## 주요 특징
- 동기성
- 간결한 api
- `Session`으로 커넥션 풀/쿠키 유지
- `urllib3` 기반 재시도 구성 가능
- 대용량 다운로드/업로드 스트리밍 쉬움


## 기본 코드
```
import requests
resp = requests.get("https://api.example.com/items", timeout=5)
resp.raise_for_status()
data = resp.json()
```

# httpx

## 주요 특징
- 동기 + 비동기(`Client` / `AsyncClient`)
- HTTP/2 지원
- 더 정밀한 Timeout
- 커넥션 Limits 제어
- 재시도를 transport 레벨에서 간단히 지정
- 이벤트 훅으로 로깅/트레이싱에 유용
- ASGI/WSGI 앱에 직접 요청 가능한 테스트 친화적 전송

## 기본 코드
```
import httpx
with httpx.Client(timeout=5.0) as client:
    resp = client.get("https://api.example.com/items")
    resp.raise_for_status()
    data = resp.json()
```
```
import asyncio, httpx

async def fetch_one(client, url):
    r = await client.get(url)
    r.raise_for_status()
    return r.json()

async def main(urls):
    async with httpx.AsyncClient(timeout=5.0, http2=True) as client:
        results = await asyncio.gather(*(fetch_one(client, u) for u in urls))
    return results

# asyncio.run(main(url_list))
```

# 요약
- requests > 간단한 동기식 호출, 폭넓은 예제/문서, 검증된 안전성
- httpx > 비동기 지원, HTTP/2, 보다 엄격한 타임아웃/타이핑, 현대적 API