# The FastMCP Server

FastMCP 서버의 핵심에 대해 배우고 실행하는 방법을 배웁니다.

FastMCP의 핵심 구성 요소는 `Fast MCP` 서버 클래스 입니다.
이 클래스는 어플리케이션의 tools, resources, prompts를 담는 주요 컨테이너 역할을 하며 MCP client와 함께 통신도 관리합니다.

****
## Creating a Server

서버 객체를 만드는 것은 간단한 작업 입니다.
서버의 이름을 지어주세요. 이는 client환경 혹은 logs에서 서버를 식별하기에 유용합니다.
```
from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="MyAssistantServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="This server provides data analysis tools. Call get_average() to analyze numerical data."
)
```
`FastMCP` 구조체는 여러 인자값을 받습니다.
- `name`: (Optional) 사람이 읽을 수 있는 서버명. 기본값은 "FastMCP"
- `instructions`: (Optional) 해당 서버에 대한 기본적인 설명. 이는 clients가 서버의 목적 및 가용 함수 들에 대해 이해할 수 있는 방법 입니다.
- `lifespan`: (Optional) 서버 실행 및 종료에 대한 비동기 context 관리 함수.
- `tags`: (Optional) 서버에 대한 tag
- `**settings`: 추가적인 `ServerSettings` 설정


## Components

FastMCP 서버는 여러 타입의 components를 client에게 제공합니다.

### Tools
클라이언트가 호출하여 사용하거나 외부 시스템에 접근할 수 있는 함수 입니다.
```
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b
```

tools에 대한 자세한 내용은 [Tools](https://gofastmcp.com/servers/tools) 을 확인해주세요.


### Resources
리소스는 클라이언트가 조회할 수 있는 데이터 소스를 외부에서 제공하는 역할을 합니다.
```
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}
```
Resources에 대한 자세한 내용은 [Resources & Templates](https://gofastmcp.com/servers/resources) 을 확인해주세요.


### Resource Templates
리소스 템플릿은 매개변수가 지정된 리소스로, 클라이언트가 특정 데이터를 요청할 수 있도록 해줍니다.
```
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    # The {user_id} in the URI is extracted and passed to this function
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}
```
Resource templates에 대한 자세한 내용은 [Resources & Templates](https://gofastmcp.com/servers/resources) 을 확인해주세요.


### Prompts
프롬프트는 LLM에게 전달되는 재사용 가능한 메세지 탬플릿 입니다.
```
@mcp.prompt()
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"
```
prompts에 대한 자세한 내용은 [Prompts](https://gofastmcp.com/servers/prompts)을 확인해주세요.


## Running the server

FastMCP 서버는 클라이언트와 통신할 전송 메커니즘을 필요로 합니다.
일반적으로 서버를 시작할 때, 메인 서버 script를 `if __name__ == "__main__":` 블록 안에 
FastMCP 객체의 `mcp.run()` 메서드를 호출합니다.
이러한 패턴은 다양한 MCP 클라이언트와의 호환성을 보장합니다.

```
# my_server.py
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()
    
    # To use a different transport, e.g., HTTP:
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=9000)
```

FastMCP는 여러 전송 옵션을 지원합니다.
- **STDIO** (Default, for local tools)
- **Streamable HTTP** (웹 서비스에 추천)
- **SSE** (전통적인 웹 전송 방식. 단, 더 이상 사용되지 않음.)

FastMCP CLI을 활용하여 서버를 실행할 수도 있습니다.

각각의 전송 방식에 대한 자세한 정보(host, port, paths 등의 구성 방법) 그리고 어떤 상황에서 어떤 방식을 사용해야 하는지에 대해서는 [Running Your FastMCP Server](https://gofastmcp.com/deployment/running-server).



## Composing Servers
FastMCP는 `import_server`(정적 복사)와 `mount`(실시간 연결) 기능을 사용해 여러 서버를 함께 조합할 수 있습니다. 
이를 통해 대규모 어플리케이션을 모듈형 컴포넌트로 구성하거나 기존 서버를 재사용 할 수 있습니다.
자세한 내용은 [Server composition](https://gofastmcp.com/servers/composition) 가이드를 확인하세요.

```
# Example: Importing a subserver
from fastmcp import FastMCP
import asyncio

main = FastMCP(name="Main")
sub = FastMCP(name="Sub")

@sub.tool()
def hello(): 
    return "hi"

# Mount directly
main.mount("sub", sub)
```


## Proxying Servers
FastMCP는 `FastMCP.as_proxy`를 사용하여 로컬 혹은 원격의 어떠한 MCP server라도 프록시 역할을 할 수 있습니다.
이를 통해 서로 다른 전송 방식을 연결하거나 기존 서버에 프론트엔드를 추가할 수 있습니다.
예를 들어, 원격 SSE 서버를 로컬에서 stdio로 노출하거나 그 반대로도 할 수 있습니다.

자세한 내용은 [Proxying Servers](https://gofastmcp.com/servers/proxy)을 확인해주세요.
```
from fastmcp import FastMCP, Client

backend = Client("http://example.com/mcp/sse")
proxy = FastMCP.as_proxy(backend, name="ProxyServer")
# Now use the proxy like any FastMCP server
```

## Server Configuration
