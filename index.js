/**
 * Shopify Products & Store Scraper | E-Commerce Catalog API
 * Official Node.js client example powered by Crawlomatic Engine on Apify
 */
import { ApifyClient } from 'apify-client';

const APIFY_TOKEN = process.env.APIFY_TOKEN || 'YOUR_APIFY_TOKEN';

async function run() {
    if (APIFY_TOKEN === 'YOUR_APIFY_TOKEN') {
        console.error('⚠️ Please set the APIFY_TOKEN environment variable.');
        console.error('Get your token at: https://console.apify.com/account/integrations');
        process.exit(1);
    }

    const client = new ApifyClient({ token: APIFY_TOKEN });
    const input = {
  "startUrls": [
    {
      "url": "https://gymshark.com"
    }
  ],
  "maxItems": 50
};

    console.log('🚀 Calling misterkhan/shopify-products-scraper...');
    const actorRun = await client.actor('misterkhan/shopify-products-scraper').call(input);

    const { items } = await client.dataset(actorRun.defaultDatasetId).listItems();
    console.log(`✅ Extraction completed! Total items: ${items.length}`);
    console.log(items.slice(0, 3));
}

run().catch(console.error);
