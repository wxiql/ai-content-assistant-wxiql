import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from content_assistant.generator import (
    generate_post,
    generate_blog_outline,
    suggest_hashtags,
    extract_keywords,
)


def test_generate_post_basic():
    result = generate_post("healthy eating", platform="twitter", seed=1)
    assert result["platform"] == "twitter"
    assert result["char_count"] <= result["max_chars"]
    assert "draft" in result


def test_generate_post_unknown_platform():
    try:
        generate_post("test", platform="myspace")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_generate_blog_outline():
    outline = generate_blog_outline("gardening")
    assert "gardening" in outline["title"].lower()
    assert len(outline["sections"]) == 6


def test_suggest_hashtags_includes_topic():
    tags = suggest_hashtags("digital marketing", "growth tips for marketing teams")
    assert any("digitalmarketing" in t for t in tags)
    assert len(tags) <= 8


def test_extract_keywords_filters_stopwords():
    keywords = extract_keywords("The quick brown fox jumps over the lazy dog")
    assert "the" not in keywords
    assert "quick" in keywords or "brown" in keywords
