# 1. Airflow란?
- python ETL 자동화 프레임워크
- Workflow as Code
	- Trigger -> Workflow -> issue control -> done


# 2. 핵심 개념 정리
## 2.1 DAG(Directed Acyclic Graph)
- DAG = Task 들의 방향성을 이어주는 비순환 그래프
	- "어떤 작업이 어떤 작업 뒤에 실행되는가" 정의

## 2.2 Task
- DAG 안에서 실행되는 하나의 작업 단위
- Task
	- python code
	- bash command
	- docker container
	- spark job
- ex) 데이터 수집 / 파일 이동 / 모델 학습 / api 호출

## 2.3 Operator
- Operator = Task의 실행 방식
	- `PythonOperator` – Python 함수 실행
	- `BashOperator` – shell command 실행
	- `DockerOperator` – Docker 컨테이너 실행
	- `KubernetesPodOperator` – K8s pod 실행
	- `BranchPythonOperator` – 조건 분기
	- `ShortCircuitOperator` – 조건부 중단

## 2.4 Scheduler / Executor
- Scheduler
	- DAG를 언제 실행할지 결정

- Executor
	- Task를 실제로 어디서 실행할지 결정

- Executor 종류
	- `SequentialExecutor` (개발용)
	- `LocalExecutor`
	- `CeleryExecutor`
	- `KubernetesExecutor`

## 2.5 Web UI
- Airflow의 강력한 장점 중 하나
	- DAG 상태 시각화
	- Task 성공/실패 확인
	- log 확인
	- Retry / Clear
	- 과거 실행 이력 관리