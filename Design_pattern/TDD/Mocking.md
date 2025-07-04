# Mocking이란?
- 테스트 대상 코드가 외부 시스템(DB, API)에 의존하고 있을 때,
  이런 진짜 의존성을
  가짜(Mock) 객체로 대체해서 
  Test code에 실제 DB/API 호출이 없도록 하는 기법


# Mocking 실제 코드
```
from unittest.mock import patch

@patch("requests.get")
def test_get_user_from_api(mock_get):
    # 1. 가짜 응답(Mock Response) 만들기
    class MockResponse:
        def json(self):
            return {"name": "Alice"}
    
    mock_get.return_value = MockResponse()
    
    # 2. 실제로는 requests.get이 호출되지 않음!
    user = get_user_from_api(1)
    assert user["name"] == "Alice"
```


# Mocking 실무 적용
- 외부 의존성이 많을수록 Test code에서 Mock 적극 활용
- Test 실행 속도 및 일관성 보장
