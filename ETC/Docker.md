# Docker


## 정의 
컨테이너 기반의 가상화 기술 제공 플랫폼. 어플리케이션과 그에 필요한 모든 종속성을 하나의 컨테이너로 패키징하여 어디서든 동일한 실행 환경을 구축할 수 있게 해줌.


## 주요 개념

### 1. 이미지(Image)
* 컨테이너 실행에 필요한 파일 시스템과 어플리케이션을 포함한 Immutable한 템플릿
* `docker run` 명령어로 실행

### 2. 컨테이너(Container)
* 독립적으로 실행되는 가상 환경 (이미지를 실행한 것)
* 호스트 os의 커널을 공유하여 가볍고 빠름
* 실행 중인 컨테이너는 상태를 가짐 (일시 정지 / 중지 / 실행 등)
* `docker ps` 명렁어로 실행 중인 컨테이너 목록 확인 가능

### 3. 레지스트리(Registry)
* Docker 이미지를 저장하고 배포하는 저장소
	* Docker hub / AWS ECR / Google Container Registry
* `docker pull <image>` 명렁어로 이미지 다운로드 가능

### 4. 볼륨 (Volume)
* 컨테이너가 종료되어도 데이터가 유지될 수 있도록 지원하는 저장소
	* `docker volume create` 
	* `docker run -v my_volume:/data ubuntu`


## 장점
2. 실행 환경의 일관성 유지
3. 가벼운 컨테이너 (의존성에 필요한 것들만 최소한으로 유지하기 때문)
4. 확장성이 뛰어남.
5. 의존성 충돌 방지



___


## Docker Network
### 1. bridge (기본 네트워크)
* 컨테이너 간 통신 가능 (`docker run`시 기본 적용 됨)
* `docker network create my_bridge`

### 2. host (호스트 네트워크)
* 컨테이너가 호스트의 네트워크를 직접 사용 (성능 향상 가능)
* `docker run --network host`

### 3. none (네트워크 미사용)
* 네트워크 기능이 필요 없는 컨테이너에 적합
* `docker run --network none`

### 4. overlay (다중 호스트 네트워크)
* Docker Swarm을 사용할 때 여러 호스트 간 네트워크를 구성할 때 사용

### 5. macvlan (물리적 네트워크와 연결)
* 컨테이너에 고유한 [[MAC 주소]]를 부여하여 외부 네트워크와 직접 연결

## Volume & Bind Bount
* 컨테이너 내부의 데이터는 기본적으로 컨테이너가 삭제되면 사라짐. 데이터를 유지하기 위해 Volume 또는 Bind Mount를 사용해야 함.

### 1. Volume
* 컨테이너가 삭제되더라도 데이터 유지

### 2. Bind Mount
* 호스트 머신의 특정 디렉토리를 컨테이너와 공유
* `docker run -v /home/user/data:/container_data ubuntu`


## Dockerfile 최적화
### 1. 멀티 스테이지 빌드(Multi-stage Build)
* 빌드 환경과 실행 환경을 분리하여 최적화
```
FROM node:16 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
```
### 2. 캐시를 활용한 빌드 속도 최적화
* 변경되지 않는 부분을 위쪽에 배치
```
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```
### 3. `.dockerignore` 파일 사용
* 불필요한 파일 제외하여 빌드 속도 향상
```
.git
__pycache__
node_modules
```