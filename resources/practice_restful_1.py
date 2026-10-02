from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/api/passengers')
def get_passengers():
	passengers = [
			{'id':1, 'name': 'Amy'},
			{'id':2, 'name': 'Bob'}
	]
	return jsonify(passengers)

if __name__ =='__main__':
	app.run(debug=True)