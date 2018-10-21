from typing import List

import requests
from bs4 import BeautifulSoup
from flask import jsonify
from flask_restful import Resource


class RecallRecord():
    def __init__(self, company: str, url: str, summary: str):
        self.company = company
        self.url = url
        self.summary = summary

    def serializeJson(self):
        return {
            'company': self.company,
            'url': self.url,
            'summary': self.summary
        }


class Recall(Resource):
    def get(self, company: str) -> object:
        return jsonify([obj.serializeJson() for obj in self.searchRecall(company)])

    def searchRecall(self, company: str) -> List[RecallRecord]:
        result = requests.get(
            "https://search-recherche.gc.ca/rGs/s_r?as_q=" + company + "&st=a&num=10&st1rt=0&langs=eng&cdn=aciacfia&s5bm3ts21rch=x&hq=&as_qdr=all&1s_s3t2s21rch=www.inspection.gc.ca%2Fabout-the-cfia%2Fnewsroom%2Ffood-recall-warnings&as_occt=%23wb-land&bsubmit=Search#wb-land")
        soup = BeautifulSoup(result.text, "html.parser")

        a = soup.find("div", class_="result row").find_all("section")
        res: List[RecallRecord] = []

        for _ in a[1:]:
            summary = soup.find('div', class_='result row').section.h3.text
            url = soup.find('div', class_='result row').section.h3.a['href']
            res.append(RecallRecord(company, url, summary))

        return res
