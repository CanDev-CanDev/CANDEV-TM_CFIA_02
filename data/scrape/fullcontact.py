import json
import pandas as pd
import requests

from config import FULLCONTACT_KEY

df = pd.read_csv('domains.csv')
domains = list(df['Domain name'][7:])

infos = []

for domain in domains:
    r = requests.post('https://api.fullcontact.com/v3/company.enrich',
                      headers={'Authorization': 'Bearer ' + FULLCONTACT_KEY},
                      data=json.dumps({'domain': domain}))
    infos.append(json.loads(r.content))

with open('domains.json', 'a') as f:
    json.dump(infos, f)