# SSG(Static Site Generation)
- build 시점에 미리 HTML 파일을 생성해두는 방식.
- 요청이 들어오면 server가 아닌 CDN에서 정적 html을 바로 전달.


# 동작 과정
1. build할 때 API 호출 -> 데이터로 html 파일 생성
2. 배포 시 각 페이지가 미리 만들어짐
3. 사용자가 접근 시 즉시 render(서버 연산 없음)


# 특징
- 장점: 빠름. 서버부하 없음. 보안 좋음
- 단점: 데이터가 변하면 다시 build 해야 함


# 사용처
- 블로그 / 문서 사이트 / 회사 소개 페이지처럼 자주 안 변하는 콘텐츠
- Jamstack 구조(Vercel, Netilify)와 궁합 좋음

