# Module 13 Completion Report

## MCP Configuration
```json
{ 
  "servers": { 
    "echo-windows": { 
      "command": "powershell", 
      "args": ["-ExecutionPolicy", "Bypass", "-File", "./path/to/mcp-echo.ps1"] 
    }  
  }  
}  
```

## Configured Servers
- echo-windows

## MCP Tool Test
- Tool used: mcp_pylance_mcp_s_pylanceWorkspaceRoots
- Output:
```text
Available Workspace roots: file:///Users/Kalyan_Navpute/hello-genai
```