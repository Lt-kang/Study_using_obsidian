list
- MLflow
- W&B
- Airflow
- Prefect
- Dagster


# MLflow
## 정체성
- ML 실험 관리
- model life cycle 관리

## 핵심 기능
- Experiment Tracking
	- parameter / metric / artifact 기록
- Model Registry
	- model version 관리
- Projects
	- 실행 환경 정의
- Model Serving


## 사용처
- hyper-parameter 실험이 필요할 때
- 모델 선택 근거로써 이 모델이 왜 좋은지 기록해야 할 때
- 팀 단위 ML 실험 관리

## 장/단점
- 장점
	- 오픈소스
	- 인프라 의존 적임
	- MLOps 입문에 적합
- 단점
	- UI/시각화는 단순함
	- 실험 비교 기능은 W&B보다 약함

> ML 실험 로그와 모델 버전의 기준점


___

# Weights & Biases
## 정체성
- 실험 시각화
- 협업 중심 ML 플랫폼

## 핵심 기능
- 실험 결과 실시간 시각화
- 실험 간 비교
- 모델 성능 추적
- dataset / model artifact 관리


## 사용처
- 실험이 많고 비교가 중요할 때
- 팀 단위 협업
- CV / LLM 실험

## 장/단점
- 장점
	- UI가 강력함
	- 실험 비교/분석 최고 수준
	- 협업에 최적
- 단점
	- SaaS 중심(보안 이슈)
	- 비용 발생 가능

> 실험을 눈으로 이해하게 해주는 도구

___

# Airflow

## 정체성
- 배치 기반 워크플로우 오케스트레이터


## 핵심 기능
- DAG 기반 작업 스케쥴링
- 의존성 관리
- 정기 배치 작업


## 사용처
- 하루/시간 단위 ETL
- 데이터 웨어하우스 파이프라인
- 안정성이 최우선일 때


## 장/단점
- 장점
	- 업계 표준
	- 안정적
	- 대규모 조직에 적합
- 단점
	- 설정 복잡
	- 실시간/동적 워크플로우에 약함
	- ML 파이프라인엔 다소 무거움

> 배치 데이터 파이프라인의 교과서


___


# Prefect

## 정체성
- Pythonic하고 유연한 워크플로우 오케스트레이터


## 핵심 기능
- python 함수 그대로 flow 구성
- 동적 분기
- 에러 핸들링 강력
- 클라우드/온프레미스 지원


## 사용처
- ML 파이프라인
- 실험적/유연한 워크플로우
- 빠른 개발이 필요할 때


## 장/단점
- 장점
	- 코드 가독성 좋음
	- ML 친화적
	- 설정 부담 적음
- 단점
	- Airflow만큼의 레퍼런스는 적음
	- 대규모 조직 표준으로 드묾

> ML 엔지니어가 쓰기 좋은 Airflow 대안

___

# Dagster
## 정체성
- 데이터/ML 파이프라인을 "asset" 중심으로 관리하는 프레임워크

## 핵심 기능
- Asset 기반 설계
- 타입/메타데이터 검증
- 테스트 친화적
- 재사용성 높은 파이프라인

## 사용처
- 복잡한 데이터/ML 파이프라인
- 유지보수성 최우선
- 장기 프로젝트


## 장/단점
- 장점
	- 구조적 / 안정적
	- 파이프라인 품질 관리에 최강
	- ML + 데이터 통합에 좋음
- 단점
	- 러닝커브 있음
	- 초기 설계 부담

> '파이프라인'을 '시스템'처럼 관리하고 싶을 때



# 요약
|도구|핵심 역할|주 사용 대상|
|---|---|---|
|MLflow|실험 기록/모델 관리|ML Engineer|
|W&B|실험 시각화/협업|연구/딥러닝 팀|
|Airflow|배치 ETL|데이터 엔지니어|
|Prefect|유연한 ML 파이프라인|ML Engineer|
|Dagster|구조적 파이프라인|ML/DE 혼합팀|

### ✅ 개인/소규모 팀
- **W&B + Prefect**
    
### ✅ 서비스형 ML
- **MLflow + Prefect**
- **MLflow + Dagster**
    
### ✅ 대규모 조직
- **Airflow + MLflow**
- **Dagster + MLflow**


- MLflow / W&B > 모델 관리
- Airflow / Prefect / Dagster > 흐름 관리


___

# ETC

|유형|추천 도구|이유|
|---|---|---|
|전통 ML|**MLflow**|가볍고 재현성 중심|
|DL (CV/NLP)|**W&B**|시각화·비교 최강|
|LLM Fine-tuning|**W&B**|실험 추적 필수|
|POC / 개인|W&B|즉각적 피드백|
|보안 민감|MLflow|온프레미스 가능|
