import os
import sys
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))
sys.path.append(main_dir)
from bs4 import BeautifulSoup
import app.utils.news_scraper as helper
import app.utils.sentiment_analysis_api as api
import json
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
all_articles_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "all_articles.json"))
all_articles_with_content_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "all_articles_with_content.json"))
def fetch_curated_data(company):
    print("fetching started...")
    #this function return the google search page for the company as bs4 element
    html_doc, error = helper.google_search_page(company)
    if html_doc is None:
        return None, error
    print("step 1 complete.")
    #the beautifulsoup parses that page so that we can apply the scarping next
    soup = BeautifulSoup(html_doc, "html.parser")

    #now we search for all the divs which has class SoaBEf becase this is the div which contains title, intro and link to the article a particle search result
    each_search_result = soup.find_all("div", class_= "SoaBEf")
    extra_search_result = soup.find_all("g-section-with-header")

    if len(each_search_result)==0 and len(extra_search_result)==0 :
        return None," looks like google has changed the structure of their news page. customise the class name according to new structure."

    #the extract information function extracts information such as news source, link to the main article, title of the aritcle and summary 
    all_articles = helper.extract_information(each_search_result, extra_search_result)

    if all_articles is None:
        return None, "error in extract_information function."
    print("step 2 complete.")
    with open(all_articles_path, "w") as f:
        f.write(json.dumps(all_articles))

    helper.add_content(all_articles)

    print("step 3 complete.")
    with open(all_articles_with_content_path, "w") as f2:
        f2.write(json.dumps(all_articles))

    final_prompt = api.generate_prompt(all_articles)
    print("step 4 complete.")

    ultimate_data, error = api.fetch_response_gemini(final_prompt, api_key)
    if ultimate_data is None:
        return None, error
    print("step 5 complete.")
    

    curated_data = helper.curate_ultimate_data(ultimate_data, company)
    print("step 6 complete.")

    return curated_data, None
# company= "tesla"
# fetch_curated_data(company)