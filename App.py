from flask import Flask, render_template, request
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nena19##'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysqldb = MySQL(app) #Connecting with MySQL

#Making routes
@app.route('/') #route principal
def Index():
	return render_template('index.html')

#route add_contacts
@app.route('/add_contacts', methods = ['POST']) #Telling the function that can receive POST method
def add():
	if request.method == 'POST': #If the request if a POST method...
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		cur = mysqldb.connection.cursor() #This cursor allows us to do MySQL querys. A cursor allows us to know where's the connection
		return 'received'

#route deleting
@app.route('/delete_contacts')
def delete():
	return 'delete contacts'

#route edit
@app.route('/edit_contacts')
def edit():
	return 'edit contacts'

if __name__ == '__main__':
	app.run(port = 3000, debug = True) #Setting port and making the program available to change while running