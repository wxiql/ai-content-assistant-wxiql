import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from content_assistant.analyzer import (
    analyze_text,
    count_words,
    count_sentences,
    flesch_reading_ease,
    readability_label,
)


def test_count_words():
    assert count_words("The quick brown fox") == 4


def test_count_sentences():
    assert count_sentences("One. Two! Three?") == 3
    assert count_sentences("No punctuation here") == 1


def test_flesch_reading_ease_simple_text():
    score = flesch_reading_ease("The cat sat on the mat.")
    assert score > 60  # simple text should score reasonably easy


def test_readability_label_bounds():
    assert readability_label(95) == "Very easy"
    assert readability_label(10) == "Very difficult"


def test_analyze_text_keys():
    result = analyze_text("This is a short sample sentence for testing.")
    for key in ("characters", "words", "sentences", "flesch_score", "readability"):
        assert key in result
