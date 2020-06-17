from flask import Flask #Importando flask

app = Flask(__name__) #Haciendo instancia

@app.route('/')
def index():
	return 'Hola Mundo'

app.run() #Ejecutando