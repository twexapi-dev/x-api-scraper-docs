# TwexAPI docs

> TwexAPI is an independent third-party service. Not affiliated with X Corp.
> "Twitter" and "X" are trademarks of X Corp.

Documentation for [TwexAPI](https://twexapi.io), an X (Twitter) Scraper API and X API alternative. Intended for **[docs.twexapi.io](https://docs.twexapi.io)**.

This repository covers REST, MCP, SDKs, CLI, Terraform, n8n, Prefect, and Apify. The OpenAPI contract currently documents **66** operations.

## Start here

- [Quickstart](https://docs.twexapi.io/x-api-quickstart)
- [API overview](https://docs.twexapi.io/api-reference/overview)
- [Authentication](https://docs.twexapi.io/api-reference/authentication)
- [MCP](https://docs.twexapi.io/mcp/overview)
- [SDKs](https://docs.twexapi.io/sdks)
- [OpenAPI](https://github.com/twexapi-dev/x-api-scraper-docs/blob/main/openapi.json)

## Local preview

```bash
npx mintlify@latest dev
```

Regenerate API pages after updating `openapi.json`:

```bash
python3 scripts/generate-api-pages.py
```

## Related repositories

- [Skill and MCP catalog](https://github.com/twexapi-dev/x-api-scraper)
- [TypeScript SDK](https://github.com/twexapi-dev/x-api-scraper-typescript)
- [n8n node](https://github.com/twexapi-dev/n8n-nodes-x-api-scraper)
- [Prefect collection](https://github.com/twexapi-dev/prefect-x-api-scraper)

## License

MIT. The license does not cover the TwexAPI product, brand, or platform.
