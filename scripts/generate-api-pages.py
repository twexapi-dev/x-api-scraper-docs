#!/usr/bin/env python3
"""Generate thin Mintlify API pages from the TwexAPI OpenAPI document."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPENAPI = json.loads((ROOT / "openapi.json").read_text())
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}

COOKIE_OPERATION_IDS = {
    "tweetsActionsLike",
    "tweetsActionsUnlike",
    "tweetsActionsRetweet",
    "tweetsActionsUnretweet",
    "tweetsActionsCreateThread",
    "tweetsActionsCreate",
    "tweetsActionsQuote",
    "tweetsActionsCreateWithoutCookie",
    "tweetsActionsBookmark",
    "tweetsActionsUnbookmark",
    "tweetsActionsDeleteBatch",
    "usersFollow",
    "usersUnfollow",
    "dmStatus",
    "dmSend",
    "dmHistory",
    "dmMedia",
    "dmConversations",
}


def kebab(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", value)
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value)
    return value.strip("-").lower()


def main() -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)

    for path, item in OPENAPI["paths"].items():
        for method, operation in item.items():
            if method not in HTTP_METHODS:
                continue
            tag = (operation.get("tags") or ["Other"])[0]
            operation_id = operation["operationId"]
            title = operation.get("summary") or operation_id
            folder = kebab(tag)
            filename = kebab(operation_id)
            rel = f"api-reference/{folder}/{filename}"
            dest = ROOT / f"{rel}.mdx"
            dest.parent.mkdir(parents=True, exist_ok=True)

            lines = [
                "---",
                f'title: "{title}"',
                f"openapi: {method.upper()} {path}",
            ]
            description = (operation.get("description") or title).split("\n")[0].strip()
            if description:
                lines.append(f'description: "{description.replace(chr(34), chr(39))}"')
            lines.append("---")
            lines.append("")
            if operation_id in COOKIE_OPERATION_IDS:
                lines.extend(
                    [
                        "<Warning>",
                        "This route needs a Twitter cookie or `auth_token` in addition to the TwexAPI API key.",
                        "Never send an X password or 2FA code.",
                        "</Warning>",
                        "",
                    ]
                )
            dest.write_text("\n".join(lines), encoding="utf-8")
            grouped[tag].append({"title": title, "page": rel})

    nav = []
    for tag in [t["name"] for t in OPENAPI.get("tags", [])]:
        pages = grouped.get(tag)
        if not pages:
            continue
        nav.append(
            {
                "group": tag,
                "pages": [item["page"] for item in pages],
            }
        )
    (ROOT / "scripts" / "api-navigation.json").write_text(
        json.dumps(nav, indent=2) + "\n",
        encoding="utf-8",
    )

    docs_path = ROOT / "docs.json"
    docs = json.loads(docs_path.read_text())
    for tab in docs["navigation"]["tabs"]:
        if tab.get("tab") == "API reference":
            tab["groups"] = [{"group": "Overview", "pages": ["api-reference/overview"]}] + nav
    docs_path.write_text(json.dumps(docs, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {sum(len(v) for v in grouped.values())} API pages")


if __name__ == "__main__":
    main()
