
___
# Back-end 관련
## EC2 (Elastic Compute Cloud)
- AWS에서 가장 기본적인 가상 머신(VM) 서비스
- 특징
	1. **직접 서버를 구성하고 운영할 수 있음.**
	2. 원하는 스펙(cpu/ram/disk)을 선택하여 **맞춤형 인스턴스 실행 가능**
	3. ssh로 접속하여 수동으로 설정 가능
	4. **docker 컨테이너 실행 가능**


## ECS (Elastic Container Service)
- Docker 컨테이너를 AWS에서 쉽게 배포하는 서비스
- 특징
	1. **Fargate 모드: 서버 없이 컨테이너만 실행 가능**
	2. **EC2 모드: EC2 인스턴스 위에서 컨테이너를 실행하는 방식**
	3. ALB(Application **Load Balancer**)와 연동하여 트래픽을 자동 분산 가능
	4. Docker 컨테이너 기반의 fast-api, Django, Express 서버 배포
	5. **마이크로서비스 아키텍처(MSA) 구현**
	6. **Server-less 아키텍처와 결합하여 배포**


## EKS (Elastic Kubernetes Service)
- AWS에서 Kubernetes 클러스터를 쉽게 운영할 수 있도록 지원하는 서비스
- 특징
	1. **Kubernetes 클러스터를 자동으로 관리/확장 가능**
	2. 온프레미스, 멀티 클라우드 환경에서도 연동 가능
	3. MSA와 대규모 트래픽을 처리하는데 유리
	4. 대규모 서비스에서 Kubernetes 기반 백엔드 API 배포
	5. MSA 환경 구축시 활용


## Lambda (AWS Lambda)
- 서버 없이 코드를 실행하는 Server-less 컴퓨팅 시스템
- 특징
	1. **이벤트 기반 실행 (API Gateway, S3, DynamoDB 연동)**
	2. 짧은 시간 동안 실행해야 하는 Server-less api 구축 가능
	3. 비용 절감 효과 (사용한 만큼만 과금)
	4. FastAPI, Flask 같은 Python 백엔드 API를 server-less로 실행
	5. image 업로드 후 자동 resizing 같은 이벤트 기반 처리
	6. chat-bot / ai 모델의 특정 기능만 빠르게 실행할 때 활용


## Elastic Beanstalk
- AWS에서 애플리케이션을 쉽게 배포할 수 있도록 도와주는 Paas(Platform as a Service)
- 특징
	1. EC2, RDS, S3, Load Balancer 등의 인프라를 자동으로 설정 및 관리
	2. **Docker 컨테이너, Node.js, Python(Fast-api, Flask, Django) 등을 지원**
	3. **간단한 웹 애플리케이션 배포에 유용 / 단, 복잡한 설정은 어려움.**


___
# AI 관련

## Segemaker
- AWS에서 머신러닝 모델을 쉽게 훈련하고 배포할 수 있도록 지원하는 ai 플랫폼
- 특징
	1. **ML 모델의 학습 / 평가 / 배포까지 통합 관리**
	2. GPU를 활용하여 모델 훈련 가속화
	3. Jupyter Notebook 기반 환경
	4. pre-trained model 기반 custom ai 솔루션 개발
	5. AutoML을 활용한 자동 모델 최적화


## Rekognition
- Computer Vision API service
- 특징
	- 얼굴 인식 / 객체 탐지 / 텍스트 감지 기능 제공 
	- 실시간 비디오 분석 가능
	- API 호출만으로 이미지 분석 기능 사용 가능
	- 얼굴 인식을 활용한 출입 보안 시스템 구축
	- 동영상 장면 분석
	- OCR 기능을 통한 문서 자동화 처리

## Comprehend
- NLP service
- 특징
	- 문서 내 키워드/감정 분석/엔터티 추출
	- 여러 언어를 지원하는 ai 기반 분석 api 제공
	- 고객 피드백 / 리뷰 데이터에서 감정 분석
	- 뉴스 / 문서에서 중요한 키워드 추출
	- 챗봇 / 고객 응대 시스템에 적용 가능


## Polly
- TExt-to-Speech service
- 특징
	- 자연스러운 음성 합성
	- 다양한 언어/음성 지원

## Transcribe
- Speech-to-Text service
- 특징
	- 음성을 텍스트로 변환 가능


___
# ETC

## Lightsail
- 쉽고 저렴한 VPS(Virtual Private Server) Service
- 특징
	- **EC2보다 설정이 간단하고 저렴함.**
	- **정해진 월 요금제로 비용이 예측 가능함.**
	- 웹사이트/블로그 등의 간단한 api 서버 등을 쉽게 배포
	- 고정 IP / storage / DNS 관리 / road balancer 제공
	- 단, 고성능 컴퓨팅(대규모 트래픽/ai학습)이 필요한 경우에는 적합하지 않음.
	- Auto Scaling 기능이 필요한 경우에는 적합하지 않음.
	- 네트워크 설정을 자유롭게 변경해야 하는 경우 적합하지 않음.
	![[Pasted image 20250303180433.png]]


## Amplify
- Front-end + Back-end 서버를 쉽게 배포할 수 있도록 지원하는 Full-stack platform
- 특징
	- React / Vue / Angular 등 프론트 엔드 애플리케이션을 쉽게 배포 가능
	- GraphQL API(AppSync) 및 Server-less Back-end(Lambda, DynamoDB) 자동 연결
	- 사용자 인증 기능(Cognito) 연동 가능
	- 스타트업, 프로토타입 개발 등 빠르게 Full-stack을 배포할 때 유용


## CloudFront
- CDN(Content Delivery Network) Service
- 특징
	- 전 세계에 분산된 엣지 로케이션을 통해 빠른 컨텐츠 제공 가능
	- S3, Lightsail, EC2, API Gateway 등과 연동 가능
	- HTTPS 트래픽 및 보안 기능 (AWS Shield, AWS WAF) 제공
	- 정적 웹사이트 (html / css / js) 캐싱 & 배포
	- 이미지/동영상 같은 대용량 컨텐츠 제공 속도 개선
	- api 응답 속도를 빠르게 하기 위한 캐싱


## API Gateway
- REST API 및 WebSocket API를 쉽게 배포할 수 있는 Service
- 특징
	- Lambda와 함께 완전한 Server-less api 구축 가능
	- EC2, ECS 등과 연동하여 api gateway 역할 수행
	- 사용량 제한(Rate Limit), 인증(Authentication) 기능 제공
	- Lambda 기반 REST API 개발 (FastAPI, Flask 등과 연동 가능)
	- 모바일 앱 / 프론트엔드 / 백엔드 api 연결
	- api 보안 및 모니터링(API Key, IAM 인증 등)


## DynamoDB
- 완전 관리형 NoSQL 데이터베이스
- 특징
	- AWS에서 자동으로 확장되는 고성능 Key-Value DB
	- server-less로 동작하며 사용한 만큼만 비용 지불
	- AWS Lambda, API Gateway, Amplify 등과 잘 연동됨.
	- 대규모 트래픽이 필요한 api
	- server-less 아키텍처 기반 데이터 저장
	- 세션 관리 / 실시간 데이터 저장


## Cognito
- 사용자 인증(로그인) Service
- 특징
	- OAuth, JWT, SSO, 소셜 로그인(Google, Facebook 등) 지원
	- Amplify와 쉽게 연동 가능
	- 사용자 그룹, 권한 관리 가능
	- React / Vue / Next.js 기반 로그인 기능 추가
	- API 인증 (JWT 토큰 기반 인증 처리)


## Bedrock
- ChatGPT 같은 생성형 AI 모델을 쉽게 활용할 수 있는 AWS service
- 특징
	- OpenAI, Anthropic Claude, Stability AI 등의 모델을 AWS에서 사용 가능
	- API 호출 만으로 AI 모델 활용 가능
	- 데이터 프라이버시 & 보안 기능 강화
	- Caht-bot Service 개발 (자연어 처리 ai)
	- image generate (Stable Diffusion)


___
![[Pasted image 20250303175851.png]]![[Pasted image 20250303182508.png]]