from typing import List
import json

from bs4 import BeautifulSoup
import pandas as pd
import requests

RECALL_BASE_URL = 'http://www.inspection.gc.ca/about-the-cfia/newsroom/food-recall-warnings/complete-listing/eng'
RECALL_2018_URL = RECALL_BASE_URL + '/1351519587174/1351519588221?ay=2018&fr=0&fc=0&fd=0&ft=1'
r = requests.get(RECALL_2018_URL)
# BeautifulSoup.find()
recall_df: List[pd.DataFrame] = pd.read_html(r.content)

recalls_json: List[dict] = [recall.to_dict(orient='records') for recall in recall_df]

with open('recall_2018.json', 'w') as f:
    f.write(json.dumps({'recalls': recalls_json}))