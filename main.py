from ai_scraper import ai_scraper
import asyncio
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from the .env file
load_dotenv()

async def main():
  # call the ai_scraper function
  url = input("Enter the URL to scrape: ")
  prompt = input("Enter the prompt: ")
  response_from_ai_scraper = await ai_scraper(
     url, # search_url
     prompt, # user_question
     "gpt-3.5-turbo", # gpt_model
     os.environ.get("OPENAI_API_KEY"), # openai_api_key 
     "json" # schema_instructions
  );
  if not response_from_ai_scraper[1]=="":
    return response_from_ai_scraper[1]
  print("response from ai_scraper... ")
  # first_line = parser_logic.split('\n')[0]
  # last_line = parser_logic.split('\n')[-1]
  #print('first_line: ', first_line, 'last_line: ', last_line)
  # new_str =""
  # if first_line == "'''" and last_line == "'''":
  #     # print("inside of main")
  #     #Split the string into lines and copy everything from the second line onward
  #     lines = parser_logic.splitlines()

  #     # Join lines starting from the second line (index 2)
  #     new_str = "\n".join(lines[1:])

  #     lines = new_str.splitlines()

  #     new_str = "\n".join(lines[:-1])
      
  #     #print(new_str)

  #     exec(new_str)
  #     return
    # code to execute the parser_logic
  # read from parser_logic.py
  with open("parser_logic.py", "w") as file:
    file.write(response_from_ai_scraper[0])
  with open('parser_logic.py', 'r') as file:
      parser_logic = file.read()
  exec(parser_logic)
if __name__ == "__main__":
    asyncio.run(main())