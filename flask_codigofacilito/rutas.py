from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo'

@app.route('/params')
def params():
	param = request.args.get('params1', 'no contiene este parametro')
	return 'El parametro es: {}'.format(param)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)