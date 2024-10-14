import requests
from fp.fp import FreeProxy
from requests.exceptions import RequestException, Timeout, ProxyError, ConnectionError
from html_reducer import cleanup_html, reduce_html  # Import the parsing function
from scraper import scrape_website  # Import the scraping function from scrape.py
from ai_scraper import ai_scraper
import asyncio



async def main():
  # call the ai_scraper function
  search_url = "https://sneakers-adda-v2.vercel.app/sneakers/Jordan%201"
  user_question = "What are the top 5 job titles and their respective companies?"
  gpt_model = "gpt-3.5-turbo"
  openai_api_key = "your_openai_api_key_here"
  schema_instructions = "json"  
  parser_logic = ai_scraper(search_url, user_question, gpt_model, openai_api_key, schema_instructions);
  print(parser_logic)
  #save to file
  with open('parser_logic.txt', 'w') as file:
    file.write(parser_logic)

if __name__ == "__main__":
    asyncio.run(main())
