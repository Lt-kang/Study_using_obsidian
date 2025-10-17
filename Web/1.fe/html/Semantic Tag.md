
# Semantic Tag를 사용하는 이유
- 가독성 향상
- SEO 최적화(검색엔진이 문서 구조를 이해하고 랭킹 반영)
- 접근성 향상(스크린 리더가 각 영역을 의미적으로 구분 가능)
- 유지보수성 향상


# Semantic Tag 종류
- header
- nav
- main
- article
- section
- aside
- footer
- figure & figcaption
- mark
- time


# header
- 문서나 섹션의 머리글
	- 로고 / 사이트 제목 / 네비게이션 메뉴 / 검색창 등
```
<header>
  <h1>My Portfolio</h1>
  <nav>
    <ul>
      <li><a href="#about">About</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
</header>
```


# nav
- 네비게이션 링크 모음
	- 사이트의 주요 이동 경로
```
<nav>
  <a href="/home">Home</a>
  <a href="/blog">Blog</a>
  <a href="/contact">Contact</a>
</nav>
```


# main
- 문서의 핵심 콘텐츠
	- 한 문서 안에 하나만 존재해야 함

```
<main>
  <article>
    <h2>오늘의 뉴스</h2>
    <p>HTML5가 드디어 정식으로 채택되었습니다.</p>
  </article>
</main>
```


# article
- 독립적으로 재사용 가능한 콘텐츠 블록
	- 블로그 글 / 뉴스 기사 / 사용자 리뷰 / 포럼

```
<article>
  <h2>HTML5의 장점</h2>
  <p>HTML5는 구조적 의미를 강화하고, 멀티미디어를 쉽게 다룰 수 있게 합니다.</p>
</article>
```


# section
- 문서의 논리적 구획(주제 단위 섹션)
	- `<article>`은 독립적 컨텐츠
	- `<section>`은 하나의 주제 아래 묶인 부분
```
<section>
  <h2>Frontend Skills</h2>
  <p>HTML, CSS, JavaScript</p>
</section>
```


# aside
- 보조 콘텐츠 영역
	- 광고 / 관련 링크 / 사이드바 / 인용문

```
<aside>
  <h3>추천 글</h3>
  <ul>
    <li><a href="#">HTML5 입문</a></li>
    <li><a href="#">CSS Flexbox 완벽 정리</a></li>
  </ul>
</aside>
```


# footer
- 문서나 섹션의 하단 영역
	- 저작권 / 연락처 / 사이트 정보 / SNS 링크

```
<footer>
  <p>© 2025 Kang Seunghyun. All rights reserved.</p>
</footer>
```

# figure & figcaption
- 이미지 / 다이어그램 / 코드 블록 등의 묶음
	- `<figcaption>`: 해당 콘텐츠의 설명(캡션) 추가
```
<figure>
  <img src="diagram.png" alt="시스템 아키텍처 다이어그램">
  <figcaption>그림 1. 전체 시스템 구조</figcaption>
</figure>
```


# mark
- 강조 표시(형광펜 효과)

```
<p>이 문장에서 <mark>중요한 부분</mark>을 강조합니다.</p>
```


# time
- 시간 / 날짜 정보 명시
- SEO/기계 판독성 향상에 도움
```
<time datetime="2025-10-15">2025년 10월 15일</time>
```


# html Semantic Tag example
```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HTML5 Semantic Tag 예제</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background: #f8f9fa;
      line-height: 1.6;
    }
    header, nav, main, article, section, aside, footer {
      padding: 1rem;
      margin: 1rem;
      border-radius: 10px;
    }
    header { background: #0077cc; color: white; }
    nav { background: #cce5ff; }
    main { background: white; }
    article { background: #f1f1f1; }
    section { background: #fafafa; }
    aside { background: #fff3cd; }
    footer { background: #343a40; color: white; text-align: center; }
    figure { margin: 0; text-align: center; }
    figcaption { font-style: italic; color: gray; }
    mark { background-color: yellow; }
  </style>
</head>
<body>

  <!-- header: 사이트 상단 정보 -->
  <header>
    <h1>HTML5 시맨틱 태그 학습 페이지</h1>
    <nav>
      <a href="#intro">소개</a> |
      <a href="#articles">글 모음</a> |
      <a href="#contact">연락처</a>
    </nav>
  </header>

  <!-- main: 주요 콘텐츠 -->
  <main>

    <!-- article: 독립적인 글 하나 -->
    <article id="intro">
      <header>
        <h2>HTML5란 무엇인가?</h2>
        <p>작성일: <time datetime="2025-10-15">2025년 10월 15일</time></p>
      </header>

      <section>
        <h3>1. 시맨틱 구조의 중요성</h3>
        <p>
          HTML5에서는 <mark>시맨틱 태그</mark>를 사용하여 문서 구조를 명확히 표현합니다.
          이는 검색엔진 최적화(SEO)와 접근성 향상에 큰 도움이 됩니다.
        </p>
      </section>

      <section>
        <h3>2. 시맨틱 태그의 예시</h3>
        <figure>
          <img src="semantic-structure.png" alt="HTML5 시맨틱 구조 예시" width="400" />
          <figcaption>그림 1. 시맨틱 태그를 활용한 웹페이지 구조 예시</figcaption>
        </figure>
      </section>
    </article>

    <!-- article 2 -->
    <article id="articles">
      <header>
        <h2>시맨틱 태그의 종류</h2>
      </header>
      <section>
        <ul>
          <li><strong>&lt;header&gt;</strong>: 머리글 영역</li>
          <li><strong>&lt;nav&gt;</strong>: 내비게이션</li>
          <li><strong>&lt;main&gt;</strong>: 주요 콘텐츠</li>
          <li><strong>&lt;article&gt;</strong>: 독립된 콘텐츠</li>
          <li><strong>&lt;section&gt;</strong>: 주제 단위 구획</li>
          <li><strong>&lt;aside&gt;</strong>: 보조 정보</li>
          <li><strong>&lt;footer&gt;</strong>: 바닥글</li>
          <li><strong>&lt;figure&gt;</strong> &amp; <strong>&lt;figcaption&gt;</strong>: 시각 자료</li>
          <li><strong>&lt;mark&gt;</strong>: 강조</li>
          <li><strong>&lt;time&gt;</strong>: 날짜/시간 표시</li>
        </ul>
      </section>
    </article>

    <!-- aside: 보조 콘텐츠 -->
    <aside>
      <h3>참고 자료</h3>
      <ul>
        <li><a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element">MDN HTML 요소 문서</a></li>
        <li><a href="https://www.w3schools.com/html/html5_semantic_elements.asp">W3Schools Semantic Elements</a></li>
      </ul>
      <p><mark>TIP:</mark> 브라우저의 개발자 도구(F12)를 열고 요소 구조를 확인해보세요!</p>
    </aside>

  </main>

  <!-- footer: 페이지 하단 -->
  <footer id="contact">
    <p>© <time datetime="2025">2025</time> Kang Seunghyun. All Rights Reserved.</p>
    <p>이메일: <a href="mailto:example@email.com">example@email.com</a></p>
  </footer>

</body>
</html>
```