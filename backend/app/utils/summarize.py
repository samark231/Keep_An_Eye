# from transformers import pipeline
# from preprocess import preprocess_content
# # Load summarization models
# t5_summarizer = pipeline("summarization", model="t5-small")
# bart_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# pegasus_summarizer = pipeline("summarization", model="google/pegasus-xsum")

# def summarize_text(text, model="t5"):
#     """
#     Summarizes a given text using the specified model.
    
#     Parameters:
#         text (str): The input text to summarize.
#         model (str): The summarization model to use. Options: 't5', 'bart', 'pegasus'
    
#     Returns:
#         str: Summarized text
#     """
#     if model == "t5":
#         summary = t5_summarizer(text, max_length=1000, min_length=500, do_sample=False)
#     elif model == "bart":
#         summary = bart_summarizer(text, max_length=150, min_length=50, do_sample=False)
#     elif model == "pegasus":
#         summary = pegasus_summarizer(text, max_length=150, min_length=50, do_sample=False)
#     else:
#         raise ValueError("Invalid model name. Choose from 't5', 'bart', or 'pegasus'.")
    
#     return summary[0]['summary_text']

# article = {
# 		"id": 10,
# 		"link": "https://www.moneycontrol.com/technology/apple-iphone-17-pro-rumour-roundup-every-big-and-small-changes-expected-from-the-next-most-expensive-iphone-article-12971488.html",
# 		"source": "Moneycontrol",
# 		"title": "Apple iPhone 17 Pro rumour roundup: Every big and small change expected from the next most expensive...",
# 		"summary": "Apple iPhone 17 Pro Max is expected to arrive later this year alongside other iPhone models. Here's everything we know so far.",
# 		"content": "See the top gainers, losers, invest and get updated what's happening in the crypto market\nIndia's Largest Regional Retail Option Traders Summit. (BOTS) is a prestigious options trading event organized by Traders Gurukul. Held on the 2nd OR 3rd Sunday of every month, across top cities in India\nThis functionality will provide users with ease of access navigation and enable create a new revenue line by generating leads of potential customers for brokers in a more integrated manner.\nApple is still several months away from launching its latest iPhone 17 series. But that hasn\u2019t stopped the leaks from posting details about the upcoming iPhone models. Leaks and rumours have already provided insights into the possible design, display, and camera upgrades.\nExpected to debut in September 2025, the iPhone 17 Pro Max is likely to bring significant changes, including a new camera layout, an upgraded processor, and improved battery technology.\nSimilar camera setup with quality improvements\nOne of the most notable changes in the iPhone 17 Pro Max is expected to be in the camera module. Reports suggest a shift from the square camera bump seen in previous models to a horizontal or elongated oval-shaped layout. The device may feature three 48-megapixel sensors for wide, ultra-wide, and telephoto cameras. Additionally, Apple is rumoured to introduce a mechanical aperture for the wide camera, allowing for better control over lighting and depth of field.\nThe front camera could also receive an upgrade, increasing from 12-megapixel to 24-megapixel for improved selfies and video calls. Apple aims to enhance the device\u2019s imaging capabilities to appeal to professional content creators.\nDisplay and design changesThe iPhone 17 Pro Max is expected to retain its 6.9-inch display size but with improved durability. Reports indicate the use of a new \"super-hard\" anti-reflective layer on the front glass. Apple may also introduce a smaller Dynamic Island, integrating the TrueDepth camera more efficiently.\nOn the design front, Apple is reportedly moving away from the titanium frame used in the iPhone 15 Pro series and returning to an aluminium frame, aligning with its environmental sustainability goals. The back panel could adopt a combination of glass and aluminium, with the top portion made of metal for added strength.\nPerformance and battery improvementsUnder the hood, the iPhone 17 Pro Max is expected to be powered by Apple\u2019s A19 Pro chip, built on a 3nm process, offering improved performance and efficiency. The device is also rumoured to come with 12GB of RAM, up from 8GB in its predecessor.\nTo manage heat, Apple may introduce a vapour chamber cooling system, a feature often found in high-performance gaming devices. Additionally, the phone could be slightly thicker than previous models, potentially accommodating a larger battery. A 7.5W reverse wireless charging feature may also be introduced, allowing users to charge smaller accessories like AirPods and the Apple Watch wirelessly.\nConnectivity and other upgradesThe iPhone 17 Pro Max is expected to support Wi-Fi 7, promising faster internet speeds and improved efficiency. Apple is also working on a custom Wi-Fi chip for better connectivity. Bluetooth 5.3 is likely to be included as well.\nPossible name changeThere is speculation that Apple might rebrand the iPhone 17 Pro Max as the \"iPhone 17 Ultra,\" marking a shift in its naming strategy. If true, the Ultra model could feature exclusive hardware enhancements, making it the most premium offering in the lineup.\nDiscover the latestBusiness News,Budget 2025 News,Sensex, andNiftyupdates. ObtainPersonal Financeinsights, tax queries, and expert opinions onMoneycontrolor download theMoneycontrol Appto stay updated!\nIPL 2025 Opening CeremonyIT StocksNSE F&O StocksKKR vs RCBBajaj Finance Share PriceIPL Schedule 2025Gold PriceKarnataka BandhSCTEVT Diploma ResultIPL 2025\nBusinessMarketsStocksIndia NewsCity NewsEconomyMutual FundsPersonal FinanceIPO NewsStartups\nHomeCurrenciesCommoditiesPre-MarketIPOGlobal MarketBonds\nHomeLoans up to 50 LakhsCredit Cards Lifetime FreeFinance TrackerNewFixed DepositsNewFixed Income\nHomeMC 30Top Ranked FundsETFsMutual Fund Screener\nIncome Tax CalculatorEMI CalculatorRetirement PlanningGratuity Calculator\nNews18FirstpostCNBC TV18News18 HindiCricketnextOverdriveTopper Learning\nAbout UsContact UsAdvisory AlertAdvertise with UsSupportDisclaimerPrivacy PolicyCookie PolicyTerms & ConditionsFinancial Terms (Glossary)SitemapInvestors\nCopyright \u00a9 Network18 Media & Investments Limited. All rights reserved. Reproduction of news articles, photos, videos or any other content in whole or in part in any form or medium without express written permission of moneycontrol.com is prohibited.\nYou are already a Moneycontrol Pro user."
# 	}
# news_article = preprocess_content(article["content"])
# # Example News Article

# # Generate Summaries using all three models
# with open("../data/t5.txt", "w") as f1:
#     t5_summary = summarize_text(news_article, model="t5")
#     f1.write(t5_summary)
# # with open("bart.txt", "w") as f2:
# #     bart_summary = summarize_text(news_article, model="bart")
# #     f2.write(bart_summary)
# # with open("pegasus.txt", "w") as f3:
# #     pegasus_summary = summarize_text(news_article, model="pegasus")
# #     f3.write(pegasus_summary)

