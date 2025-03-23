# import re
# import spacy

# nlp = spacy.load("en_core_web_sm")

# def preprocess_content(text):
#     """Cleans scraped article content by removing ads, unwanted text, and fixing Unicode issues."""

#     # Step 1: Remove unwanted Unicode characters like \u2019
#     text = text.encode("utf-8").decode("unicode_escape")
#     print("step1")
#     # print(text)
#     # Step 2: Define stop phrases (ads, disclaimers, subscriptions)
#     stop_phrases = [
#         "subscribe", "advertisement", "follow us", "watch more", "manage subscription",
#         "sponsored content", "copyright", "author", "disclaimer", "purchase through links",
#         "follow on social media", "terms and conditions"
#     ]
#     print("step2")
#     # Step 3: Remove unwanted paragraphs
#     paragraphs = text.split("\n")
#     print(len(paragraphs))
#     cleaned_paragraphs = []

#     for para in paragraphs:
#         para = para.strip()
        
#         # Remove very short paragraphs (likely noise)
#         if len(para.split()) < 5:
#             continue
        
#         # Skip paragraphs containing unwanted phrases
#         if any(phrase in para.lower() for phrase in stop_phrases):
#             continue

#         cleaned_paragraphs.append(para)

#     cleaned_text = " ".join(cleaned_paragraphs)

#     # Step 4: Use Named Entity Recognition (NER) to extract relevant sentences
#     doc = nlp(cleaned_text)
#     important_sentences = [
#         sent.text for sent in doc.sents 
#         if any(ent.label_ in ["ORG", "PERSON"] for ent in sent.ents)
#     ]

#     return " ".join(important_sentences)

