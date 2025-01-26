# 예시 코드 / 헤더에서 token값 받기


* 코드
```
from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

# 인증 의존성 함수
def verify_token(token: str = Header(...)):  # 헤더에서 'token' 값을 찾음
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/protected/")
async def protected_route(token: str = Depends(verify_token)):
    return {"message": "Access granted", "token": token}
```

* 요청 컨텍스트
```
curl -X GET "http://127.0.0.1:8000/protected/" -H "token: valid-token"
```
``