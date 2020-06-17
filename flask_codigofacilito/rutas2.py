from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo'

@app.route('/params/')
@app.route('/params/<name>/<int:num>')
def params(name = 'este es un valor por default', num = 'nada'):
	
	return 'El parametro encontrado fue: {} {}'.format(name, num)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)