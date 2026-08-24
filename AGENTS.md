# Agent notes

- Source of truth for routes is `openapi.json` (copied from the TypeScript SDK OpenAPI).
- Do not add endpoints that are not in that file.
- Public reads: Bearer API key. Writes/DMs: cookie or `auth_token` plus confirmation.
- MCP: `https://api.twexapi.io/mcp`, tools `explore` and `twexapi_request`.
