import re

from flask import jsonify
from flask_restful import Resource
from pymongo.collection import Collection

class Details(Resource):
    def __init__(self):
        from app import database
        self.collection: Collection = database["details"]

    def get(self, company: str) -> object:
        regex = re.compile('^.*{}.*$'.format(company), re.IGNORECASE)
        return jsonify(self.collection.find_one({'name': regex},
                                                {'_id': False}))