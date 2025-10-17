# gRPC (google Remote Procedure Call)
- google이 만든 고성능 원격 호출(프로세스 간 통신) 프레임워크
- REST처럼 "리소스"기반이 아니라, 함수 호출 방식
- Protocol Buffers(바이너리 포맷) 사용 -> 데이터 전송 효율 높음.

# 동작 구조
- 서버: 함수 정의(`service userService { rpc GetUser (UserRequest) returns (UserReply); })
- 클라이언트: 그 함수를 직접 호출하듯 사용
- 내부적으로 HTTP/2 기반으로 통신


# 특징
- 장점
	- 속도 빠름(바이너리 전송 / 압축효율이 높음)
	- 타입 안정성(Protobuf 기반 스키마)
	- 양방향 스트리밍, 실시간 처리 강함
- 단점
	- 브라우저 직접 호출 어렵고, 일반 REST보다 설정 복잡
	- 디버깅/로깅 어렵고, HTTP/JSON 친화적 환경과 호환성 떨어짐

# 사용처
- 마이크로서비스 간 통신 / 백엔드 내부 서비스 호출 / 실시간 데이터 처리 / 고성능 API 서버
  (ex. FastAPI <-> ML model server / Go <-> Python 간 RPC 호출)

