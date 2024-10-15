from html_reducer import cleanup_html, reduce_html
from html_parser import generate_parser_logic
from scraper import scrape_website
from requests.exceptions import Timeout, ProxyError, ConnectionError, RequestException
import requests


async def ai_scraper(url, user_question, gpt_model, openai_api_key, schema_instructions):
    reduced_html = ""
    try:
        print("Attempting direct scraping with Playwright at local...")
        response = await scrape_website(url, False)
        # print("response:", response.get("status_code"))
          
        if response.get("status_code") == 200:
            cleaned_html = cleanup_html(response.get("html_content"), url)
            reduced_html = reduce_html(cleaned_html.get("minimized_body"), 2)
            print("Scraping successful with Playwright.")
    except Exception as e:
        print(f"Initial headless scraping failed: {e}")
    
    # If Playwright scraping fails or reduced_html is still empty, try with proxies
    if not reduced_html:
        print("Attempting scraping with proxies...")
        max_retries = 5
        for attempt in range(max_retries):
            try:
                # Perform the request using the proxy
                response = await scrape_website(url, True)
                # Check if the request was successful
                if response.get("status_code") == 200:    
                    # Parse the HTML content
                    cleaned_html = cleanup_html(response.get("html_content"), url)
                    reduced_html = reduce_html(cleaned_html.get("minimized_body"), 2)

                    print("Reduced HTML with proxy:", reduced_html)
                    break
                else:
                    print("Received unexpected status code:", response.get("status_code"))

            except (Timeout, ProxyError, ConnectionError) as e:
                print(f"Network-related error occurred: {e}")
            except RequestException as e:
                print(f"Request failed: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            # If we've exhausted all retries
            if attempt == max_retries - 1:
                print("Max retries reached. Unable to get a successful response.")
    # Generate parser logic even if reduced_html is from Playwright or proxy scraping
    
    parser_logic = generate_parser_logic(gpt_model, {"title": cleaned_html.get("title"), "reduced_html": reduced_html, "link_urls_data": cleaned_html.get("link_urls")}, user_question, url, schema_instructions)
    # For now, we'll just return the parser_logic as a string
    return parser_logic
