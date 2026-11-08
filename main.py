"""
Shopify Products & Store Scraper | E-Commerce Catalog API
Official Python client example powered by Crawlomatic Engine on Apify
"""
import os
import sys
from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN")

def main():
    if APIFY_TOKEN == "YOUR_APIFY_TOKEN":
        print("⚠️ Please set your APIFY_TOKEN environment variable or pass your token to ApifyClient.")
        print("Get your token at: https://console.apify.com/account/integrations")
        sys.exit(1)

    client = ApifyClient(APIFY_TOKEN)

    run_input = {
  "startUrls": [
    {
      "url": "https://gymshark.com"
    }
  ],
  "maxItems": 50
}

    print("🚀 Calling misterkhan/shopify-products-scraper...")
    run = client.actor("misterkhan/shopify-products-scraper").call(run_input=run_input)

    dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items
    print(f"✅ Extraction completed! Total items: {len(dataset_items)}")

    for idx, item in enumerate(dataset_items[:5], 1):
        print(f"\n--- Record {idx} ---")
        print(item)

if __name__ == "__main__":
    main()
