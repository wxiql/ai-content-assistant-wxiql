# ai-content-assistant-wxiql

AI assistant for content creation and automation.

A small, dependency-free Python toolkit that helps draft social media posts,
outline blog articles, and check the readability of text — all from the
command line.

## Features

- **Post drafting** — generates a platform-tailored post (Instagram, Twitter,
  LinkedIn, Telegram) with a hook, body, call-to-action, and hashtags.
- **Hashtag suggestions** — pulls relevant hashtags from the topic and body
  text using simple keyword frequency analysis.
- **Blog outlines** — produces a ready-to-fill section structure for a blog
  post on any topic.
- **Readability analysis** — computes word/sentence counts and a Flesch
  Reading Ease score for any text.

## Installation

No external dependencies are required — just Python 3.8+.

```bash
git clone https://github.com/<your-username>/ai-content-assistant-wxiql.git
cd ai-content-assistant-wxiql
```

## Usage

```bash
# Generate a social media post
python cli.py post "remote work productivity" --platform linkedin

# Generate a blog outline
python cli.py outline "intermittent fasting"

# Analyze the readability of a piece of text
python cli.py analyze "Your text goes here, as much as you like."

# Or analyze a file
python cli.py analyze --file draft.txt

# Get JSON output for any command
python cli.py post "healthy eating" --platform twitter --json
```

## Running tests

```bash
pip install pytest
pytest tests/ -v
```

## Project structure

```
ai-content-assistant-wxiql/
├── cli.py                     # CLI entry point
├── content_assistant/
│   ├── __init__.py
│   ├── generator.py           # post & outline generation
│   ├── analyzer.py            # readability analysis
│   └── templates.py           # templates & presets
├── tests/
│   ├── test_generator.py
│   └── test_analyzer.py
├── requirements.txt
└── README.md
```

## License

MIT
