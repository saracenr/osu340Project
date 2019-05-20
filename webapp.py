from flask import Flask, render_template, request, redirect
from db_connector.db_connector import connect_to_database, execute_query

webapp = Flask(__name__)

@webapp.route('/')
def root():
    return 'Foobar'


@webapp.route('/displayUsers')
def browseUsers():
	print("Fetching user list")
	db_connection = connect_to_database()
	query = "SELECT id, first_name, last_name, date_of_birth, weight, height, gender, routine_id FROM user;"
	result = execute_query(db_connection, query).fetchall();
	print(result)
	return render_template('display_Users.html', rows=result)

@webapp.route('/userCreate')
def userCreate():
    return render_template('userCreate.html')

@webapp.route('/add_user', methods=['POST','GET'])
def add_user():
	print('Added a new user!')
	db_connection = connect_to_database()
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	date_of_birth = request.form['dob']
	weight = request.form['weight']
	feet = request.form['feet']
	inches = request.form['inches']
	gender = request.form['gender']
	query = 'INSERT INTO user (first_name, last_name, date_of_birth, weight, height, gender) VALUES (%s,%s,%s,%s,%s,%s)'
	data = (first_name, last_name, date_of_birth, weight, feet, gender)
	execute_query(db_connection, query, data)
	return render_template('display_Users.html')
