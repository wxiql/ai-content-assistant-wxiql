"""Text analysis utilities: word/char counts and a Flesch reading-ease score."""

import re


VOWELS = "aeiouy"


def count_words(text):
    return len(re.findall(r"[A-Za-zÀ-ÿ']+", text))


def count_sentences(text):
    sentences = re.split(r"[.!?]+", text)
    return max(1, len([s for s in sentences if s.strip()]))


def count_syllables(word):
    word = word.lower()
    if not word:
        return 0
    syllables = 0
    prev_was_vowel = False
    for char in word:
        is_vowel = char in VOWELS
        if is_vowel and not prev_was_vowel:
            syllables += 1
        prev_was_vowel = is_vowel
    if word.endswith("e") and syllables > 1:
        syllables -= 1
    return max(1, syllables)


def flesch_reading_ease(text):
    """Compute the Flesch Reading Ease score (0-100, higher = easier)."""
    words = re.findall(r"[A-Za-zÀ-ÿ']+", text)
    word_count = len(words)
    sentence_count = count_sentences(text)

    if word_count == 0:
        return 0.0

    syllable_count = sum(count_syllables(w) for w in words)

    score = (
        206.835
        - 1.015 * (word_count / sentence_count)
        - 84.6 * (syllable_count / word_count)
    )
    return round(score, 2)


def readability_label(score):
    if score >= 90:
        return "Very easy"
    if score >= 70:
        return "Easy"
    if score >= 60:
        return "Standard"
    if score >= 30:
        return "Difficult"
    return "Very difficult"


def analyze_text(text):
    """Return a dict of basic stats and readability for a text block."""
    words = count_words(text)
    sentences = count_sentences(text)
    score = flesch_reading_ease(text)
    return {
        "characters": len(text),
        "words": words,
        "sentences": sentences,
        "avg_words_per_sentence": round(words / sentences, 2) if sentences else 0,
        "flesch_score": score,
        "readability": readability_label(score),
    }
