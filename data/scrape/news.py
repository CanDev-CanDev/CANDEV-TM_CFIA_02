from typing import List

import pandas as pd
from newsapi import NewsApiClient
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from config import NEWSAPI_KEY, MONGO_URI, MONGO_DB


def fetch_news(company: str, outfile: str) -> None:
    info = NewsApiClient(api_key=NEWSAPI_KEY).get_everything(q=company)
    df = pd.DataFrame(info['articles']).drop(['author', 'content', 'urlToImage'], axis=1)
    df.to_csv(outfile)

def fetch_news_companies(names: List[str]) -> None:
    for name in names:
        fetch_news(name, name + '.csv')



##remove all colums except description
avg = 0
for line in b['description'].iterrows():
   analyze = TextBlob(line)
   avg = analyze.sentiment.polarity + avg
avg = avg / i
if avg > 0.2:
   print ("No immediate threat")
else:
   print ("Recently flagged")

if __name__ == '__main__':
    client = MongoClient(MONGO_URI)
    database: Database = client[MONGO_DB]
    collection: Collection = database["company"]
    company_names: List[str] = collection.find_one({}, {'_id': False})['companies']
    fetch_news_companies(company_names)