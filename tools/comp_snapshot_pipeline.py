"""
Skeleton for Part 7 competitive signals (Timberline Data).

This does NOT crawl the live web by default. It documents the intended pipeline:
 1. Load an approved comp list (JSON) — see comps.example.json
 2. For each URL, respect robots.txt and rate limits before any GET
 3. Prefer official APIs (e.g. Google Places) over HTML scraping aggregators
 4. Store structured rows + fetch time for the V2 "Neighborhood snapshot" block

Run: python tools/comp_snapshot_pipeline.py
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = Path(__file__).with_name("comps.example.json")


def load_comps(path: Path = EXAMPLE) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8-sig"))


def demo_report(rows: list[dict]) -> str:
    lines = [
        "Comp snapshot (demo report)",
        f"Generated {datetime.now(timezone.utc).isoformat()}",
        "",
    ]
    for r in rows:
        lines.append(
            f"  - {r.get('venue','?')}: source={r.get('source_type','?')} url={r.get('url','')}"
        )
    lines.append("")
    lines.append("Next: wire httpx/playwright fetchers + robots check per domain.")
    return "\n".join(lines)


def main() -> None:
    rows = load_comps()
    print(demo_report(rows))


if __name__ == "__main__":
    main()
