#!/usr/bin/env python3
"""
bootstrap_campaign.py

Create a local campaign workspace under campaigns/ for the Limitless Ad System.

Usage:
  python3 scripts/bootstrap_campaign.py --name "day1-day2-flagship"

What it creates:
  campaigns/YYYYMMDD-HHMM-day1-day2-flagship/
    briefs/
    outputs/
    assets/originals/
    assets/alternatives/

This script is intentionally simple and beginner-friendly.
Generated campaigns are meant to stay local by default.
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-") or "campaign"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a local campaign workspace")
    parser.add_argument("--name", required=True, help="Human-friendly campaign name")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    campaigns_dir = root / "campaigns"
    campaigns_dir.mkdir(exist_ok=True)

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    slug = slugify(args.name)
    campaign_dir = campaigns_dir / f"{stamp}-{slug}"

    for rel in [
        "briefs",
        "outputs",
        "assets/originals",
        "assets/alternatives",
    ]:
        (campaign_dir / rel).mkdir(parents=True, exist_ok=True)

    readme = campaign_dir / "README.md"
    readme.write_text(
        f"# {args.name}\n\n"
        "## Next steps\n"
        "1. Put your campaign request markdown into `briefs/`.\n"
        "2. Put your brand brief into `briefs/` or reference the one in `brand/generated-briefs/`.\n"
        "3. Run `python3 scripts/generate_campaign_assets.py --campaign <folder> --brand <brand-brief.md> --request <campaign-request.md>`.\n"
        "4. Save generated image files into `assets/originals/` and `assets/alternatives/`.\n"
        "5. Copy or merge the generated manifest into the review board when ready.\n"
    )

    print(campaign_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
