from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Passengers(Resource):
    def get(self):
        return {'message': '讀取所有資料'}, 200
    
    def post(self):
        return {'message': '新增資料'}, 201

class Passenger(Resource):
	def get(self, id ):
		return {'message': f'讀取第{id}筆的資料'}, 200

	def put(self, id ):
		return {'message': f'修改第{id}筆的資料'}, 200

	def delete(self, id ):
		return {'message': f'刪除第{id}筆的資料'}, 200
  
api.add_resource(Passengers, '/api/passengers')
api.add_resource(Passenger, '/api/passenger')

if __name__ =='__main__':
	app.run(debug=True)