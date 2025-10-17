- SPA 자체가 본질적으로 불안한 게 아니라, 
  개발자가 클라이언트에서만 보안 결정을 내리고(중요 검사들을 클라이언트에만 맡기고)
  그 결과 발생하는 실수/오해에서 문제가 생김.


# 구체적인 공격 시나리오
1. 클라이언트에서만 접근 제어를 하면 우회당함
	- Client router가 `if (user.role !== 'admin') redirect()`와 같은 검사만 한다면, 공격자는 브라우저 개발자 도구나 직접 API 호출로 우회 가능

2. 민감한 정보가 번들에 포함될 수 있음(노출 위험)
	- API 키 / 시크릿 / 내부 URL 등
	  JS 소스 번들이나 설정에 하드코딩하면 누구나 번들 분석으로 추출 가능.
	  **(클라이언트 코드는 공개자원임.)**

3. 클라이언트 js는 변조/재생이 쉬움
	- 요청을 변조하거나 악의적 스크립트를 주입해 동작을 바꿀 수 있음.
	  (브라우저 확장, 프록시, mitm 등 HTTPS로 대부분 막지만 로컬 변조는 가능)

4.  XSS(교차 사이트 스크립팅) 위험
	-  SPA는 JS를 많이 사용하므로 `innerHTML`, `dangerouslySetInnerHTML` 등으로 동적 HTML을 삽입하면 XSS에 취약.
	- 공격자는 토큰/쿠키/세션 정보를 탈취 가능

5.  인증 토큰 보관 방식 문제
	- `localStorage`에 토큰을 넣어두면 XSS로 쉽게 탈취됨. Cookie도 잘못 구성하면 CSRF 대상이 될 수 있음.

6. 보안 오해(보안 through obscurity)
	- Route가 보이지 않으니 안전하겠지 라는 믿음 
	  -> 실제로는 보이지 않는 경로를 통해 접근 가능.


# 방어책 체크리스트

1. 서버에서 항상 권한 검사(Authorization/Authentication)
	- 모든 민감 API는 매 요청마다 토큰/세션을 검증하고 권한을 확인해야 함.
	  client 검사는 보조역할

2. 비밀값 or API KEY는 절대 Client에 넣지 않기
	- 클라이언트가 접근할 필요가 있는 키는 최소 권한의 퍼블릭 키여야 하며, 
	  민감한 키는 서버에서만 사용

3. 토큰 저장: 가능한 경우 `HttpOnly`, `Secure`, `SameSite` 쿠기 사용
	1. localStorage 대신 서버 발행의 HttpOnly 쿠키로 인증하면 XSS로부터 토큰 탈취 위험 낮춤. (단, CSRF 대비 필요)

4. CSRF 대응
	1. 쿠키 인증을 쓰면 CSRF 토큰, SameSite 설정, double submit cookie 등을 적용.

5. 모든 입력은 server/client에서 검증(validation + sanitization)
	1. server가 최종 방어선: 길이, 타입, 허용값 검사, SQL/명렁어 주입 방지 등.

6. XSS 방지
	1. 출력 시 이스케이프, 사용자 제공 HTML은 신뢰할 수 있는 sanitizer(ex. DOMPurity)로 정제
	   가능한 `dangerouslySetInnerHTML` 사용 지양

7. CSP(Content Security Policy) 설정
	1. 인라인 스크립트 금지
	   신뢰된 출처만 허용으로 XSS 피해 축소

8. CORS 정책 최소화
	1. 허용 출처를 최소로, 자격증명 필요 시 명시적으로 설정.

9. HTTPS 강제 및 HSTS 사용
	1. 중간자 공격 방지

10. Rate limiting / ip 방어 / 인증 실패 모니터링
	1. api 남용 방지 및 브루트포스 차단

11. 번들 산출물(프로덕션)에서 소스맵 관리
	1. 프로덕션에 자세한 소스맵/디버그 정보 노출 금지(또는 접근 제한)

12. 의존성/라이브러리 보안 스캔
	1. 취약한 패키지 사용 금지 및 정기적 업데이트



# 실무 팁

- 실수: 클라이언트 라우팅으로 "관리자 화면 숨기기" → 서버는 권한 체크 없음.  
- 권장: 모든 관리자 API는 서버에서 사용자 권한을 확인하고, UI는 단지 UX용 보조.
    
- 실수: 인증 토큰을 localStorage에 보관 → XSS로 탈취 가능.  
- 권장: 가능한 경우 HttpOnly 쿠키 + CSRF 방어.
    
- 실수: 사용자 입력을 HTML에 직접 삽입.  
- 권장: sanitize/escape, CSP 적용.
    
- **보안은 다층 방어**(defense in depth). 
  클라이언트 검사(빠른 UX용)는 유지하되 **서버 검증을 반드시 1차 방어선**으로 삼기.

# 결론

- client routing/rendering 자체가 보안 취약을 만드는 것은 아니나
  client에만 의존하는 보안 로직은 쉽게 우회/노출 될 수 있음
- client는 UX/표시용 검사만 하고, 결정적 판단은 서버에서 함