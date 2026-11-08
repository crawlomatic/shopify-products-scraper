# Shopify Products & Store Scraper | E-Commerce Catalog API

[![Apify Store](https://img.shields.io/badge/Apify%20Store-View%20Actor-brightgreen?logo=apify)](https://apify.com/misterkhan/shopify-products-scraper)
[![GitHub stars](https://img.shields.io/github/stars/crawlomatic/shopify-products-scraper?style=social)](https://github.com/crawlomatic/shopify-products-scraper)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python SDK](https://img.shields.io/badge/SDK-Python-3776AB?logo=python&logoColor=white)](https://github.com/apify/apify-client-python)
[![Node.js SDK](https://img.shields.io/badge/SDK-Node.js-339933?logo=node.js&logoColor=white)](https://github.com/apify/apify-client-js)

> Extract complete product catalogs, prices, variants, images, and inventory data from any Shopify storefront in seconds.

---

## ⚡ Quick Start

You can run this scraper directly via the **[Apify Store Web Console](https://apify.com/misterkhan/shopify-products-scraper)** with zero setup, or integrate it into your Python / Node.js backend using the code below.

### 🐍 Python Quickstart

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
# Get your token from https://console.apify.com/account/integrations
client = ApifyClient("YOUR_APIFY_TOKEN")

# Configure input parameters
run_input = {
  "startUrls": [
    {
      "url": "https://gymshark.com"
    }
  ],
  "maxItems": 50
}

print("🚀 Launching Shopify Products & Store Scraper | E-Commerce Catalog API on Crawlomatic Engine...")
run = client.actor("misterkhan/shopify-products-scraper").call(run_input=run_input)

# Fetch results from the Actor's default dataset
dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items
print(f"✅ Successfully fetched {len(dataset_items)} records!")

for item in dataset_items[:3]:
    print(item)
```

---

### 🟢 Node.js / JavaScript Quickstart

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your API token
const client = new ApifyClient({
    token: 'YOUR_APIFY_TOKEN',
});

// Configure input parameters
const input = {
  "startUrls": [
    {
      "url": "https://gymshark.com"
    }
  ],
  "maxItems": 50
};

console.log('🚀 Launching Shopify Products & Store Scraper | E-Commerce Catalog API...');
const run = await client.actor('misterkhan/shopify-products-scraper').call(input);

// Fetch results
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`✅ Extracted ${items.length} records!`);
console.dir(items.slice(0, 3));
```

---

## What does Shopify Store Products Scraper do?

Shopify Store Products Scraper is an e-commerce catalog extraction tool that scrapes complete product feeds from **any Shopify or Shopify Plus online store**—capturing product titles, active prices, compare-at prices, SKU codes, size/color variants, stock availability, vendor names, tags, and high-resolution product images.

Whether you are monitoring competitor DTC pricing and seasonal markdowns, exporting supplier catalogs for dropshipping and wholesale research, or building structured product feeds for AI shopping assistants, this scraper extracts clean catalog records from any store root domain, /collections/ URL, or /products/ URL.

> 🛡️ **Zero Proxy Configuration Required:** Anti-blocking and regional routing are **handled automatically out of the box** — just paste your target URLs and click **Start**.

## What data can you extract with Shopify Store Products Scraper?

**🏷️ Product Identity & Brand** — unique Shopify product `id`, `title`, `vendor` / brand name, and `product_type` category <br>
**💵 Active Price & Compare-at Price** — current selling `price` and original pre-discount `compare_at_price` for instant markdown calculation <br>
**📦 Variants, SKUs & Stock Availability** — primary sku code, `variants_count` (sizes, colors, materials), and boolean `available` stock status <br>
**🏷️ Merchandising Tags & Metadata** — full tags array used by the merchant for collections, seasons, and filtering <br>
**🖼️ High-Resolution CDN Media & Links** — primary Shopify CDN product `image` URL and canonical product page `url` <br>

## Why scrape product catalogs from Shopify stores?

**💪 Track competitor DTC pricing and promotions in real time** — detect flash sales, compare-at price markdowns, and new product drops across rival Shopify brands <br>
**🕵️ Audit stock availability and SKU breadth** — monitor which product variants (available: true vs. false) are selling out across any DTC vertical <br>
**✨ Build clean wholesale, affiliate, or AI shopping feeds** — export normalized product titles, images, SKUs, and URLs ready for Google Merchant Center, Shopify CSV import, or vector search <br>
**👍 Works on custom domains and /collections/ URLs** — pass either a root domain (`https://allbirds.com`) or a specific collection link to scope your extraction <br>
**📩 Automate catalog syncs via API or webhooks** — connect recurring runs directly to Google Sheets, Airtable, BigQuery, Make, or n8n <br>

## How do I use Shopify Store Products Scraper?

Shopify Store Products Scraper is designed for fast, zero-setup operation in Apify Console:

1. Click **Try for free** on the Actor page to open Apify Console.
2. Paste one or more Shopify store root domains or collection URLs into **Start URLs** (for example, `https://allbirds.com`).
3. Set **Max Results** (`maxItems`) to control how many products to extract.
4. Click **Start** to launch the catalog extraction run.
5. Download your product catalog from the **Dataset** tab in Excel, CSV, JSON, or HTML table format.

## Input

Shopify Store Products Scraper accepts a simple 2-parameter JSON configuration. Click on the [Input tab](https://apify.com/misterkhan/shopify-products-scraper/input-schema) for the interactive form.

```json
{
  "startUrls": [
    {
      "url": "https://allbirds.com"
    }
  ],
  "maxItems": 50
}
```

**🛍️ `startUrls`** — array of Shopify store root URLs, collection URLs (/collections/...), or individual product URLs (e.g., `https://allbirds.com`) <br>
**🔢 `maxItems`** — maximum number of store products to collect per run (default: 50; Free plan runs collect up to 50 products per run, while paid Apify plans support unlimited full-catalog runs) <br>

## Output sample

Results are streamed in real time to your default Apify Dataset. Each record represents a normalized Shopify product with pricing, SKU, availability, and CDN image links:

```json
[
  {
    "id": 78291048204,
    "title": "Men's Tree Runners",
    "vendor": "Allbirds",
    "product_type": "Shoes",
    "price": "98.00",
    "compare_at_price": "110.00",
    "available": true,
    "sku": "TR1MJBK080",
    "variants_count": 14,
    "tags": [
      "mens",
      "running",
      "breathable"
    ],
    "image": "https://cdn.shopify.com/s/files/1/1104/4168/products/Tree_Runner_Jet_Black.png",
    "url": "https://allbirds.com/products/mens-tree-runners"
  }
]
```

## How much does it cost to scrape Shopify products?

Shopify Store Products Scraper uses **Pay-Per-Event (PPE)** pricing (apify-default-dataset-item) with a `$0.00` startup fee—you only pay for products delivered to your dataset:

**🆓 Free plan** — `$0.005` per product ($5.00 / 1,000 products, up to 50 products/run) <br>
**🥉 Starter (Bronze) plan** — `$0.0009` per product ($0.90 / 1,000 products) <br>
**🥈 Scale (Silver) plan** — `$0.00065` per product ($0.65 / 1,000 products) <br>
**🥇 Business+ (Gold) plan** — `$0.0004` per product ($0.40 / 1,000 products) <br>

With the monthly free credit on the Apify Free plan, you can extract **up to 1,000 Shopify products per month for free**.

> 💡 **Predictable, All-Inclusive Pay-Per-Event Pricing:** There is a **`$0.00` run start fee** and **no separate proxy configuration required**. You only pay the flat per-result rate above for data successfully delivered to your dataset — works out of the box on both **Free** and **Paid** Apify plans.

## How many results can you scrape with Shopify Store Products Scraper?

Shopify Store Products Scraper can extract **thousands of products per store** on paid Apify plans (up to 50 products per run on the Free plan). Keep these tips in mind when scraping DTC catalogs:

- **Verify whether a domain runs on Shopify** — this Actor is purpose-built for stores powered by Shopify or Shopify Plus. If you have a mixed list of unknown e-commerce domains and want to detect which ones run on Shopify (alongside Klaviyo, Meta Pixel, and verified store contacts), run them through our [Website Tech Stack, Contacts & AI Markdown Scanner](https://apify.com/misterkhan/website-tech-stack-scanner) first.
- **Full Store vs. Specific Collection URLs** — passing a root domain (e.g., `https://allbirds.com`) extracts products across the entire store catalog, whereas passing a /collections/mens-shoes URL scopes extraction to that specific collection.
- **Multi-store batching** — you can pass dozens of Shopify store URLs in `startUrls` to harvest multiple competitor catalogs in a single run.

## Want to verify Shopify stores, spy on DTC Meta Ads, or enrich store contacts?

Combine Shopify Store Products Scraper with our companion e-commerce and DTC intelligence Actors:

🛠️ **[Website Tech Stack, Contacts & AI Markdown Scanner](https://apify.com/misterkhan/website-tech-stack-scanner)** — detect Shopify, Shopify Plus, Klaviyo, Meta/TikTok pixels, and business emails across any list of domains <br>
📢 **[Facebook Ads Library Scraper](https://apify.com/misterkhan/facebook-ads-library-scraper)** — spy on any Shopify brand's active Meta Ads, video creatives, landing page URLs, and ad longevity <br>
📸 **[Instagram All-in-One Scraper](https://apify.com/misterkhan/instagram-all-in-one-scraper)** — extract DTC brand Instagram profiles, Reel play counts, engagement rates, and bio-link contacts <br>
⭐ **[Trustpilot Reviews Scraper](https://apify.com/misterkhan/trustpilot-reviews-scraper)** — analyze verified customer reviews and star ratings for any online store <br>

## Integrations and Shopify Store Products Scraper

Shopify Store Products Scraper integrates directly with your merchandising spreadsheets, BI warehouses, and automation tools via [Apify integrations](https://apify.com/integrations):

- **No-Code Automation** — trigger price-drop alerts and catalog syncs via Make, Zapier, n8n, or Airbyte.
- **Spreadsheets & Databases** — export product catalogs straight into Google Sheets, Airtable, BigQuery, Snowflake, or PostgreSQL.
- **Webhooks** — notify your pricing engine via HTTP webhook as soon as a catalog crawl finishes.

## Using Shopify Store Products Scraper with the Apify API

You can launch catalog runs and fetch product items programmatically using the official `apify-client` SDKs for **Node.js** and **Python**, or connect this Actor to AI shopping and merchandising agents via the **Apify MCP Server** (`https://mcp.apify.com`).

Check the [API tab](https://apify.com/misterkhan/shopify-products-scraper/api) for ready-to-copy Node.js, Python, and cURL examples.

## Frequently asked questions about Shopify Store Products Scraper

**🛍️ Do I need a .myshopify.com URL, or can I use the brand's custom domain? <br>**
You can use any custom store domain (such as `https://allbirds.com` or `https://gymshark.com`) as well as .myshopify.com subdomains—the scraper resolves the underlying Shopify catalog automatically.

**📦 Does the scraper capture discounted items and original prices? <br>**
Yes. Whenever a product is on sale, `price` shows the active selling price and `compare_at_price` shows the original pre-discount price so you can calculate exact discount percentages.

**🛡️ Do I need to configure proxies or Shopify API keys? <br>**
**No — everything works out of the box with zero setup.** Regional routing, session management, and anti-blocking are handled automatically so you do not need to configure custom proxy settings.

## Is it legal to scrape public Shopify product catalogs?

Our scrapers are ethical and only extract publicly available product catalog information (titles, prices, SKUs, availability, and product images) displayed to shoppers on public online stores. They do not access private merchant admin data or customer orders. For more details on the legality of web scraping, read Apify's guide on [is web scraping legal](https://blog.apify.com/is-web-scraping-legal/).

## Your feedback

We keep this Actor under active maintenance. If a run finishes successfully but returns fewer results than you expected, hangs, or errors — please **open an Issue before posting a public review** so we can diagnose and fix it for you.

**🛠️ How to report** — Use the Actor’s [Issues tab](https://apify.com/misterkhan/shopify-products-scraper/issues/open) in Apify Console. Include the run ID, your input JSON, and what you expected vs. what you got. <br>
**⏱️ Response time** — We aim to reply within 24 hours on business days. <br>
**⭐ Reviews** — Happy with the results? A short positive review helps other users find a reliable scraper. Ran into a problem? Open an Issue first — we’ll work with you to resolve it before you leave a rating. <br>


---

## 🛡️ Architecture & Engine Reliability

This scraper runs on the **[Crawlomatic Engine](https://crawlomatic.com)**:
- **Zero Proxy Configuration:** Intelligent residential and datacenter proxy rotation with automated regional ccTLD binding.
- **WAF Bypass Engine:** Autonomous challenge solving for Cloudflare Turnstile, DataDome, PerimeterX, Kasada, and Akamai.
- **Pay-Per-Event (PPE) Pricing:** Transparent pay-as-you-go pricing with \$0 starting fee.

## 📄 License

Apache License 2.0. See [LICENSE](LICENSE) for details.

Developed & Maintained by **[Crawlomatic](https://crawlomatic.com)**.
