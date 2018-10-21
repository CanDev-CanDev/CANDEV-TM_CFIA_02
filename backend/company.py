from flask import jsonify
from flask_restful import Resource
from pymongo.collection import Collection

class Companies(Resource):
    def __init__(self):
        from app import database
        self.collection: Collection = database["company"]

    def get(self) -> object:
        return jsonify(self.collection.find_one({}, {'_id': False})['companies'])

