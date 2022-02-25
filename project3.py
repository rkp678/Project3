# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:12:46 2022

@author: Margee
"""

# Initial imports
import os
import pandas as pd
from dotenv import load_dotenv
from newsapi import NewsApiClient
from pathlib import Path

# For Sentiment Analysis
import nltk as nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# For Tokenizing
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from string import punctuation
import re

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

home = Path.home() / ".env"  # windows 1/2
load_dotenv(home)  # windows 2/2

api_key = os.getenv("NEWS_API")

# Create a newsapi client
newsapi = NewsApiClient(api_key=api_key)

# Part 1
# Fetch the cryptocurrency news articles
crypto_news = newsapi.get_everything(
    q="cryptocurrency",
    language="en"
)
#%%
# export text to txt file for later use in AWS Comprehend
data = crypto_news["articles"]

all_content = []

for i in data:
    print(i["content"])
    all_content.append(i["content"])
    
filename = 'project3crypto.txt'
file_write = "C:/Users/Margee/working_class_uofm/Project3/project3crypto.txt"

with open(file_write, 'w') as f:
    f.write(f"{all_content}\n")
    for item in all_content.append(i["content"]):
        f.write(item+"\n")
#%%

# Part 2
# Fetch the open banking news articles
openbanking_news = newsapi.get_everything(
    q="open banking",
    language="en"
)

data2 = openbanking_news["articles"]

all_content = []

for i in data2:
    print(i["content"])
    all_content.append(i["content"])
    
filename = 'project3openbanking.txt'
file_write = "C:/Users/Margee/working_class_uofm/Project3/project3openbanking.txt"

with open(file_write, 'w') as f:
    f.write(f"{all_content}\n")
    for item in all_content.append(i["content"]):
        f.write(item+"\n")
#%%

# Part 2
# Fetch the open banking news articles
banking_news = newsapi.get_everything(
    q="banking",
    language="en"
)

data3 = banking_news["articles"]

all_content = []

for i in data3:
    print(i["content"])
    all_content.append(i["content"])
       
filename = 'project3banking.txt'
file_write = "C:/Users/Margee/working_class_uofm/Project3/project3banking.txt"

with open(file_write, 'w') as f:
    f.write(f"{all_content}\n")
    for item in all_content.append(i["content"]):
        f.write(item+"\n")     