from html_reducer import cleanup_html, reduce_html
from html_parser import generate_parser_logic
from scraper import scrape_website
from requests.exceptions import Timeout, ProxyError, ConnectionError, RequestException

async def ai_scraper(url, user_question, gpt_model, openai_api_key, schema_instructions):
    try:
        print("Attempting direct scraping with Playwright at local...")
        response = await scrape_website(url, False)
        if response[1] == 200:
            cleaned_html = cleanup_html(response[0], url)
            reduced_html = reduce_html(cleaned_html, 2)
            print("Reduced HTML:", reduced_html)
            return  # Exit if scraping via Playwright is successful
    except Exception as e:
        print(f"Initial headless scraping failed: {e}")
    
    # If Playwright scraping fails, try with proxiesx
    print("Attempting scraping with proxies...")
    max_retries = 5
    for attempt in range(max_retries):
        try:
            # Perform the request using the proxy
            response = await scrape_website(url, True)
            # Check if the request was successful
            if response[1] == 200:    
                # Parse the HTML content
                cleaned_html = cleanup_html(response[0], url)
                reduced_html = reduce_html(cleaned_html, 2)

                print("Reduced HTML:", reduced_html)
                break
            else:
                print(f"Received unexpected status code: {response[1]}")

        except (Timeout, ProxyError, ConnectionError) as e:
            print(f"Network-related error occurred: {e}")
        except RequestException as e:
            print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # If we've exhausted all retries
        if attempt == max_retries - 1:
            print("Max retries reached. Unable to get a successful response.")

    

   

    # Generate parser logic
    parser_logic = generate_parser_logic(gpt_model, reduced_html, user_question, url, schema_instructions)

    # For now, we'll just return the parser_logic as a string
    return parser_logic
