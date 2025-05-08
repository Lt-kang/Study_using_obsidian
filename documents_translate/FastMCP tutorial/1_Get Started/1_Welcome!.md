# Welcome to FastMCP!

FastMCP는 빠르면서도 Pythonic한 방법으로 MCP servers와 clients를 구축하는 방법입니다.

[Model Context Protocol](https://modelcontextprotocol.io/introduction)은 여러분의 LLM에게 맥락(context)와 도구(tools)를 표준화된 방법으로 제공하는 새로운 방법 입니다.
또한 FastMCP는 MCP servers와 clients 구축을 쉬우면서도 직관적으로 만들도록 도와줍니다.
tools를 만드시고, 이를 활용할 수 있도록 공개하며, prompts를 정의하고, 더 깔끔하고 Pythonic한 코드를 만드세요!


```
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```


## What is MCP?
Model Context Protocol은 LLM 애플리케이션이 안전하고 표준화된 방식으로 데이터와 기능에 접근할 수 있도록 지원하는 서버를 쉽게 구축할 수 있게 해줍니다.

MCP는 LLM이 활용할 수 있도록 표준화된 방식으로 데이터를 제공한다는 점에서 `Ai를 위한 USB-C port`로 설명되곤 합니다.
이는 API처럼 여겨질 수 있으나 MCP는 LLM과의 상호작용만을 위해 설계되었습니다.

MCP servers는 아래와 같은 기능이 있습니다.
- `Resources`를 통해 데이터 제공 (이는 GET endpoints와 유사합니다. 이는 정보를 LLM의 context에 불러오는데 사용됩니다.)
- `Tools`를 통해 (LLM이 사용할) 함수 제공 (이는 POST endpoints와 유사합니다. 이는 code를 실행할 때 사용되거나 그 외 무언가를 생성할 때 사용됩니다.)
- `Prompts`를 통해 (LLM과의)  상호작용 정의 (LLM의 상호작용을 위한 재사용 가능한 templates를 의미합니다.)

이는 protocol을 직접적으로 구현할 수 있는 저수준의 Python SDK도 제공되지만
고수준 Pythonic interface를 제공함으로써 protocol 구축을 보다 쉽게 만들도록 하는 것이 목표 입니다.

> FastMCP 1.0 was so successful that it is now included as part of the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)!


## Why FastMCP?

MCP는 강력하지만 구현을 위해서는 반복적인 boilerplate(server setup, protocol handlers, context types, error management)가 많이 필요합니다.
- *형식 코드*: boilerplate
FastMCP는 모든 복잡한 protocol의 세부사항과 server management를 대신 처리해주기 때문에
여러분은 훌륭한 tools 구축에만 집중할 수 있습니다.
FastMCP는 Pythonic과 고수준 인터페이스로 제작되었으며
대부분의 경우 함수에 데코레이터를 적용하는 것만으로 충분합니다.

FastMCP는 아래의 내용을 목표로 합니다.

🚀 **Fast**: 고수준 인터페이스는 곧 적은 코드와 빠른 개발을 의미합니다.

🍀 **Simple**: 적은 boilerplate로 MCP servers를 구축합니다.

🐍 **Pythonic**: python 개발자들에게 친화적입니다.

🔍 **Complete**: FastMCP MCP의 핵심 사양을 완전히 구현하는 것을 목표로 합니다.

**FastMCP v1**은 MCP 서버 기능을 외부에 노출할 때 발생하는 가장 일반적인 boilerplate를 추상화하는 데 중점을 두었으며, 현재는 공식 MCP Python SDK에 포함되어 있습니다.
**FastMCP v2**은 위 내용에서 더 확장하여 서버와의 상호작용을 더욱 단순화하는 새로운 기능들을 도입합니다.
- flexible clients
- proxying
- composition
- deployment


# 요약
FastMCP는 빠르고 간단한 MCP를 구축하는 Python SDK 이다!
