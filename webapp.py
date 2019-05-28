from flask import Flask, render_template, request, redirect
from db_connector.db_connector import connect_to_database, execute_query

webapp = Flask(__name__)
URL = "http://flip2.engr.oregonstate.edu:7890/"


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
	userQuery = "SELECT id, first_name, last_name FROM `user`;"
	result = execute_query(db_connection, query).fetchall()
	exerciseList = execute_query(db_connection, exerciseQuery).fetchall()
	userList = execute_query(db_connection, userQuery).fetchall()
	return render_template('workoutTracking.html', rows=result, exercises=exerciseList, users=userList)

@webapp.route('/displayUsers')
def browseUsers():
	print("Fetching user list")
	db_connection = connect_to_database()
	query = "SELECT id, first_name, last_name, date_of_birth, weight, height, gender, routine_id FROM user;"
	result = execute_query(db_connection, query).fetchall()
	print(result)
	return render_template('display_Users.html', rows=result)

@webapp.route('/userCreate')
def userCreate():
    return render_template('userCreate.html')

@webapp.route('/routineCreate')
def routineCreate():
	db_connection = connect_to_database()
	query = "SELECT re.id, r.name, e.name, re.sets, re.reps, re.day_of_the_week FROM `routine_exercise` as re INNER JOIN exercise as e ON e.id = re.exercise_id INNER JOIN routine AS r ON r.id = re.routine_id;"
	exerciseQuery = "SELECT id, name FROM `exercise`;"
	routineQuery = "SELECT id, name FROM `routine`;"
	print(query)
	print(exerciseQuery)
	print(routineQuery)
	result = execute_query(db_connection, query).fetchall()
	exerciseList = execute_query(db_connection, exerciseQuery).fetchall()
	routineList = execute_query(db_connection, routineQuery).fetchall()
	print(result)
	print(exerciseList)
	print(routineList)
	return render_template('routineCreate.html', rows=result, routines=routineList, exercises=exerciseList)

@webapp.route('/add_routine')
def add_routine():

	return render_template('routineCreate.html')

@webapp.route('/create_routine', methods=['POST','GET'])
def create_routine():
	print('Added a new routine!')
	db_connection = connect_to_database()
	routineName = request.form['routineName']
	query = 'INSERT INTO routine name VALUES %s;'
	data = routineName
	execute_query(db_connection, query, data)
	return render_template('routineCreate.html')

@webapp.route('/routineSelect')
def routineSelect():
	print("Fetching routine list")
	db_connection = connect_to_database()
	query = "SELECT id, name FROM routine;"
	result = execute_query(db_connection, query).fetchall()
	print(result)
	return render_template('routineSelect.html', rows=result)

@webapp.route('/muscleGroupCreate')
def muscleGroupCreate():
	print("Fetching muscle group list")
	db_connection = connect_to_database()
	query = "SELECT name FROM muscle"
	result = execute_query(db_connection, query).fetchall()
	print(result)
	return render_template('muscleGroupCreate.html', rows=result)

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

@webapp.route('/add_muscle_group', methods=['POST', 'GET'])
def add_muscle_group():
	print('Added a new muscle group!')
	db_connection = connect_to_database()
	name = request.form['name']
	query = 'INSERT INTO muscle (name) VALUES (%s)'
	data = (name)
	execute_query(db_connection, query, data)
	
	print('foobar')
	query = 'SELECT name FROM `muscle`'
	result = execute_query(db_connection, query).fetchall()
	return render_template('muscleGroupCreate.html', rows=result)

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
	data = (userID, exerciseID, sets, reps, weight, date)
	execute_query(db_connection, query, data)
	# Run the display query using the user they selected
	query = "SELECT w.id, e.name, w.sets, w.reps, w.weight, w.date, w.user_id FROM `workout` as w INNER JOIN exercise as e ON e.id = w.exercise_id WHERE w.user_id = " + userID + ';'
	exerciseQuery = "SELECT id, name FROM `exercise`;"
	userQuery = "SELECT id, first_name, last_name FROM `user`;"
	result = execute_query(db_connection, query).fetchall()
	exerciseList = execute_query(db_connection, exerciseQuery).fetchall()
	userList = execute_query(db_connection, userQuery).fetchall()
	return render_template('workoutTracking.html', rows=result, exercises=exerciseList, users=userList)