useTransition
useDeferredValue

BrowserRouter/HashRouter/Nested Routing

Link와 NavLink의 차이

useParams

Styled-components


SPA
SEO
SaaS
MVP
MSA
SSR/SSG
마이크로서비스 설계 패턴
웹소켓
ES6
tRPC
Master Slave
db 이중화
로드밸런서
게이트웨이
메시징 시스템
캐싱
Nginx
CDN



좋아요 👍  
"FE(Frontend) / BE(Backend) / FE+BE 공통(Infra 포함)" 세 영역으로 나누어  
**웹의 기본기를 완전히 익히기 위한 모든 핵심 개념 및 키워드 맵**을 구조적으로 정리해드릴게요.  
중복 포함 — 즉, 양쪽에서 동시에 중요한 개념은 **FE+BE 공통 영역**에도 다시 명시했습니다.

---

## 🧩 FE (Frontend)

### 1. 브라우저 동작 원리

- **주요 키워드**
    
    - Rendering Engine, DOM, CSSOM, Render Tree
        
    - Reflow, Repaint, Event Loop, Call Stack
        
    - Critical Rendering Path
        
    - Web API, JavaScript Engine(V8), Execution Context
        

### 2. HTML / CSS / JavaScript 기본

- **주요 키워드**
    
    - HTML5 Semantic Tag (`<header>`, `<main>`, `<section>`)
        
    - CSS Flexbox / Grid / Position / Media Query
        
    - JavaScript ES6+ 문법, Arrow Function, Destructuring, Promise, Async/Await
        

### 3. 브라우저 이벤트 & DOM 조작

- **주요 키워드**
    
    - Event Bubbling / Capturing
        
    - addEventListener, preventDefault, stopPropagation
        
    - querySelector, innerHTML, classList
        

### 4. 상태 관리 및 렌더링 로직

- **주요 키워드**
    
    - React (useState, useEffect, props, component lifecycle)
        
    - Virtual DOM
        
    - 상태 관리: Context API, Redux, Zustand, Recoil
        
    - 컴포넌트 분리, Props drilling, Memoization
        

### 5. 비동기 통신

- **주요 키워드**
    
    - Fetch API, Axios
        
    - REST API, JSON
        
    - CORS, Preflight, Same-Origin Policy
        

### 6. UI 프레임워크 / 라이브러리

- **주요 키워드**
    
    - React, Next.js, Vue.js, Svelte
        
    - Tailwind CSS, MUI, Styled Components
        

### 7. 빌드 & 배포

- **주요 키워드**
    
    - Vite, Webpack, Babel, ESLint
        
    - CSR / SSR / SSG / ISR (Next.js)
        
    - Bundle, Tree-shaking, Lazy Loading
        

---

## ⚙️ BE (Backend)

### 1. 서버 기본 개념

- **주요 키워드**
    
    - Client-Server Model
        
    - HTTP / HTTPS / TCP / UDP
        
    - Port, Socket, DNS, Proxy, Load Balancer
        
    - API Server, Web Server, Application Server
        

### 2. 웹 프로토콜

- **주요 키워드**
    
    - HTTP Method (GET, POST, PUT, DELETE)
        
    - Status Code (200, 201, 400, 401, 403, 404, 500)
        
    - Header, Cookie, Session, JWT
        
    - RESTful API, GraphQL
        

### 3. 서버 개발

- **주요 키워드**
    
    - FastAPI, Flask, Django, Express.js, Node.js
        
    - Router, Middleware, Request/Response
        
    - ORM (SQLAlchemy, Prisma, Sequelize)
        
    - MVC / MVT 아키텍처
        

### 4. 데이터베이스

- **주요 키워드**
    
    - SQL vs NoSQL
        
    - MySQL, PostgreSQL, SQLite, MongoDB
        
    - Index, Transaction, Join, Normalization
        
    - CRUD, Schema Design, ERD
        

### 5. 인증 / 보안

- **주요 키워드**
    
    - JWT, OAuth 2.0, Refresh Token
        
    - Password Hashing (bcrypt)
        
    - CSRF, XSS, SQL Injection 방지
        
    - HTTPS / SSL / TLS
        

### 6. 서버 배포 및 운영

- **주요 키워드**
    
    - Gunicorn, Uvicorn, Nginx, Reverse Proxy
        
    - Docker, Docker Compose
        
    - CI/CD (GitHub Actions, Jenkins)
        
    - 환경 변수 관리 (.env, dotenv)
        

---

## 🌐 FE + BE 공통 (Infra / DevOps / Web 전체 흐름)

### 1. 웹 아키텍처 이해

- **주요 키워드**
    
    - Request → Response Cycle
        
    - API Gateway
        
    - CDN (Cloudflare, Akamai)
        
    - Load Balancer, Reverse Proxy
        
    - Microservice vs Monolith
        

### 2. 네트워크 및 통신

- **주요 키워드**
    
    - DNS, IP, MAC Address
        
    - HTTP vs WebSocket
        
    - REST vs GraphQL vs gRPC
        
    - CORS, Proxy 설정
        
    - Rate Limiting, API Key
        

### 3. 인증/인가 흐름

- **주요 키워드**
    
    - Cookie, Session, Token 기반 인증
        
    - OAuth2, OpenID Connect
        
    - SSO (Single Sign-On)
        

### 4. 배포 / 인프라 / 클라우드

- **주요 키워드**
    
    - Docker, Dockerfile, Image, Container
        
    - Kubernetes (Pod, Deployment, Service)
        
    - AWS / GCP / Azure
        
    - CI/CD, GitHub Actions, Pipeline
        
    - Vercel (FE), Render / EC2 (BE)
        

### 5. 성능 / 최적화

- **주요 키워드**
    
    - Caching (Redis, CDN, Browser Cache)
        
    - Lazy Loading, Code Splitting
        
    - DB Indexing, Query Optimization
        
    - Logging / Monitoring (Prometheus, Grafana)
        

### 6. 보안 및 운영

- **주요 키워드**
    
    - HTTPS / SSL 인증서
        
    - CORS 정책
        
    - CSP (Content Security Policy)
        
    - Secret Management (Vault, .env)
        
    - 로깅 / 에러 핸들링
        

---

## 🧱 한눈에 보는 구조 요약

|구분|핵심 주제|예시 키워드|
|---|---|---|
|**FE**|브라우저 렌더링 / UI / 비동기 통신|React, DOM, Axios, CSR/SSR|
|**BE**|서버 / DB / 인증 / API 설계|FastAPI, SQLAlchemy, REST, JWT|
|**FE+BE**|네트워크 / 배포 / 보안 / DevOps|Docker, CI/CD, Nginx, HTTPS|

---

원하신다면 다음 단계로 **“학습 로드맵”** 형태로 정리해드릴 수도 있습니다.  
예를 들어:

> 1단계: 브라우저와 HTTP 이해 →  
> 2단계: HTML/CSS/JS →  
> 3단계: React →  
> 4단계: FastAPI + DB →  
> 5단계: Docker + 배포

이렇게 “학습 순서 + 추천 자료”까지 구성해드릴까요?