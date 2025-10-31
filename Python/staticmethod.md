# 정의
- `@staticmethod` 클래스와 인스턴스 모두와 독립적인 메서드
- `self`나 `cls`를 인자로 받지 않음.
- class의 name space 내 있지만 클래스 변수나 인스턴스 변수에 접근할 수 없음.
- 단지, 클래스와 관련된 유틸리티 함수를 묶어둘 때 사용



# 사용 이유
- 클래스 내부 보조 함수
	- 클래스 로직에 관련된 단순 계산/변환/유틸리티 기능
- 인스턴스/클래스 변수 접근이 불필요한 경우
- 코드 구조화
	- 클래스 관련 함수를 한 곳에 묶어두기 위해
	- **특정 클래스에 종속될 필요는 없지만 그 클래스 내 논리적 영역 안에 포함되어야 할 때 사용**


# 예제 코드
## 기본 사용
```
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  # ✅ 8
```


## 호출 방식
```
class Converter:
    @staticmethod
    def cm_to_inch(cm):
        return cm / 2.54

    @staticmethod
    def inch_to_cm(inch):
        return inch * 2.54

# 클래스 이름으로 호출 가능
print(Converter.cm_to_inch(10))  # ✅ 3.937

# 인스턴스로도 호출 가능하지만 권장하지 않음
c = Converter()
print(c.inch_to_cm(3.937))       # ✅ 10.0
```

