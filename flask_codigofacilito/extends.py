from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = 'Sebastian'
	return render_template('index.html', name = name)

@app.route('/client')
def client():
	list_name = ['Test1', 'Test2', 'Test3']
	return render_template('client.html', list = list_name)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)