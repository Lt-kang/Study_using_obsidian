# 정의
`@classmethod`는 class 자체를 첫 번째 인자로 받는 메서드


# 사용 이유
- 클래스 변수에 접근하거나 변경할 때 사용
- 인스턴스를 생성하지 않아도 호출 가능하다는 장점이 있음.


# 예제 코드
## 일반 사용 방법
```
class Dog:
    species = "Canine"  # 클래스 변수

    def __init__(self, name):
        self.name = name  # 인스턴스 변수

    @classmethod
    def get_species(cls):
        return cls.species


# 클래스 이름으로 호출 가능
print(Dog.get_species())  # ✅ "Canine"

# 인스턴스로도 호출 가능
d = Dog("Buddy")
print(d.get_species())    # ✅ "Canine"
```


## 대체 생성자 활용
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 문자열을 파싱해서 객체 생성
    @classmethod
    def from_string(cls, info_str):
        name, age = info_str.split(",")
        return cls(name.strip(), int(age))

# 일반 생성자 사용
p1 = Person("Alice", 30)

# 클래스 메서드를 통한 대체 생성자
p2 = Person.from_string("Bob, 25")

print(p2.name)  # ✅ Bob
print(p2.age)   # ✅ 25
```

## 클래스 변수 변경 예제
```
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def reset_count(cls):
        cls.count = 0


c1 = Counter()
c2 = Counter()
print(Counter.count)  # ✅ 2

Counter.reset_count()
print(Counter.count)  # ✅ 0
```

