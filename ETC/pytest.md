# 1. pytest란?
## pytest란?
- python 테스트 자동화 프레임 워크
	- unit test 
	- functional test
	- integration test

## 특징
- 간결하고 직관적인 문법
- 다양한 테스트 유형 지원
- 플러그인 및 확장 기능이 풍부

## 예시
### 간단한 사용법
`assert`문을 그대로 사용
```
def test_add():
    assert 1 + 2 == 3
```

### 자동으로 테스트 함수 인식
- 파일명: `test_*.py` 또는 `*_test.py`
- 함수명: `test_`로 시작



# 2. 주요 개념
## Fixture
- 테스트 함수에 필요한 환경이나 데이터를 제공
- 함수, 클래스, 모듈, 세션 등 다양한 스코프 지정 가능
```
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```
## Parametrize
- 여러 케이스에 대해 반복적으로 테스트
```
import pytest

@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 20, 30),
])
def test_add(a, b, result):
    assert a + b == result
```

# 확장성 및 플러그인
- 코드 커버리지: `pytest-cov`
- 테스트 리프토: `pytest-html`
