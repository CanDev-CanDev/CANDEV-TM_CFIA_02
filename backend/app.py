from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from flask_restful import Api
from pymongo.database import Database

from config import MONGO_URI, MONGO_DB

from company import Companies
from details import Details
from news import News
from recall import Recall

app: Flask = Flask(__name__)
CORS(app)
client = MongoClient(MONGO_URI)
database: Database = client[MONGO_DB]

api = Api(app)
api.add_resource(Companies, '/companies')
api.add_resource(Details, '/details/<string:company>')
api.add_resource(News, '/news/<string:company>')
api.add_resource(Recall, '/recall/<string:company>')

if __name__ == '__main__':
    app.run(debug=True)
