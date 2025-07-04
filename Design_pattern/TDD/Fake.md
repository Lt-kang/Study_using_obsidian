# Fake 란?
- 실제로 동작하지만, 아주 단순화된 버전의 가짜 객체
- [[Stub]]보다 더 진짜처럼 동작하지만, 실제 환경보다 훨씬 가볍고 빠르게 설계된 게 특징


# 특징
- 실제 로직이 있긴 하지만, 테스트 환경에 맞춰 간략화된 구현체
- 실제로 CRUD 등 동작이 가능


# 적용 환경
- 데이터 CRUD나 여러 조건별 로직이 필요할 때
- 여러 케이스를 실제와 가깝게 흉내내고 싶을 때

# 실전 코드
```
# 실제 코드에서는 진짜 DB 연동
class RealDatabase:
    def save_user(self, user):
        # DB 연결, INSERT 등 진짜 동작
        ...

# Fake DB (테스트용)
class FakeDatabase:
    def __init__(self):
        self.users = []
    def save_user(self, user):
        self.users.append(user)  # 메모리 리스트에 저장
```