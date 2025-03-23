import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import os
import sys
import re
from pprint import pprint
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))
sys.path.append(main_dir)
curated_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "curated_data.json"))


# this funtion take name of company as argument and it searches the google news. and the search excludes some sites like deccan herald, bloomberg beacuase they load js-heavy pages and youtube links are not text based so scraping those are worthless.

def google_search_page(company):
    search_url = f"https://www.google.com/search?q={company}+news+english+-site:bloomberg.com+-site:deccanherald.com+-site:youtube.com+-site:x.com&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"} #setting headers so that google doesnt flag this search as something robotic
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        return response.text, None
    except Exception as e:
        print(f"Error occured in google_search_page function: {e}")
        return None, str(e)

#this function takes two beautifulsoup objects as input. but what are these two objects? whenever you search google there is old fahsioned list of of news links and then there are news links grouped together like cards on top and both have different class names as so both needs to be scraped differently. 

#headings1 represnt the normal oldfasioned list style newses
# in headings1 actuallu an array of those articles. there are many divs. each div reprents a news articles.  each div has anchor tag conataing link to original website where the article is posted 
#headings2 represnt card style news.
def extract_information(headings1, headings2):
    print("inside extract_information")
    news_list =[]
    i = 1
    for head in headings1:
        mp={}
        mp["id"]= i
        anchor = head.find("a") #link to originall article
        if anchor and anchor.has_attr("href"):
            mp["link"] = anchor["href"]
        source = head.find("span") #news source of the article 
        if source:
            mp["source"]= source.get_text(strip=True)  
        title = head.find("div", attrs={"role":"heading"})
        if title:
            mp["title"]=title.get_text(strip=True)  #title of the article
        summary = head.find("div", class_ ="GI74Re") #the short summary that appears on the google page.
        if summary:
            mp["summary"]=summary.get_text(strip=True)
        news_list.append(mp)
        i=i+1
    if i<=10:  #sometimes there are very few list style news and lots of card style news. if there are less than 10 list style news then we search for card style news and append them into our list of news articles .
        for head in headings2:
            anchors = head.find_all("a") #links 
            for anchor in anchors:
                mp={}
                mp["id"]= i
                if anchor and anchor.has_attr("href"):
                    mp["link"] = anchor["href"]
                    source = anchor.find("span") #source
                    if source:
                        mp["source"]= source.get_text(strip=True)
                    title = anchor.find("div", attrs={"role":"heading"}) #title
                    if title:
                        mp["title"]=title.get_text(strip=True)
                summary = "no summary available"
                mp["summary"]=summary #summary
                news_list.append(mp)
                i=i+1
    return news_list

#this function takes the news link and fetches the content of the article from the page. so by observing the pages or articles i found that most websites use p tag to write the paragraphs of elements of their article so we basically scrape all the p tags and remove the tags containing some stop words like advertisement and follow us etc. 

def fetch_news_content(url):
    print("inside fetch_news_contnet")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"Error occured in google_search_page function: {e}")
        return []
    # pprint(soup)
    list_of_para = soup.find_all("p")
    # print(list_of_para)
    content =[]
    for para in list_of_para:
        text = para.get_text(strip=True)
        # print(text)
        if(len(text)>15):
            content.append(text)
    # print(len(content))
    whole_para = " ".join(content)
    return whole_para

def add_content(all_articles):
    print("inside add content")
    for article in all_articles:  
        content = fetch_news_content(article["link"])
        # print(type(content))
        # reg ex to remove the unicodes. some news articles had hindi words and got converted into unicodes while scraping so below two lines removes them.
        pattern = r"\S*\\u\S*"
        cleaned_text = re.sub(pattern, " ", content)
        article["content"]=cleaned_text

def curate_ultimate_data(ultimate_data, company):
    curated_data = {}
    curated_data["Company"]= company
    articles =[]
    sentiment_score = {"positive":0, "negative":0, "neutral":0}
    coverage_diff = []
    topic_overlap = {}
    topic_overlap["Common Topics"] = ultimate_data[1]
    for article_data in ultimate_data[0]:
        temp ={}
        comp_temp ={}
        id = article_data["id"]
        temp_str = f"Unique Topics in Article {id}"

        temp["Source"] = article_data["source"]
        temp["Title"]=article_data["title"]
        temp["Link"] = article_data["link"]
        temp["Summary"]=article_data["content_summary"]
        sentiment = article_data["sentiment_val"]
        if sentiment not in sentiment_score:
            sentiment_score[sentiment] = 0  # Initialize if missing
        sentiment_score[sentiment] += 1

        sentiment_score[sentiment]+=1
        temp["Sentiment"] = sentiment
        temp["Topics"] = article_data["topic_val"]
        comp_temp["Comparision"]= article_data["comparision_val"]
        comp_temp["Impact"] = article_data["impact_val"]
        topic_overlap[temp_str] = article_data["topic_val"]

        articles.append(temp)
        coverage_diff.append(comp_temp)
        
    curated_data["Articles"]=articles
    temp_comp_sent_score = {"Sentiment Distribution Score":sentiment_score, "Coverage Differences":coverage_diff}
    curated_data["Comparative Sentiment Score"] = temp_comp_sent_score
    curated_data["Final Sentiment Analysis"]=ultimate_data[2]
    # with open(curated_data_path, "w") as file:
    #     file.write(json.dumps(curated_data))
    return curated_data
# url = "https://www.deccanherald.com/technology/how-delhi-capitals-womens-team-used-apple-watch-ultra-2-to-keep-fit-and-improve-performance-3457247"
# print(fetch_news_content(url))
