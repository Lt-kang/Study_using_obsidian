- 정적 타입 힌트(static type hints)를 지원하기 위한 표준 라이브러리


## 목적
- 가독성 향상: 함수 클래스의 입력/출력 타입을 명시적으로 표현해 코드 의도를 명확히 함
- 정적 분석: `mypy`, `pyright`, `pylance` 같은 타입 체커가 잠재적 버그를 컴파일 타임에 잡아줌
- 런타임 안정성: `pydantic`, `beartype` 같이 런타임 검사를 수행하는 프레임 워크와 연동 가능


## 주요 타입 힌트 요소

### `List`, `Dict`, `Tuple`, `Set`, `Iterable`, `Sequence`
- 컬렉션 타입을 요소 타입과 함께 명시
- `Iterable`:  iterable한 객체
- `Sequence`: 순서가 있는 컬렉션. (Iterable의 하위 개념)
```
from typing import List, Dict, Tuple, Set, Iterable, Sequence

def sum_all(nums: List[int]) -> int:
    return sum(nums)

def get_scores() -> Dict[str, float]:
    return {"math": 95.5, "science": 88.0}

def unpack() -> Tuple[int, str, bool]:
    return (1, "hello", True)

def get_unique(words: Iterable[str]) -> Set[str]:
    return set(words)

def get_top3(seq: Sequence[int]) -> List[int]:
    return sorted(seq, reverse=True)[:3]
```

### `Union` / `|`
- 두 개 이상의 타입 중 하나일 수 있음을 명시

```
from typing import Union

def stringify(x: Union[int, float, str]) -> str:
    return str(x)

# Python 3.10+에서 가능
def parse(x: int | str) -> int:
    return int(x)
```

### `Optional[T]` = `Union[T, None]`
- 값이 있거나(None일 수도 있음)을 표현

```
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, anonymous!"
```

### `Any`
- 모든 타입을 허용(type checker 무시)
```
from typing import Any

def log_data(data: Any) -> None:
    print(f"Received: {data}")
```


### `Callable`
- 함수 시그니처를 타입으로 명시할 때 사용
```
from typing import Callable

def compute(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

add = lambda a, b: a + b
result = compute(3, 4, add)  # 7
```


### `Literal`
- 정해진 상수 값 중 하나만 허용

```
from typing import Literal

def set_mode(mode: Literal["debug", "release"]) -> None:
    print(f"Mode is {mode}")

```

### `TypedDict`

- 딕셔너리의 key-value 스키마를 정의

```
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str

def print_user(user: User) -> None:
    print(user["name"], user["email"])

```

### `TypeVar` & `Generic`

- 제네릭 타입(타입 파라미터화)를 지원

```
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

s = Stack[int]()
s.push(3)
print(s.pop())  # 3

```

### `Annotated`

- 추가 메타정보를 붙인 타입
```
from typing import Annotated

Age = Annotated[int, "Must be >= 0"]
```
#### **LangGraph에서의 예시**
```
# 현재 state
state = {"input_text": "ChatGPT is a useful tool."}

# 함수 정의
def summarize(input_text: Annotated[str, "input_text"]) -> Annotated[str, "summary"]:
    return input_text[:20]

# 실행 후 state는 이렇게 됨
state = {
    "input_text": "ChatGPT is a useful tool.",
    "summary": "ChatGPT is a usef"
}
```

### `Protocol` (구조적 서브 타이핑)

- 구조 기반 인터페이스 (Duck Typing)

```
from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str: ...

class Korean:
    def greet(self) -> str:
        return "안녕하세요"

def say_hello(person: Greeter):
    print(person.greet())

say_hello(Korean())  # OK
```

