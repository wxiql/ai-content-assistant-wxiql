"""Templates and constants used across the content assistant."""

# Platform-specific tone/length presets
PLATFORM_PRESETS = {
    "instagram": {
        "max_chars": 2200,
        "hook_style": "emoji",
        "hashtag_count": 8,
    },
    "twitter": {
        "max_chars": 280,
        "hook_style": "punchy",
        "hashtag_count": 2,
    },
    "linkedin": {
        "max_chars": 3000,
        "hook_style": "professional",
        "hashtag_count": 4,
    },
    "telegram": {
        "max_chars": 4096,
        "hook_style": "direct",
        "hashtag_count": 3,
    },
}

HOOK_TEMPLATES = {
    "emoji": [
        "✨ Let's talk about {topic} ✨",
        "🔥 Everything you need to know about {topic}",
        "👀 Here's the thing about {topic}...",
    ],
    "punchy": [
        "{topic}. Let's break it down.",
        "Unpopular opinion about {topic}:",
        "Here's what nobody tells you about {topic}.",
    ],
    "professional": [
        "A few thoughts on {topic}.",
        "What I've learned about {topic}:",
        "{topic} — a short breakdown.",
    ],
    "direct": [
        "About {topic}:",
        "{topic}, explained simply.",
    ],
}

CTA_TEMPLATES = [
    "What's your take? Drop a comment below.",
    "Save this for later if it was useful.",
    "Share this with someone who needs it.",
    "Follow for more on this topic.",
]

BLOG_SECTION_SKELETON = [
    "Introduction",
    "Why {topic} matters",
    "Key concepts",
    "Common mistakes",
    "Practical steps",
    "Conclusion",
]

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "in", "on", "for", "to",
    "is", "are", "was", "were", "be", "been", "with", "as", "at", "by",
    "this", "that", "it", "its", "from", "about", "into", "your", "you",
    "we", "our", "i", "he", "she", "they", "them", "his", "her",
}
