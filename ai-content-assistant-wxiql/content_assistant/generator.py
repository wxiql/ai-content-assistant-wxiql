"""Content generation logic: social posts, hashtags, and blog outlines."""

import random
import re
from collections import Counter

from .templates import (
    PLATFORM_PRESETS,
    HOOK_TEMPLATES,
    CTA_TEMPLATES,
    BLOG_SECTION_SKELETON,
    STOPWORDS,
)


def extract_keywords(text, limit=10):
    """Pull the most frequent meaningful words out of a text block."""
    words = re.findall(r"[A-Za-zÀ-ÿ']+", text.lower())
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    counts = Counter(words)
    return [word for word, _ in counts.most_common(limit)]


def suggest_hashtags(topic, body="", count=None, platform="instagram"):
    """Suggest hashtags from the topic and body text."""
    preset = PLATFORM_PRESETS.get(platform, PLATFORM_PRESETS["instagram"])
    count = count or preset["hashtag_count"]

    seed_text = f"{topic} {body}"
    keywords = extract_keywords(seed_text, limit=count * 2)

    # Always include a hashtag made from the topic itself first.
    topic_tag = "#" + re.sub(r"\s+", "", topic.strip().lower())
    tags = [topic_tag]

    for kw in keywords:
        tag = f"#{kw}"
        if tag not in tags:
            tags.append(tag)
        if len(tags) >= count:
            break

    return tags[:count]


def generate_post(topic, platform="instagram", body=None, seed=None):
    """Generate a short social media post draft for a given platform."""
    if platform not in PLATFORM_PRESETS:
        raise ValueError(
            f"Unknown platform '{platform}'. Choose from: {list(PLATFORM_PRESETS)}"
        )

    rng = random.Random(seed)
    preset = PLATFORM_PRESETS[platform]
    hook_style = preset["hook_style"]

    hook = rng.choice(HOOK_TEMPLATES[hook_style]).format(topic=topic)
    cta = rng.choice(CTA_TEMPLATES)

    if body is None:
        body = (
            f"{topic} is worth understanding well. Start with the basics, "
            f"stay consistent, and adjust as you learn what works."
        )

    hashtags = suggest_hashtags(topic, body, platform=platform)

    parts = [hook, "", body, "", cta, "", " ".join(hashtags)]
    draft = "\n".join(parts)

    max_chars = preset["max_chars"]
    truncated = False
    if len(draft) > max_chars:
        draft = draft[: max_chars - 1].rstrip() + "…"
        truncated = True

    return {
        "platform": platform,
        "draft": draft,
        "char_count": len(draft),
        "max_chars": max_chars,
        "truncated": truncated,
        "hashtags": hashtags,
    }


def generate_blog_outline(topic):
    """Produce a simple structured outline for a blog post about a topic."""
    sections = []
    for section in BLOG_SECTION_SKELETON:
        sections.append(section.format(topic=topic))
    return {
        "title": f"{topic}: A Practical Guide",
        "sections": sections,
    }
