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
## 🔗 Related Repositories

Explore our complete web scraping toolkit:

### Instagram Scrapers

- [Instagram Scraper](https://github.com/data-scrape/instagram-scraper) - Python Instagram scraper - extract posts, profiles, followers, hashtags
- [Instagram Account Scraper](https://github.com/data-scrape/instagram-account-scraper) - Instagram account scraper - profiles, posts, reels, stories
- [Instagram Follower Scraper](https://github.com/data-scrape/instagram-follower-scraper) - Instagram follower scraper - extract follower and following lists
- [Instagram Profile Scraper](https://github.com/data-scrape/instagram-profile-scraper) - Instagram profile scraper - extract profile data and analytics
- [Scrape Instagram Followers](https://github.com/data-scrape/scrape-instagram-followers) - Scrape Instagram followers and following lists in bulk
- [Best Instagram Scraper](https://github.com/data-scrape/best-instagram-scraper) - Best Instagram scraper 2025 - extract posts, reels, stories, profiles
- [Apify Instagram Scraper](https://github.com/data-scrape/apify-instagram-scraper) - Apify Instagram scraper alternative - free Python Instagram scraper
- [Scrape Instagram Photos](https://github.com/data-scrape/scrape-instagram-photos) - Scrape Instagram photos - download photos from any profile in bulk
- [Instagram Comment Scraper](https://github.com/data-scrape/instagram-comment-scraper) - Instagram comment scraper - extract comments from posts and reels
- [Instagram Email Scraper](https://github.com/data-scrape/instagram-email-scraper) - Instagram email scraper - extract emails from Instagram bios and profiles

### Google Maps Scrapers

- [Google Maps Data Scraper](https://github.com/data-scrape/google-maps-data-scraper) - Google Maps data scraper - extract business data, reviews, ratings
- [Best Google Maps Scraper](https://github.com/data-scrape/best-google-maps-scraper) - Best Google Maps scraper 2025 - business data extraction tool
- [Scrape Google Maps](https://github.com/data-scrape/scrape-google-maps) - Scrape Google Maps - extract places, reviews, and business data
- [Google Map Scraper Api ](https://github.com/data-scrape/google-map-scraper-api-) - Google Maps scraper API - REST API for business data extraction
- [Outscraper Google Maps Scraper](https://github.com/data-scrape/outscraper-google-maps-scraper) - Outscraper Google Maps scraper alternative - free Python tool
- [Apify Google Maps Scraper](https://github.com/data-scrape/apify-google-maps-scraper) - Apify Google Maps scraper alternative - free Python scraper

### Amazon Scrapers

- [Best Amazon Scraper](https://github.com/data-scrape/best-amazon-scraper) - Best Amazon scraper 2025 - extract product data, reviews, prices
- [Amazon Review Scraper](https://github.com/data-scrape/amazon-review-scraper) - Amazon review scraper - extract product reviews and ratings in bulk
- [Amazon Product Scraper](https://github.com/data-scrape/amazon-product-scraper) - Amazon product scraper - extract product details, images, and specs
- [Amazon Asin Scraper](https://github.com/data-scrape/amazon-asin-scraper) - Amazon ASIN scraper - lookup ASIN data and product information
- [Amazon Price Scraper](https://github.com/data-scrape/amazon-price-scraper) - Amazon price scraper - track prices and extract pricing history
- [Amazon Scraper Api](https://github.com/data-scrape/amazon-scraper-api) - Amazon scraper API - REST API for Amazon data extraction

### LinkedIn Scrapers

- [Best Linkedin Scraper](https://github.com/data-scrape/best-linkedin-scraper) - Best LinkedIn scraper 2025 - extract profiles, company data, jobs
- [Linkedin Profile Data Scraper](https://github.com/data-scrape/linkedin-profile-data-scraper) - LinkedIn profile data scraper - extract profiles, experience, skills
- [Linkedin Job Scraper](https://github.com/data-scrape/linkedin-job-scraper) - LinkedIn job scraper - extract job listings, salaries, company info
- [Linkedin Sales Navigator Scraper](https://github.com/data-scrape/linkedin-sales-navigator-scraper) - LinkedIn Sales Navigator scraper - extract leads and accounts
- [Linkedin Email Scraper](https://github.com/data-scrape/linkedin-email-scraper) - LinkedIn email scraper - extract emails from LinkedIn profiles
- [Linkedin Scraper Api](https://github.com/data-scrape/linkedin-scraper-api) - LinkedIn scraper API - REST API for LinkedIn data extraction
- [Linkedin Post Scraper](https://github.com/data-scrape/linkedin-post-scraper) - LinkedIn post scraper - extract posts, likes, comments, analytics

### YouTube Scrapers

- [Best Youtube Scraper](https://github.com/data-scrape/best-youtube-scraper) - Best YouTube scraper 2025 - extract videos, comments, channel data
- [Youtube Channel Scraper](https://github.com/data-scrape/youtube-channel-scraper) - YouTube channel scraper - extract channel data, videos, subscribers
- [Scrape Youtube Comments](https://github.com/data-scrape/scrape-youtube-comments) - Scrape YouTube comments - extract comments from any video
- [Scrape Youtube Search Results](https://github.com/data-scrape/scrape-youtube-search-results) - Scrape YouTube search results - extract videos, channels, playlists
- [Youtube Video Scraper Api](https://github.com/data-scrape/youtube-video-scraper-api) - YouTube video scraper API - REST API for video data extraction

### Facebook Scrapers

- [Best Facebook Scraper](https://github.com/data-scrape/best-facebook-scraper) - Best Facebook scraper 2025 - extract pages, posts, and reviews
- [Facebook Profile Scraper](https://github.com/data-scrape/facebook-profile-scraper) - Facebook profile scraper - extract profiles, friends, photos, posts
- [Facebook Group Scraper](https://github.com/data-scrape/facebook-group-scraper) - Facebook group scraper - extract group posts, members, discussions
- [Facebook Scrape Website](https://github.com/data-scrape/facebook-scrape-website) - Facebook scrape website - full Facebook data extraction toolkit
- [Facebook Page Scraper](https://github.com/data-scrape/facebook-page-scraper) - Facebook page scraper - extract page posts, reviews, insights
- [Facebook Post Scraper](https://github.com/data-scrape/facebook-post-scraper) - Facebook post scraper - extract post data, reactions, comments

### TikTok Scrapers

- [Best Tiktok Scraper](https://github.com/data-scrape/best-tiktok-scraper) - Best TikTok scraper 2025 - extract videos, profiles, hashtags
- [Apify Tiktok Scraper](https://github.com/data-scrape/apify-tiktok-scraper) - Apify TikTok scraper alternative - free Python TikTok scraper
- [Tiktok Comment Scraper](https://github.com/data-scrape/tiktok-comment-scraper) - TikTok comment scraper - extract comments from TikTok videos
- [Tiktok Video Scraper](https://github.com/data-scrape/tiktok-video-scraper) - TikTok video scraper - extract video data, hashtags, trending content
- [Tiktok Comments Scraper](https://github.com/data-scrape/tiktok-comments-scraper) - TikTok comments scraper - bulk extract comments and replies
- [Tiktok Data Scraper Api](https://github.com/data-scrape/tiktok-data-scraper-api) - TikTok data scraper API - REST API for TikTok data extraction
- [Tiktok Profile Scraper](https://github.com/data-scrape/tiktok-profile-scraper) - TikTok profile scraper - extract profiles, followers, video stats

### eBay & E-commerce Scrapers

- [Best Ebay Scraper](https://github.com/data-scrape/best-ebay-scraper) - Best eBay scraper 2025 - extract product listings and seller data
- [Ebay Web Scraper](https://github.com/data-scrape/ebay-web-scraper) - eBay web scraper - extract product listings, prices, seller data
- [Ebay Price Scraper](https://github.com/data-scrape/ebay-price-scraper) - eBay price scraper - track prices and extract sold item history
- [Scrap Gold Ebay](https://github.com/data-scrape/scrap-gold-ebay) - Scrap gold eBay - extract gold and precious metal listings
- [Best Walmart Scraper](https://github.com/data-scrape/best-walmart-scraper) - Best Walmart scraper 2025 - extract product data and reviews
- [Best Zillow Scraper](https://github.com/data-scrape/best-zillow-scraper) - Best Zillow scraper 2025 - extract property listings and agent data

### Search & Job Scrapers

- [Best Google Search Scraper](https://github.com/data-scrape/best-google-search-scraper) - Best Google Search scraper 2025 - extract search results in bulk
- [Best Indeed Scraper](https://github.com/data-scrape/best-indeed-scraper) - Best Indeed scraper 2025 - extract job listings and company data

### Social & Other

- [Best Reddit Scraper](https://github.com/data-scrape/best-reddit-scraper) - Best Reddit scraper 2025 - extract posts, comments, user data

### Scraping Platforms & Lists

- [Best Apify Alternative](https://github.com/data-scrape/best-apify-alternative) - Best Apify alternative 2025 - free web scraping platform
- [Awesome Apify Alternatives](https://github.com/data-scrape/awesome-apify-alternatives) - Awesome Apify alternatives - curated list of web scraping tools
- [Awesome Lead Generation](https://github.com/data-scrape/awesome-lead-generation) - Awesome lead generation tools - curated list of scrapers and extractors

---

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
