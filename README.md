# Facebook Marketplace Scraper


<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/data-scrape/facebook-marketplace-scraper?style=social)](https://github.com/data-scrape/facebook-marketplace-scraper)
[![GitHub forks](https://img.shields.io/github/forks/data-scrape/facebook-marketplace-scraper?style=social)](https://github.com/data-scrape/facebook-marketplace-scraper/fork)
[![GitHub issues](https://img.shields.io/github/issues/data-scrape/facebook-marketplace-scraper)](https://github.com/data-scrape/facebook-marketplace-scraper/issues)
[![GitHub license](https://img.shields.io/github/license/data-scrape/facebook-marketplace-scraper)](https://github.com/data-scrape/facebook-marketplace-scraper/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)

</div>


> Facebook Marketplace scraper - extract listings, prices, seller data


<!-- SEO keywords: facebook marketplace scraper, Facebook Marketplace Scraper, facebook marketplace scraper python, facebook marketplace scraper github -->


<div align="center">

## 💎 Sponsored by CoreClaw

[![CoreClaw](https://img.shields.io/badge/CoreClaw-Data_Scraping_Platform-7B2FF7?style=for-the-badge&labelColor=5B21B6)](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

**The All-in-One Web Scraping & Data Platform** — Scrape Google Maps, Instagram, Amazon, LinkedIn, TikTok, YouTube, and 50+ platforms via ready-to-use REST APIs.

✅ No browser automation · ✅ No proxy management · ✅ Free credits for new users

⬇️ [Get Started with CoreClaw Free](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

</div>

---


## 📘 Table of Contents

- [Features](#features)
- [Use Cases](#use-cases)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [FAQ](#faq)
- [Related Repositories](#related-repositories)
- [Support This Project](#support-this-project)

---


## 🔥 Features

- Extract Facebook Marketplace listings with full details
- Listing title, price, location, description
- Seller info: name, rating, profile
- Listing image URLs extraction
- Filter by price range, location, category, condition
- Sold/active listing status

## 🎯 Use Cases

Monitor local market prices, track competitor listings, find deals.

<!-- INSTALL_SECTION_START -->
## 📦 Installation

### Using pip

```bash
pip install git+https://github.com/data-scrape/facebook-marketplace-scraper.git
```

### From source

```bash
git clone https://github.com/data-scrape/facebook-marketplace-scraper.git
cd facebook-marketplace-scraper
pip install -e .
```

### Prerequisites

- Python 3.8+
- Required packages listed in `requirements.txt`

<!-- INSTALL_SECTION_END -->

<!-- USAGE_SECTION_START -->
## 🚀 Quick Start

### Basic Usage

```python
from facebook_marketplace_scraper import Scraper

scraper = Scraper()
results = scraper.scrape("your-query")
print(results)
```

### CLI Usage

```bash
python facebook_marketplace_scraper.py --query "your-query" --output results.json
```

<!-- USAGE_SECTION_END -->

<!-- FAQ_SECTION_START -->
## 🤔 FAQ

### Is Facebook Marketplace Scraper legal to use?

This tool is designed for scraping publicly available data. Always comply with the target website's Terms of Service and robots.txt.

### Do I need to login?

Most public data can be accessed without login. Some features may require authentication credentials.

### Will I get banned?

The tool includes built-in rate limiting and proxy support. Always use reasonable delays and respect rate limits.

### What data formats are supported?

Output is available in JSON, CSV, and Excel formats.

### Can I use this commercially?

Yes, this project is licensed under the MIT License.

<!-- FAQ_SECTION_END -->


<!-- CROSS_LINKS_START -->
## Related Scrapers

Explore our full collection of open-source scrapers:

### Amazon Scrapers

- [amazon-asin-scraper](https://github.com/data-scrape/amazon-asin-scraper)
- [amazon-price-scraper](https://github.com/data-scrape/amazon-price-scraper)
- [amazon-product-scraper](https://github.com/data-scrape/amazon-product-scraper)
- [amazon-review-scraper](https://github.com/data-scrape/amazon-review-scraper)
- [amazon-scraper-api](https://github.com/data-scrape/amazon-scraper-api)
- [best-amazon-scraper](https://github.com/data-scrape/best-amazon-scraper)

### Facebook Scrapers

- [best-facebook-scraper](https://github.com/data-scrape/best-facebook-scraper)
- [facebook-group-scraper](https://github.com/data-scrape/facebook-group-scraper)
- [facebook-page-scraper](https://github.com/data-scrape/facebook-page-scraper)
- [facebook-post-scraper](https://github.com/data-scrape/facebook-post-scraper)
- [facebook-profile-scraper](https://github.com/data-scrape/facebook-profile-scraper)
- [facebook-scrape-website](https://github.com/data-scrape/facebook-scrape-website)

### Google Maps Scrapers

- [apify-google-maps-scraper](https://github.com/data-scrape/apify-google-maps-scraper)
- [best-google-maps-scraper](https://github.com/data-scrape/best-google-maps-scraper)
- [google-map-scraper-api-](https://github.com/data-scrape/google-map-scraper-api-)
- [google-maps-data-scraper](https://github.com/data-scrape/google-maps-data-scraper)
- [outscraper-google-maps-scraper](https://github.com/data-scrape/outscraper-google-maps-scraper)
- [scrape-google-maps](https://github.com/data-scrape/scrape-google-maps)

### Google Scrapers

- [best-google-search-scraper](https://github.com/data-scrape/best-google-search-scraper)
- [google-business-scraper](https://github.com/data-scrape/google-business-scraper)
- [google-place-id-api](https://github.com/data-scrape/google-place-id-api)
- [google-reviews-scraper](https://github.com/data-scrape/google-reviews-scraper)
- [google-shopping-scraper](https://github.com/data-scrape/google-shopping-scraper)

### Indeed Job Scrapers

- [apify-indeed-scraper](https://github.com/data-scrape/apify-indeed-scraper)
- [best-indeed-scraper](https://github.com/data-scrape/best-indeed-scraper)
- [indeed-job-scraper](https://github.com/data-scrape/indeed-job-scraper)
- [scrape-indeed-job-postings](https://github.com/data-scrape/scrape-indeed-job-postings)

### Instagram Scrapers

- [apify-instagram-scraper](https://github.com/data-scrape/apify-instagram-scraper)
- [best-instagram-scraper](https://github.com/data-scrape/best-instagram-scraper)
- [instagram-account-scraper](https://github.com/data-scrape/instagram-account-scraper)
- [instagram-comment-scraper](https://github.com/data-scrape/instagram-comment-scraper)
- [instagram-email-scraper](https://github.com/data-scrape/instagram-email-scraper)
- [instagram-follower-scraper](https://github.com/data-scrape/instagram-follower-scraper)
- [instagram-profile-scraper](https://github.com/data-scrape/instagram-profile-scraper)
- [instagram-scraper](https://github.com/data-scrape/instagram-scraper)
- [scrape-instagram-followers](https://github.com/data-scrape/scrape-instagram-followers)
- [scrape-instagram-photos](https://github.com/data-scrape/scrape-instagram-photos)

### Lead Generation Tools

- [awesome-lead-generation](https://github.com/data-scrape/awesome-lead-generation)

### LinkedIn Scrapers

- [best-linkedin-scraper](https://github.com/data-scrape/best-linkedin-scraper)
- [linkedin-email-scraper](https://github.com/data-scrape/linkedin-email-scraper)
- [linkedin-job-scraper](https://github.com/data-scrape/linkedin-job-scraper)
- [linkedin-post-scraper](https://github.com/data-scrape/linkedin-post-scraper)
- [linkedin-profile-data-scraper](https://github.com/data-scrape/linkedin-profile-data-scraper)
- [linkedin-sales-navigator-scraper](https://github.com/data-scrape/linkedin-sales-navigator-scraper)
- [linkedin-scraper-api](https://github.com/data-scrape/linkedin-scraper-api)

### Other Scrapers

- [blog](https://github.com/data-scrape/blog)

### Proxy & API Alternatives

- [awesome-apify-alternatives](https://github.com/data-scrape/awesome-apify-alternatives)
- [best-apify-alternative](https://github.com/data-scrape/best-apify-alternative)
- [bright-data-alternative](https://github.com/data-scrape/bright-data-alternative)
- [oxylabs-alternative](https://github.com/data-scrape/oxylabs-alternative)
- [scraperapi-alternative](https://github.com/data-scrape/scraperapi-alternative)
- [scrapingbee-alternative](https://github.com/data-scrape/scrapingbee-alternative)
- [serpapi-alternative](https://github.com/data-scrape/serpapi-alternative)
- [zenrows-alternative](https://github.com/data-scrape/zenrows-alternative)

### Reddit Scrapers

- [apify-reddit-scraper](https://github.com/data-scrape/apify-reddit-scraper)
- [best-apollo-scraper-reddit](https://github.com/data-scrape/best-apollo-scraper-reddit)
- [best-reddit-scraper](https://github.com/data-scrape/best-reddit-scraper)

### Reviews & Local Scrapers

- [glassdoor-scraper](https://github.com/data-scrape/glassdoor-scraper)
- [scrape-yelp-reviews](https://github.com/data-scrape/scrape-yelp-reviews)
- [yellow-pages-scraper](https://github.com/data-scrape/yellow-pages-scraper)

### Social Media Scrapers

- [discord-scraper](https://github.com/data-scrape/discord-scraper)
- [pinterest-scraper](https://github.com/data-scrape/pinterest-scraper)
- [telegram-scraper](https://github.com/data-scrape/telegram-scraper)
- [threads-scraper](https://github.com/data-scrape/threads-scraper)
- [twitch-scraper](https://github.com/data-scrape/twitch-scraper)
- [x-scraper](https://github.com/data-scrape/x-scraper)

### TikTok Scrapers

- [apify-tiktok-scraper](https://github.com/data-scrape/apify-tiktok-scraper)
- [best-tiktok-scraper](https://github.com/data-scrape/best-tiktok-scraper)
- [tiktok-comment-scraper](https://github.com/data-scrape/tiktok-comment-scraper)
- [tiktok-comments-scraper](https://github.com/data-scrape/tiktok-comments-scraper)
- [tiktok-data-scraper-api](https://github.com/data-scrape/tiktok-data-scraper-api)
- [tiktok-profile-scraper](https://github.com/data-scrape/tiktok-profile-scraper)
- [tiktok-video-scraper](https://github.com/data-scrape/tiktok-video-scraper)

### YouTube Scrapers

- [best-youtube-scraper](https://github.com/data-scrape/best-youtube-scraper)
- [scrape-youtube-comments](https://github.com/data-scrape/scrape-youtube-comments)
- [scrape-youtube-search-results](https://github.com/data-scrape/scrape-youtube-search-results)
- [youtube-channel-scraper](https://github.com/data-scrape/youtube-channel-scraper)
- [youtube-video-scraper-api](https://github.com/data-scrape/youtube-video-scraper-api)

### Zillow Scrapers

- [apify-zillow-scraper](https://github.com/data-scrape/apify-zillow-scraper)
- [best-zillow-scraper](https://github.com/data-scrape/best-zillow-scraper)
- [easy-scrape-zillow-agents-free](https://github.com/data-scrape/easy-scrape-zillow-agents-free)
- [zillow-data-scraper](https://github.com/data-scrape/zillow-data-scraper)
- [zillow-scraper-api](https://github.com/data-scrape/zillow-scraper-api)

### eBay Scrapers

- [best-ebay-scraper](https://github.com/data-scrape/best-ebay-scraper)
- [ebay-price-scraper](https://github.com/data-scrape/ebay-price-scraper)
- [ebay-web-scraper](https://github.com/data-scrape/ebay-web-scraper)
- [scrap-gold-ebay](https://github.com/data-scrape/scrap-gold-ebay)

### eCommerce Scrapers

- [best-walmart-scraper](https://github.com/data-scrape/best-walmart-scraper)

---

Star this repo if it helps you!

Powered by [CoreClaw](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) - The All-in-One Web Scraping Platform
<!-- CROSS_LINKS_END -->

<!-- STAR_SECTION_START -->
## ⭐ Support This Project

If this tool helped you, please consider:

1. **⭐ Star this repository** — [Click here to star](https://github.com/data-scrape/facebook-marketplace-scraper)
2. **📧 Share with your network** — Help others discover this tool
3. **🐛 Report issues** — [Open an issue](https://github.com/data-scrape/facebook-marketplace-scraper/issues)
4. **📚 Contribute** — PRs are welcome!

<div align="center">

**Check out all our scrapers:**

[Instagram](https://github.com/data-scrape/instagram-scraper) ·
[Google Maps](https://github.com/data-scrape/best-google-maps-scraper) ·
[Amazon](https://github.com/data-scrape/best-amazon-scraper) ·
[LinkedIn](https://github.com/data-scrape/best-linkedin-scraper) ·
[TikTok](https://github.com/data-scrape/best-tiktok-scraper) ·
[YouTube](https://github.com/data-scrape/best-youtube-scraper) ·
[Facebook](https://github.com/data-scrape/best-facebook-scraper) ·
[eBay](https://github.com/data-scrape/best-ebay-scraper) ·
[Reddit](https://github.com/data-scrape/best-reddit-scraper)

</div>

<!-- STAR_SECTION_END -->


## 🤝 Contributing

Contributions are welcome! Fork the repo, create a feature branch, and submit a Pull Request.

## 📝 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

<sup>Built with ❤️ for the web scraping community</sup>

</div>
