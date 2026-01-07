# 템플릿(Template)란?
HTML 문서의 기본 틀
jinja2를 사용하면 고정된 레이아웃 구조 내 특정 부분에 대해서
동적으로 데이터를 삽입할 수 있음.

___

# 템플릿의 역할
* 반복되는 구조를 효율적으로 관리
* 동적 데이터 삽입
	* 고정된 html 대신 python 코드에서 전달된 데이터를 템플릿에 삽입하여 동적 컨텐츠 생성
* 코드와 디자인 분리
	* 템플릿 파일은 html/css로 구성되고, 실제 데이터는 python 코드에서 제공되므로 개발자와 디자이너가 역할을 분리하여 작업할 수 있음.

___

# 템플릿의 구성 요소
* 일반적인 html 코드와 함께 변수, 조건문, 반복문 등을 포함할 수 있음.

## 변수 삽입
* `{{ 변수명 }}`
	* ```<p>Welcome, {{ user_name }}!</p>```

## 제어 구조
* 반복문
```
<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

* 조건문
```
<p>
    {% if user.is_authenticated %}
        Hello, {{ user.name }}!
    {% else %}
        Please log in.
    {% endif %}
</p>
```

* 주석
```
{# 주석 내용 #}
```

* 매크로
```
{% macro macro_name(param1, param2) %}
    <!-- 반복적으로 사용할 HTML 코드 -->
{% endmacro %}
```

* include와 extends
	* [[(작성중)jinja2_include_extends]]

## 예시 코드

```
<!DOCTYPE html>
<html>
<head>
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>Hello, {{ user_name }}!</h1>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```


___


# 템플릿 파일 동작 과정

1. 클라이언트가 서버에 요청을 보냄
2. 서버(fast api)가 필요한 데이터를 준비함
3. 준비된 데이터를 템플릿에 삽입하여 최종 html을 생성
4. 생성된 html을 클라이언트에게 반환


## python 코드를 통한 템플릿 사용 예시코드

### app.py

```
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
	data = {
		"request": request,
		"page_title": "My Page",
		"user_name": "Alice",
		"items": ["Apple", "Banana", "Cherry"]
	}
	return templates.TemplateResponse("example.html", data)

```

### example.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Jinja2 Control Structures</title>
</head>
<body>
    <h1>Users List</h1>
    {% if users %}
        <ul>
            {% for user in users %}
                <li>{{ user.name }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No users found.</p>
    {% endif %}
</body>
</html>
```