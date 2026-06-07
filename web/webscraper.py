#!/usr/bin/env python3
"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT
"""

import argparse
import csv
import json
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, base_url, output=None, fmt="txt", delay=0):
        self.base_url = base_url.rstrip("/")
        self.output = output
        self.fmt = fmt
        self.delay = delay
        self.visited = set()
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        })

    def fetch(self, url):
        try:
            resp = self.session.get(url, timeout=15)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(f"  [!] Failed {url}: {e}")
            return None

    def extract_text(self, html):
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)

    def extract_links(self, html, current_url):
        soup = BeautifulSoup(html, "html.parser")
        links = set()
        for a in soup.find_all("a", href=True):
            full = urljoin(current_url, a["href"])
            if urlparse(full).netloc == urlparse(self.base_url).netloc:
                links.add(full.split("#")[0])
        return links

    # ---------- modes ----------

    def single(self, url=None):
        target = url or self.base_url
        print(f"[*] Scraping: {target}")
        html = self.fetch(target)
        if not html:
            return
        text = self.extract_text(html)
        title = BeautifulSoup(html, "html.parser").title
        title_str = title.string.strip() if title else "No title"
        self.results.append({"url": target, "title": title_str, "content": text})
        print(f"  [✓] Title: {title_str}")

    def crawl(self, max_depth=2, max_pages=50):
        queue = [(self.base_url, 0)]
        while queue and len(self.visited) < max_pages:
            url, depth = queue.pop(0)
            if url in self.visited or depth > max_depth:
                continue
            self.visited.add(url)
            print(f"[*] Crawl (depth {depth}): {url}")
            html = self.fetch(url)
            if not html:
                continue
            text = self.extract_text(html)
            title = BeautifulSoup(html, "html.parser").title
            title_str = title.string.strip() if title else "No title"
            self.results.append({"url": url, "title": title_str, "content": text})
            print(f"  [✓] {title_str}  ({len(self.visited)}/{max_pages})")
            if depth < max_depth:
                for link in self.extract_links(html, url):
                    if link not in self.visited:
                        queue.append((link, depth + 1))
            time.sleep(self.delay)

    def products(self, product_sel, name_sel, price_sel):
        print(f"[*] Scraping products from: {self.base_url}")
        html = self.fetch(self.base_url)
        if not html:
            return
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select(product_sel)
        print(f"  [✓] Found {len(items)} product elements")
        for item in items:
            name_el = item.select_one(name_sel) if name_sel else None
            price_el = item.select_one(price_sel) if price_sel else None
            name = name_el.get_text(strip=True) if name_el else "N/A"
            price = price_el.get_text(strip=True) if price_el else "N/A"
            link_el = item.find("a", href=True)
            link = urljoin(self.base_url, link_el["href"]) if link_el else ""
            self.results.append({"name": name, "price": price, "url": link})
            print(f"    {name}  |  {price}")

    # ---------- output ----------

    def export(self):
        if self.fmt == "csv":
            self._write_csv()
        elif self.fmt == "json":
            self._write_json()
        else:
            self._write_text()

    def _write_text(self):
        out = self.output or "output.txt"
        with open(out, "w", encoding="utf-8") as f:
            for r in self.results:
                f.write(f"URL: {r.get('url', '')}\n")
                f.write(f"Title: {r.get('title', '')}\n")
                f.write(f"Content:\n{r.get('content', '')}\n")
                f.write("---\n\n")
        print(f"[+] Saved: {out}")

    def _write_csv(self):
        out = self.output or "output.csv"
        if not self.results:
            print("[!] No results to write")
            return
        keys = self.results[0].keys()
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(self.results)
        print(f"[+] Saved: {out}")

    def _write_json(self):
        out = self.output or "output.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"[+] Saved: {out}")


def main():
    parser = argparse.ArgumentParser(description="Web scraper with single, crawl, and product modes")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-m", "--mode", choices=["single", "crawl", "products"],
                        default="single", help="Scraping mode")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Crawl depth")
    parser.add_argument("-p", "--pages", type=int, default=50, help="Max pages to crawl")
    parser.add_argument("--delay", type=float, default=0, help="Delay between requests (s)")
    parser.add_argument("-f", "--format", choices=["txt", "csv", "json"], default="txt",
                        help="Output format")
    parser.add_argument("-o", "--output", help="Output file path")
    # product selectors
    parser.add_argument("--product-selector", help="CSS selector for product container")
    parser.add_argument("--name-selector", help="CSS selector for product name")
    parser.add_argument("--price-selector", help="CSS selector for product price")

    args = parser.parse_args()

    scraper = WebScraper(args.url, args.output, args.format, args.delay)

    if args.mode == "single":
        scraper.single()
    elif args.mode == "crawl":
        scraper.crawl(max_depth=args.depth, max_pages=args.pages)
    elif args.mode == "products":
        if not args.product_selector:
            print("[!] --product-selector is required in products mode")
            return
        scraper.products(args.product_selector, args.name_selector, args.price_selector)

    if scraper.results:
        scraper.export()


if __name__ == "__main__":
    main()
