#!/usr/bin/env python3
"""
Placements and Internships Support — curated portal browser
Constraint: C1 (no AI API calls)
Requirements: Python 3.10+, no external dependencies
How to run:
    python3 tools/live-data/placements-and-internships/placements_and_internships.py --category placement
    python3 tools/live-data/placements-and-internships/placements_and_internships.py --category internship --tag engineering
Example output: 1. LinkedIn Jobs — professional network with placement listings across industries.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def _default_repo_root() -> Path:
    env_root = os.environ.get("SRUJANABUDDY_REPO_ROOT")
    if env_root:
        return Path(env_root).expanduser().resolve()
    return Path(__file__).resolve().parents[3]


def _load_resources(repo_root: Path) -> list[dict]:
    sources = [
        ("internship", repo_root / "knowledge" / "internship-portals.json"),
        ("placement", repo_root / "knowledge" / "placement-portals.json"),
    ]

    resources: list[dict] = []
    for category, path in sources:
        try:
            entries = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"[ERROR] Data file not found: {path}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as exc:
            print(f"[ERROR] Could not parse {path}: {exc}", file=sys.stderr)
            sys.exit(1)

        for entry in entries:
            tagged_entry = dict(entry)
            tagged_entry["category"] = category
            tagged_entry["tags"] = [str(tag).lower() for tag in entry.get("tags", [])]
            resources.append(tagged_entry)
    return resources


def _filter_resources(resources: list[dict], args: argparse.Namespace) -> list[dict]:
    tag_filters = [tag.lower() for tag in args.tag]
    search_text = args.search.lower() if args.search else ""
    portal_types = [portal_type.lower() for portal_type in args.portal_type]

    filtered: list[dict] = []
    for resource in resources:
        if args.category != "all" and resource["category"] != args.category:
            continue
        if tag_filters and not all(tag in resource["tags"] for tag in tag_filters):
            continue
        if portal_types and resource.get("type", "").lower() not in portal_types:
            continue
        if search_text:
            haystack = " ".join(
                [
                    resource.get("name", ""),
                    resource.get("description", ""),
                    resource.get("eligibility", ""),
                    " ".join(resource.get("tags", [])),
                ]
            ).lower()
            if search_text not in haystack:
                continue
        filtered.append(resource)

    return filtered[: args.limit] if args.limit else filtered


def _render_markdown(resources: list[dict], repo_root: Path) -> str:
    guidance_path = repo_root / "docs" / "placements-and-internships-guidance.md"
    lines = [
        "# Placements and Internships Support",
        f"- Guidance note: {guidance_path}",
        f"- Matching resources: {len(resources)}",
        "",
    ]

    for index, resource in enumerate(resources, start=1):
        lines.extend(
            [
                f"{index}. **{resource['name']}** [{resource['category']}]",
                f"   - URL: {resource['url']}",
                f"   - Type: {resource['type']}",
                f"   - Eligibility: {resource['eligibility']}",
                f"   - Tags: {', '.join(resource['tags'])}",
                f"   - {resource['description']}",
            ]
        )
    if not resources:
        lines.append("No matching portals found. Try a broader tag or remove the search filter.")
    return "\n".join(lines)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Browse curated placements and internships resources for SrujanaBuddy."
    )
    parser.add_argument(
        "--repo-root",
        default=str(_default_repo_root()),
        help="Path to the SrujanaBuddy repository root.",
    )
    parser.add_argument(
        "--category",
        choices=["all", "placement", "internship"],
        default="all",
        help="Filter resources by category.",
    )
    parser.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Filter by tag. Repeat the flag for multiple tags.",
    )
    parser.add_argument(
        "--portal-type",
        action="append",
        default=[],
        help="Filter by portal type (national, international, company-specific). Repeat as needed.",
    )
    parser.add_argument(
        "--search",
        help="Case-insensitive text search across name, description, eligibility, and tags.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum number of results to show. Default: all.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    repo_root = Path(args.repo_root).expanduser().resolve()
    resources = _load_resources(repo_root)
    filtered = _filter_resources(resources, args)

    if args.format == "json":
        print(json.dumps(filtered, indent=2))
        return

    print(_render_markdown(filtered, repo_root))


if __name__ == "__main__":
    main()
