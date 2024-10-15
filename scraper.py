import asyncio
from playwright.async_api import async_playwright
from typing import Optional, List
from requests.exceptions import RequestException
from fp.fp import FreeProxy
import requests
# Enable proxy settings if needed
def get_proxy() -> Optional[dict]:
    try:
        proxy = FreeProxy(country_id=['US', 'CA', 'IN'], timeout=10, rand=True).get()
        return {'server': proxy}
    except RequestException as e:
        print(f"Error fetching proxy: {e}")
        return None

async def scrape_website(url: str, use_proxy: bool = False) -> List[Optional[str]]:
    """
    Scrapes the provided URL using Playwright and returns the HTML content and status code.
    Supports proxy rotation.
    """
    print(f"Scraping URL: {url}")
    html_content = ""
    status_code = None

    proxy_settings = await get_proxy() if use_proxy else None
    print('Using proxy:', proxy_settings)
    async with async_playwright() as p:
        browser_args = {
            'headless': True,  # Run browser in headless mode
        }

        # Launch the browser with or without proxy
        browser = await p.chromium.launch(**browser_args)
        try:
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                proxy=proxy_settings  # Add proxy settings if applicable
            )
            # Apply stealth settings to avoid detection
            # Add stealth logic similar to 'Malenia.apply_stealth' from chromium.py, if needed
            
            page = await context.new_page()
            response = await page.goto(url, wait_until="domcontentloaded")
            
            # Capture the page content and status code
            html_content = await page.content()
            status_code = response.status if response else None

            print(f"Scraped content from {url}")
            print(f"Status code: {status_code}")

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            status_code = None

        finally:
            await browser.close()
    #print('html_content:', html_content)
    # file_path = 'html_content.html'
    # with open(file_path, 'w', encoding='utf-8') as file:
    #     file.write(html_content)
    
    return {"html_content": html_content, "status_code": status_code}