from flask import Flask, render_template, request, redirect
from db_connector.db_connector import connect_to_database, execute_query

webapp = Flask(__name__)
URL = "http://flip1.engr.oregonstate.edu:3987/"


@webapp.route('/')
def index():
	workoutTracking = URL + "workoutTracking"
	displayUsers = URL + "displayUsers"
	userCreate = URL + "userCreate"
	routineCreate = URL + "routineCreate"
	routineSelect = URL + "routineSelect"
	muscleGroupCreate = URL + "muscleGroupCreate"
	exerciseCreate = URL + "exerciseCreate"
	return render_template('index.html', **locals())

@webapp.route('/workoutTracking')
def workouts():
	print("Fetching workout")
	db_connection = connect_to_database()
	query = "SELECT w.id, e.name, w.sets, w.reps, w.weight, w.date, w.user_id FROM `workout` as w INNER JOIN exercise as e ON e.id = w.exercise_id WHERE w.user_id = 1;"
	exerciseQuery = "SELECT id, name FROM `exercise`;"
	userQuery = "SELECT id, name FROM 'user';"
	result = execute_query(db_connection, query).fetchall();
	exerciseList = execute_query(db_connection, exerciseQuery).fetchall();
	userList = execute_query(db_connection, userQuery).fetchall();
	return render_template('workoutTracking.html', rows=result, exercises=exerciseList, userList=users)

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

@webapp.route('/routineCreate')
def routineCreate():
	return render_template('routineCreate.html')

@webapp.route('/routineSelect')
def routineSelect():
	print("Fetching routine list")
	db_connection = connect_to_database()
	query = "SELECT id, name FROM routine;"
	result = execute_query(db_connection, query).fetchall();
	print(result)
	return render_template('routineSelect.html', rows=result)

@webapp.route('/muscleGroupCreate')
def muscleGroupCreate():
	return render_template('muscleGroupCreate.html')

@webapp.route('/exerciseCreate')
def exerciseCreate():
	return render_template('exerciseCreate.html')

@webapp.route('/add_User', methods=['POST','GET'])
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

@webapp.route('/add_exercise', methods=['POST','GET'])
def add_exercise():
	print('Added a new exercise!')
	db_connection = connect_to_database()
	name = request.form['name']
	query = 'INSERT INTO exercise (name) VALUES (%s)'
	data = (name)
	execute_query(db_connection, query, data)
	return render_template('exerciseCreate.html')

@webapp.route('/add_workout', methods=['POST','GET'])
def add_workout():
	print('Added a new workout!')
	db_connection = connect_to_database()
	exerciseID = request.form['exerciseName']
	userID = request.form['userName']
	sets = request.form['sets']
	reps = request.form['reps']
	weight = request.form['weight']
	date = request.form['date']
	query = 'INSERT INTO workout (user_id, exercise_id, sets, reps, weight, date) VALUES (%s,%s,%s,%s,%s,%s)'
	data = (exerciseID, userID, sets, reps, weight, date)
	execute_query(db_connection, query, data)
	return render_template('workoutTracking.html')