from flask import Blueprint
from flask_restful import Api
from  resources.practice_flaskrestful_1 import Passengers, Passenger

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#設定路由
api.add_resource(Passengers, '/passengers')
api.add_resource(Passenger, '/passengers/<id>')