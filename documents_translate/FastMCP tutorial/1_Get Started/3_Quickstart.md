# Quickstart

반갑습니다. 해당 가이드는 당신이 빠르게 FastMCP를 설치하고 
당신이 만든 MCP server를 실행하도록 도와줄겁니다.


## Creating a FastMCP Server
FastMCP 서버는 `tools`, `resources`, `MCP components`의 집합 입니다.
서버를 생성하기 위해, FastMCP 클래스를 생성해보세요.

`my_server.py` 파일을 생성하고 해당 파일에 아래의 코드를 입력하세요.
#### my_server.py
```
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")
```
이로써 여러분은 FastMCP 서버를 만든겁니다.
이제부터 Tool을 더 추가해보도록 하겠습니다.

## Adding a Tool

간단한 인사를 반환해주는 tool을 추가하기 위해,
함수를 작성하고 서버에 tool을 등록하기 위해 `@mcp.tool` 데코레이터를 사용하도록 하겠습니다.

#### my_server.py
```
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"
```


## Testing the Server

서버를 test해보기 위해, FastMCP client를 생성하고 서버 객체를 지정해보겠습니다.

#### my_server.py
```
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

client = Client(mcp)

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))
```

몇 가지를 명심해주세요.
- client는 **비동기 방식**이므로 `asyncio.run`으로 실행해야 합니다.
-  client를 사용하기 전에 반드시 `async with client:` 문구로 선언해야 합니다. 하나의 문구 안에서 여러 번 클라이언트 호출을 수행할 수 있습니다.


## Running the server
Python을 통해 서버를 실행하기 위해, `run` 상태와 `__main__`블럭을 서버파일에 추가해야합니다.

#### my_server.py
```
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```
이렇게 하면 `python my_server.py` 명령어를 통해 서버를 실행할 수 있으며,
기본 전송 방식인 `stdio`을 사용하게 됩니다.
이는 MCP 서버를 client에 제공하는 표준적인 방법 입니다.


> 어째서 `if __name__ == "__main__"` 블럭을 사용해야하나요? <br> 
FastMCP 생태계에서는 위와 같은 블럭은 불필요 합니다. 
그러나 이러한 코드를 포함하면 모든 사용자와 client 환경에서 서버가 일관되게 실행되도록 
보장할 수 있기 때문에 이와 같은 방법을 권장합니다.


### Interacting with the Python server

이제 `ptyhon my_server.py` 명령어로 서버를 실행할 수 있으므로 
다른 MCP 서버와 마찬가지로 해당 서버와 상호작용이 가능합니다.

새로운 파일에 client를 생성하고 server 파일을 지정하세요.
#### my_client.py
```
from fastmcp import Client

client = Client("my_server.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))
```


### Using the FastMCP CLI

FastMCP에게 직접 서버를 실행하도록 하고 싶다면 `fastmcp run` 커맨드를 사용해보세요.
이는 서버를 실행하며 실행한 상태를 유지합니다.
기본적으로 전송 방식은 `stdio`를 사용합니다.
이는 서버와 상호작용하기 위한 간단한 text 기반 protocol 입니다.

```
fastmcp run my_server.py:mcp
```

명심하세요.
FastMCP는 서버파일에 `__main__` 블럭이 필수는 아니며 있더라도 이를 무시합니다.
대신, 서버 객체를 CLI 커맨드로 지정해야합니다.(위 예시에서 `mcp`가 관련된 부분 입니다.)
만약 객체명을 지정하지 않았다면 `fastmcp run`은 파일에서 `mcp`, `app`, `server` 라는 객체명을 
자동으로 탐색합니다.

>우리는 client를 server file에 연결하였고, 이는 Python MCP 서버로 인식됩니다. 또한 `python my_server.py` 명령어로 실행됩니다. 기본적으로 실행시 서버 파일의 `__main__`이 실행됩니다. 또 다른 실행 방법으로는  [서버 설정 가이드](https://gofastmcp.com/servers/fastmcp#running-the-server)를 참고하세요.


