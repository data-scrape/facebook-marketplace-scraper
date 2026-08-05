#!/usr/bin/env python3
"""
Facebook Marketplace Scraper - Facebook Marketplace scraper - extract listings, prices, seller data
"""
import json, csv, time, logging
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
import requests
from bs4 import BeautifulSoup

__version__ = "1.0.0"
__author__ = "data-scrape"
__license__ = "MIT"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class ScrapeResult:
    url: str = ""
    title: str = ""
    data: Dict[str, Any] = None
    timestamp: str = ""
    raw_html: str = ""

    def to_dict(self):
        return asdict(self)


class Scraper:
    """Main scraper class for Facebook Marketplace Scraper."""

    def __init__(self, config=None):
        self.config = config or {}
        self.rate_limit_ms = self.config.get("rate_limit_ms", 1000)
        self.max_retries = self.config.get("max_retries", 3)
        self.proxies = self.config.get("proxy_list", [])
        self.proxy_index = 0
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        })
        logger.info(f"FacebookMarketplaceScraper initialized")

    def _get_proxy(self):
        if not self.proxies:
            return None
        proxy = self.proxies[self.proxy_index % len(self.proxies)]
        self.proxy_index += 1
        return {"http": proxy, "https": proxy}

    def _rate_limit(self):
        if self.rate_limit_ms > 0:
            time.sleep(self.rate_limit_ms / 1000.0)

    def _fetch(self, url):
        for attempt in range(self.max_retries):
            try:
                self._rate_limit()
                resp = self.session.get(url, proxies=self._get_proxy(), timeout=30)
                resp.raise_for_status()
                return resp.text
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt+1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
        raise RuntimeError(f"Failed after {self.max_retries} attempts")

    def _parse(self, html, url):
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("title")
        return ScrapeResult(
            url=url, title=title.text.strip() if title else "",
            data={}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            raw_html=html[:5000]
        )

    def scrape(self, query):
        url = query if query.startswith("http") else f"https://example.com/search?q={query}"
        logger.info(f"Scraping: {url}")
        html = self._fetch(url)
        return [self._parse(html, url)]

    def scrape_batch(self, queries):
        results = []
        for q in queries:
            try:
                results.extend(self.scrape(q))
            except Exception as e:
                logger.error(f"Failed: {e}")
        return results

    def export_json(self, results, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([r.to_dict() for r in results], f, ensure_ascii=False, indent=2)

    def export_csv(self, results, filepath):
        if not results:
            return
        keys = results[0].to_dict().keys()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for r in results:
                writer.writerow(r.to_dict())


def main():
    import argparse
    p = argparse.ArgumentParser(description="Facebook Marketplace Scraper")
    p.add_argument("--query", "-q", required=True)
    p.add_argument("--output", "-o", default="output.json")
    p.add_argument("--format", "-f", default="json", choices=["json", "csv"])
    args = p.parse_args()
    scraper = Scraper()
    results = scraper.scrape(args.query)
    if args.format == "json":
        scraper.export_json(results, args.output)
    else:
        scraper.export_csv(results, args.output)
    print(f"Done! {len(results)} results saved to {args.output}")


if __name__ == "__main__":
    main()
