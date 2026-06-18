import requests

class AIScraper:
    def __init__(self, llm=None): self.llm, self.s = llm, requests.Session()
    def fetch(self, url, retries=3):
        for _ in range(retries):
            try: r = self.s.get(url, timeout=10); return r.text if r.ok else None
            except: pass
    def extract(self, html, schema):
        return self.llm.generate(f"Extract: {schema}\n{html[:3000]}") if self.llm else {}
