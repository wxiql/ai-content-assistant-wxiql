#!/usr/bin/env python3
"""Command-line interface for the AI Content Assistant.

Examples
--------
    python cli.py post "remote work productivity" --platform linkedin
    python cli.py outline "intermittent fasting"
    python cli.py analyze "Your text goes here, as much as you like."
"""

import argparse
import json
import sys

from content_assistant.generator import generate_post, generate_blog_outline
from content_assistant.analyzer import analyze_text


def cmd_post(args):
    result = generate_post(
        topic=args.topic,
        platform=args.platform,
        body=args.body,
        seed=args.seed,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result["draft"])
        print(f"\n--- {result['char_count']}/{result['max_chars']} chars ---")


def cmd_outline(args):
    result = generate_blog_outline(args.topic)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result["title"])
        for i, section in enumerate(result["sections"], 1):
            print(f"  {i}. {section}")


def cmd_analyze(args):
    text = args.text
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    if not text:
        print("Provide text via argument or --file", file=sys.stderr)
        sys.exit(1)

    result = analyze_text(text)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for key, value in result.items():
            print(f"{key.replace('_', ' ').title()}: {value}")


def build_parser():
    parser = argparse.ArgumentParser(description="AI Content Assistant CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_post = sub.add_parser("post", help="Generate a social media post draft")
    p_post.add_argument("topic")
    p_post.add_argument("--platform", default="instagram",
                         choices=["instagram", "twitter", "linkedin", "telegram"])
    p_post.add_argument("--body", default=None, help="Custom body text")
    p_post.add_argument("--seed", type=int, default=None, help="Random seed")
    p_post.add_argument("--json", action="store_true")
    p_post.set_defaults(func=cmd_post)

    p_outline = sub.add_parser("outline", help="Generate a blog post outline")
    p_outline.add_argument("topic")
    p_outline.add_argument("--json", action="store_true")
    p_outline.set_defaults(func=cmd_outline)

    p_analyze = sub.add_parser("analyze", help="Analyze text readability")
    p_analyze.add_argument("text", nargs="?", default=None)
    p_analyze.add_argument("--file", default=None, help="Read text from a file")
    p_analyze.add_argument("--json", action="store_true")
    p_analyze.set_defaults(func=cmd_analyze)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
