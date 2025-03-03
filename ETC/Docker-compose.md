# Docker-compose

## 정의
여러 개의 컨테이너로 구성된 어플리케이션을 손쉽게 정의하고 실행할 수 있도록 하는 도구.


## 장점

1. 여러 개의 컨테이너를 하나의 설정 파일로 관리 가능
2. `depends_on` 을 사용해 컨테이너 실행 순서 제어 가능
3. 동일한 설정을 팀원들과 쉽게 공유 가능

___

## .env file
* `docker-compose.yml`에서 환경 변수를 사용하면 설정을 유연하게 관리할 수 있다.

* `.env` 파일
```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=mydb
```
* `docker-compose.yml`
```
version: '3.8'
services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
```

## 컨테이너 자동 재시작 설정
- 컨테이너가 비정상적으로 종료될 경우 자동으로 재시작하도록 설정 가능
```
version: '3.8'
services:
  web:
    image: nginx
    restart: always
```

## 여러 개의 `docker-compose.yml` file
- 환경별로 다른 설정을 적용하고 싶다면, 여러 개의 `docker-compose.yml` 파일을 사용
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```
`docker-compose.yml`: 기본 개발 환경
`docker-compose.prod.yml`: 운영 환경