from flask import jsonify
from flask_restful import Resource
from pymongo.collection import Collection

class News(Resource):
    def __init__(self):
        from app import database
        self.collection: Collection = database["news"]

    def get(self, company: str) -> object:
        return jsonify([news for news in self.collection.find({'company': company},
                                                              {'_id': False})])

