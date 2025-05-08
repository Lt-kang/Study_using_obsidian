# Installation

## Install FastMCP
우리는 FastMCP 설치 및 관리에 대해서 [uv](https://docs.astral.sh/uv/getting-started/installation/)를 추천하고 있습니다.

만약 당신의 프로젝트에서 FastMCP를 사용할 계획이라면, 당신은 아래 명령어로 의존성 패키지를 설치할 수 있습니다.
```
uv add fastmcp
```

그 외에도 `pip` 혹은 `uv pip`를 통해 설치할 수 있습니다.
#### uv
```
uv pip install fastmcp
```
#### pip
```
pip install fastmcp
```


### Verify Installation
FastMCP가 정상적으로 설치되었는지 검증이 필요하다면,
아래 커맨드를 입력하여 확인할 수 있습니다.
```
fastmcp version
```
정상적으로 설치되었다면 아래와 같은 내용이 출력됩니다.
```
$ fastmcp version

FastMCP version:   0.4.2.dev41+ga077727.d20250410
MCP version:                                1.6.0
Python version:                            3.12.2
Platform:            macOS-15.3.1-arm64-arm-64bit
FastMCP root path:            ~/Developer/fastmcp
```

### Installing for Development
FastMCP에 코드를 기여하실 계획이 있다면, repository를 복사하고 `uv`를 사용하여 모든 의존성 패키지를 설치하세요.
```
git clone https://github.com/jlowin/fastmcp.git
cd fastmcp
uv sync
```

test 코드를 실행해보시려면 pytest를 사용하세요.
```
pytest
```


# 요약

### pip 로 설치
```
pip install fastmcp
```
### uv로 설치
```
uv pip install fastmcp
```



