# The FastMCP Server

FastMCP 서버의 핵심에 대해 배우고 실행하는 방법을 배웁니다.

FastMCP의 핵심 구성 요소는 `Fast MCP` 서버 클래스 입니다.
이 클래스는 어플리케이션의 tools, resources, prompts를 담는 주요 컨테이너 역할을 하며 MCP client와 함께 통신도 관리합니다.


### Creating a Server

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

FastMCP 서버는 클라이언트와 통신하기 위해 전송 메커니즘이 필요합니다.
MCP 프로토콜 에서는, 서버가 보통 클라이언트와 분리된 독립 프로세스로 실행되며, 클라이언트가 여기에 연결하는 방식으로 동작합니다.

### The `__main__` Block Pattern

서버를 실행하는 표준화된 방법은 `if __name__ == "__main__":` 블럭 내에서 `run()`으로 호출하는 방법 입니다.

#### my_server.py
```
# my_server.py
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This code only runs when the file is executed directly
    
    # Basic run with default settings (stdio transport)
    mcp.run()
    
    # Or with specific transport and parameters
    # mcp.run(transport="sse", host="127.0.0.1", port=9000)
```

이러한 실행 방법이 중요한 이유는 아래와 같습니다.
1. **Client Compatibility**: 표준화된 MCP 클라이언트 (이를 테면 Claude Desktop)는 여러분의 서버 파일을 직접적으로 실행하기를 기대합니다. (`python my_server.py`)
2. **Process Isolation**: 각 서버는 별도의 프로세스에서 실행되므로, 클라이언트는 여러 서버를 독립적으로 관리할 수 있습니다.
3. **Import Safety**: `__main__` 블록은 다른 코드로에서 해당 파일을 import할 때 서버가 실행되는 것을 방지해줍니다. (`__main__` 블록은 스크립트를 직접 실행할 때만 실행되는 블록입니다. 다른 스크립트로부터 import 하는 것으로는 실행되지 않습니다.)

이러한 패턴은 FastMCP의 CLI을 사용할 때는 선택 사항이지만, 모든 MCP 클라이언트와의 최대 호환성을 위해 권장되는 모범 사례로 여겨집니다.


### Transport Options
FastMCP는 2개의 transport 매커니즘을 지원합니다.

### STDIO Transport (Default)

The standard input/output (STDIO) 전송방식은 기본값으로 설정된 방식이며
가장 널리 호환되는 옵션 입니다.
```
# Run with stdio (default)
mcp.run()  # or explicitly: mcp.run(transport="stdio")
```

STDIO 특징
- 클라이언트가 접속을 시도할 때마다 새로운 서버 프로세스를 시작합니다.
- standard input/output streams에 따라 통신이 이루어집니다.
- 클라이언트가 연결을 종료하면 서버 프로세스가 종료됩니다.
- Claude Desktop과 같은 도구와의 통합에 가장 이상적입니다. 이때, 각 대화마다 고유한 서버 인스턴스를 갖습니다.


### SSE Transport (Server-Sent Events)
여러 클라이언트에게 서비스를 제공하기 위한 장시간 서버에 적합한 전송 방식이며
이 또한 역시 FastMCP가 지원하고 있습니다.

```
# Run with SSE on default host/port (0.0.0.0:8000)
mcp.run(transport="sse")
```

SSE 특징
- 지속적으로 실행되는 웹서버의 형태로 동작합니다.
- 여러 클라이언트가 동시에 접속할 수 있습니다.
- 서버를 종료하기 전까지 서버는 계속해서 실행된 상태를 유지합니다.
- 서비스에 원격으로 접근하기에 가장 이상적인 방법입니다.

실행할 서버를 파라미터로 설정할 수 있습니다.
```
# Configure with specific parameters
mcp.run(
    transport="sse", 
    host="127.0.0.1",  # Override default host
    port=8888,         # Override default port
    log_level="debug"  # Set logging level
)

# You can also run asynchronously with the same parameters
import asyncio
asyncio.run(
    mcp.run_sse_async(
        host="127.0.0.1", 
        port=8888, 
        log_level="debug"
    )
)
```

`run()` 또는 `run_sse_async()`에 전달된 **전송(transport) 파라미터**는  
**FastMCP 인스턴스를 생성할 때 정의된 설정값들을 덮어씁니다(우선합니다).**