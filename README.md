# Web Scraper Ai

AI-powered web scraper that understands page structure.

## Features
- LLM-based content extraction (no selectors needed)
- Anti-bot bypass (Playwright + stealth)
- Structured data output (JSON, CSV)
- Rate limiting and proxy rotation

## Example
```python
from scraper import AIScraper
s = AIScraper(model='gpt-4o-mini')
data = s.extract('https://example.com', schema={'title': str, 'price': float})
```

## License
MIT
