#!/usr/bin/env python3
"""
generate_campaign_assets.py

Generate a structured ad concept pack from a brand brief and campaign request.
Supports OpenAI and OpenRouter for TEXT generation.

Usage:
  python3 scripts/generate_campaign_assets.py \
    --campaign campaigns/20260423-2145-day1-day2-flagship \
    --brand brand/generated-briefs/brand-brief.md \
    --request briefs/campaign-request.md

Outputs written into the campaign folder:
- outputs/concepts.generated.md
- outputs/copy-pack.generated.md
- outputs/manifest.generated.json

Notes:
- This script generates concepts, hooks, copy, and manifest structure.
- It does NOT render final images by itself.
- For v1, OpenAI/OpenRouter are used primarily for copy + structured concept generation.
- Students can then use Claude Code / Claude Cowork + image tools to create the visual assets.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import textwrap
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def load_env(path: Path) -> dict[str, str]:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip()
    return env


def require_file(path_str: str, label: str) -> Path:
    path = Path(path_str).expanduser()
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if not path.exists():
        raise SystemExit(f"Missing {label}: {path}")
    return path


def provider_config(env: dict[str, str]) -> tuple[str, str, str, str]:
    provider = env.get("TEXT_PROVIDER", "").strip().lower()
    openai_key = env.get("OPENAI_API_KEY", "").strip()
    openrouter_key = env.get("OPENROUTER_API_KEY", "").strip()

    if not provider:
        provider = "openai" if openai_key else "openrouter" if openrouter_key else ""

    if provider == "openai":
        if not openai_key:
            raise SystemExit("TEXT_PROVIDER=openai but OPENAI_API_KEY is missing in .env")
        model = env.get("TEXT_MODEL", "gpt-4.1-mini")
        return provider, "https://api.openai.com/v1/chat/completions", openai_key, model

    if provider == "openrouter":
        if not openrouter_key:
            raise SystemExit("TEXT_PROVIDER=openrouter but OPENROUTER_API_KEY is missing in .env")
        model = env.get("TEXT_MODEL", "openai/gpt-4.1-mini")
        return provider, "https://openrouter.ai/api/v1/chat/completions", openrouter_key, model

    raise SystemExit(
        "Could not determine TEXT_PROVIDER. Set TEXT_PROVIDER=openai or TEXT_PROVIDER=openrouter in .env."
    )


def prompt_payload(brand_brief: str, campaign_request: str) -> str:
    return textwrap.dedent(
        f"""
        You are generating a structured ad concept pack for the Limitless Ad System.

        Read the brand brief and campaign request carefully.
        Return ONLY valid JSON with this exact top-level shape:
        {{
          "campaign_name": "string",
          "summary": "string",
          "concepts": [
            {{
              "slug": "short-kebab-case",
              "title": "working title",
              "family": "Originals or Alternatives or another logical family label",
              "angle": "specific angle name",
              "notes": "why this concept works",
              "proof": "proof or mechanism line",
              "cta": "short call to action",
              "template": "split or poster or statement",
              "hook": "headline or opening hook",
              "primary_text": "1-3 sentence ad copy"
            }}
          ]
        }}

        Requirements:
        - Generate 8 strong concepts.
        - Be specific, conversion-oriented, and practical.
        - Use clear business language, not abstract fluff.
        - Keep CTA short.
        - Make slugs unique.

        BRAND BRIEF:
        {brand_brief}

        CAMPAIGN REQUEST:
        {campaign_request}
        """
    ).strip()


def post_json(url: str, headers: dict[str, str], payload: dict) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"API request failed: HTTP {e.code}\n{body}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error while calling provider: {e}") from e


def extract_content(provider: str, response: dict) -> str:
    try:
        return response["choices"][0]["message"]["content"]
    except Exception as exc:
        raise SystemExit(f"Unexpected {provider} response shape: {json.dumps(response)[:1000]}") from exc


def parse_json_response(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                text = part[4:].strip()
                break
            if part.startswith("{"):
                text = part
                break
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Model did not return valid JSON. First 1000 chars:\n{text[:1000]}") from exc


def write_outputs(campaign_dir: Path, data: dict) -> None:
    outputs = campaign_dir / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)

    concepts = data.get("concepts", [])
    manifest = []
    concept_lines = [f"# {data.get('campaign_name', 'Generated Campaign')}\n", "## Summary", data.get("summary", ""), ""]
    copy_lines = [f"# {data.get('campaign_name', 'Generated Campaign')} — Copy Pack", ""]

    for concept in concepts:
        slug = concept["slug"]
        family = concept.get("family", "Alternatives")
        manifest.append({
            "slug": slug,
            "title": concept.get("title", slug),
            "angle": concept.get("angle", "General"),
            "family": family,
            "file": f"assets/alternatives/{slug}.png",
            "notes": concept.get("notes", ""),
            "proof": concept.get("proof", ""),
            "cta": concept.get("cta", ""),
            "template": concept.get("template", "split"),
        })
        concept_lines += [
            f"## {concept.get('title', slug)}",
            f"- Slug: `{slug}`",
            f"- Family: {family}",
            f"- Angle: {concept.get('angle', '')}",
            f"- Notes: {concept.get('notes', '')}",
            f"- Proof: {concept.get('proof', '')}",
            f"- CTA: {concept.get('cta', '')}",
            f"- Template: {concept.get('template', '')}",
            "",
        ]
        copy_lines += [
            f"## {concept.get('title', slug)}",
            f"- Hook: {concept.get('hook', '')}",
            f"- Primary text: {concept.get('primary_text', '')}",
            f"- CTA: {concept.get('cta', '')}",
            "",
        ]

    (outputs / "manifest.generated.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    (outputs / "concepts.generated.md").write_text("\n".join(concept_lines))
    (outputs / "copy-pack.generated.md").write_text("\n".join(copy_lines))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a concept pack from brand brief + campaign request")
    parser.add_argument("--campaign", required=True, help="Campaign folder created by bootstrap_campaign.py")
    parser.add_argument("--brand", required=True, help="Path to brand brief markdown")
    parser.add_argument("--request", required=True, help="Path to campaign request markdown")
    args = parser.parse_args()

    env = load_env(ROOT / ".env")
    provider, url, api_key, model = provider_config(env)

    campaign_dir = require_file(args.campaign, "campaign folder")
    if not campaign_dir.is_dir():
        raise SystemExit(f"Campaign path must be a folder: {campaign_dir}")
    brand_path = require_file(args.brand, "brand brief")
    request_path = require_file(args.request, "campaign request")

    brand_brief = brand_path.read_text()
    campaign_request = request_path.read_text()

    payload = {
        "model": model,
        "temperature": 0.8,
        "messages": [
            {"role": "system", "content": "You are a senior direct-response creative strategist."},
            {"role": "user", "content": prompt_payload(brand_brief, campaign_request)},
        ],
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    if provider == "openrouter":
        headers["HTTP-Referer"] = "https://github.com/jetlauncher/limitless-ad-system"
        headers["X-Title"] = "Limitless Ad System"

    response = post_json(url, headers, payload)
    content = extract_content(provider, response)
    data = parse_json_response(content)
    write_outputs(campaign_dir, data)

    print(f"Generated assets into: {campaign_dir / 'outputs'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
