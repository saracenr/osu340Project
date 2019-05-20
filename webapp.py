from flask import Flask, render_template, request, redirect
from db_connector.db_connector import connect_to_database, execute_query

webapp = Flask(__name__)

@webapp.route('/')
def root():
    return "<p>foobar</p>"


@webapp.route('/userCreate')
def browseUsers():
	print("Fetching user list")
	db_connection = connect_to_database()
	query = "SELECT id, first_name, last_name, date_of_birth, weight, height, gender, routine_id FROM user;"
	result = execute_query(db_connection, query).fetchall();
	print(result)
	return render_template('display_Users.html', rows=result)


