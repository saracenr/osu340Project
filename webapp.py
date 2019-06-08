from flask import Flask, render_template, request, redirect, url_for
from db_connector.db_connector import connect_to_database, execute_query
from time import sleep

webapp = Flask(__name__)
URL = "http://flip2.engr.oregonstate.edu:7896/"


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
def workoutTracking():
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
	result = [list(user) for user in result]
	print(result)
	for user in result:
		height = int(user[5])
		user[5] = str(height // 12) + "'" + str(height % 12) + '"'
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

@webapp.route('/add_routine', methods=['POST','GET'])
def add_routine():
	db_connection = connect_to_database()
	routine = request.form['routineSelect']
	exercise = request.form['exerciseName']
	sets = request.form['sets']
	reps = request.form['reps']
	days = request.form['days']
	query = 'INSERT INTO routine_exercise (routine_id, exercise_id, sets, reps, day_of_the_week) VALUES (%s,%s,%s,%s,%s);'
	data = (routine,exercise,sets,reps,days)
	execute_query(db_connection, query, data)
	return redirect(url_for('routineCreate'))

@webapp.route('/create_routine', methods=['POST','GET'])
def create_routine():
	print('Added a new routine!')
	db_connection = connect_to_database()
	routineName = request.form['routineName']
	query = 'INSERT INTO routine (name) VALUES (%s);'
	data = (routineName,)
	execute_query(db_connection, query, data)
	#Fill routineCreate html page
	query = "SELECT re.id, r.name, e.name, re.sets, re.reps, re.day_of_the_week FROM `routine_exercise` as re INNER JOIN exercise as e ON e.id = re.exercise_id INNER JOIN routine AS r ON r.id = re.routine_id;"
	exerciseQuery = "SELECT id, name FROM `exercise`;"
	routineQuery = "SELECT id, name FROM `routine`;"
	result = execute_query(db_connection, query).fetchall()
	exerciseList = execute_query(db_connection, exerciseQuery).fetchall()
	routineList = execute_query(db_connection, routineQuery).fetchall()
	return render_template('routineCreate.html', rows=result, routines=routineList, exercises=exerciseList)

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
	query = "SELECT id, name FROM muscle"
	result = execute_query(db_connection, query).fetchall()
	print(result)
	return render_template('muscleGroupCreate.html', rows=result)

@webapp.route('/add_muscle_group', methods=['POST', 'GET'])
def add_muscle_group():
	print('Added a new muscle group!')
	db_connection = connect_to_database()
	name = request.form['name']
	query = 'INSERT INTO muscle (name) VALUES (%s)'
	data = (name,) # comma needed to force tuple
	print(data)
	execute_query(db_connection, query, data)
	
	print('foobar')
	query = 'SELECT id, name FROM `muscle`'
	result = execute_query(db_connection, query).fetchall()
	return render_template('muscleGroupCreate.html', rows=result)

@webapp.route('/update_muscle/<int:id>', methods=['POST','GET'])
def update_muscle(id):
	db_connection = connect_to_database()
	if request.method == 'GET':
		query = "SELECT id, name FROM muscle WHERE id = %s;" % (id)
		result = execute_query(db_connection, query).fetchone()
		return render_template('muscleGroupUpdate.html', muscle=result)
	elif request.method == 'POST':
		print('Updating muscle!')
		muscle_id = request.form['muscle_id']
		name = request.form['name']		
		query = 'UPDATE muscle SET name=%s WHERE id=%s;'
		data = (name, muscle_id)
		execute_query(db_connection, query, data)
		return redirect(url_for('muscleGroupCreate'))

@webapp.route('/delete_muscle/<int:id>', methods=['POST','GET'])
def delete_muscle(id):
	db_connection = connect_to_database()
	print('Deleting muscle!')
	query = "DELETE FROM muscle WHERE id = %s;" % (id)
	execute_query(db_connection, query)
	return redirect(url_for('muscleGroupCreate'))

@webapp.route('/exerciseCreate')
def exerciseCreate():
	print('Fetching muscle group and exercise lists')
	db_connection = connect_to_database()
	muscleGroupQuery = "SELECT id, name FROM muscle"
	muscleGroupResult = execute_query(db_connection, muscleGroupQuery).fetchall()
	exerciseQuery = "SELECT id, name FROM exercise"
	exerciseResult = execute_query(db_connection, exerciseQuery).fetchall()
	return render_template('exerciseCreate.html', muscleGroups=muscleGroupResult, exercises=exerciseResult)

@webapp.route('/update_user/<int:id>', methods=['POST','GET'])
def update_user(id):
	db_connection = connect_to_database()
	if request.method == 'GET':
		userQuery = "SELECT id, first_name, last_name, height, weight, date_of_birth, gender FROM user WHERE id = %s;" % (id)
		userResult = list(execute_query(db_connection, userQuery).fetchone())
		height = userResult[3]
		userResult[3] = height // 12
		userResult.insert(4, height % 12)
		return render_template('userUpdate.html', user=userResult)
	elif request.method == 'POST':
		print('Update user!')
		userID = request.form['user_id']
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		date_of_birth = request.form['dob']
		weight = request.form['weight']
		feet = int(request.form['feet'])
		inches = int(request.form['inches'])
		height = str(feet * 12 + inches)
		gender = request.form['gender']
		query = 'UPDATE user SET first_name=%s, last_name=%s, date_of_birth=%s, weight=%s, height=%s, gender=%s WHERE id=%s;'
		data = (first_name, last_name, date_of_birth, weight, height, gender, userID)
		execute_query(db_connection, query, data)
		return redirect(url_for('browseUsers'))


@webapp.route('/add_user', methods=['POST','GET'])
def add_user():
	print('Added a new user!')
	db_connection = connect_to_database()
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	date_of_birth = request.form['dob']
	weight = request.form['weight']
	feet = int(request.form['feet'])
	inches = int(request.form['inches'])
	height = str(feet * 12 + inches)
	gender = request.form['gender']
	query = 'INSERT INTO user (first_name, last_name, date_of_birth, weight, height, gender) VALUES (%s,%s,%s,%s,%s,%s)'
	data = (first_name, last_name, date_of_birth, weight, height, gender)
	execute_query(db_connection, query, data)
	return redirect(url_for('browseUsers'))

@webapp.route('/delete_user/<int:id>', methods=['POST','GET'])
def delete_user(id):
	db_connection = connect_to_database()
	print('Deleting user!')
	query = 'DELETE FROM user WHERE id=%s;'
	data = (id,)
	execute_query(db_connection, query, data)
	return redirect(url_for('browseUsers'))

@webapp.route('/add_exercise', methods=['POST','GET'])
def add_exercise():
	print('Added a new exercise!')
	db_connection = connect_to_database()
	name = request.form['name']
	query = 'INSERT INTO exercise (name) VALUES (%s)'
	data = (name,)
	execute_query(db_connection, query, data)
	query = "SELECT id FROM exercise WHERE name = '" + name + "'" 
	exerciseResult = execute_query(db_connection, query).fetchall()
	exercise_id = exerciseResult[0][0]
	print(exerciseResult)
	print(exercise_id)
	for muscle_id in request.form.getlist('muscleGroups'):
		print(muscle_id)
		query = 'INSERT INTO exercise_muscle (exercise_id, muscle_id) VALUES (%s,%s)'
		data = (exercise_id, muscle_id)
		execute_query(db_connection, query, data)
	print('Fetching muscle group and exercise lists')
	muscleGroupQuery = "SELECT id, name FROM muscle"
	muscleGroupResult = execute_query(db_connection, muscleGroupQuery).fetchall()
	exerciseQuery = "SELECT id, name FROM exercise"
	exerciseResult = execute_query(db_connection, exerciseQuery).fetchall()
	return render_template('exerciseCreate.html', muscleGroups=muscleGroupResult, exercises=exerciseResult)

@webapp.route('/update_exercise', methods=['POST', 'GET'])
def update_exercise():
	db_connection = connect_to_database()
	if request.method == 'GET':
		print('Editing exercise!')
		data = (request.args.get('id'),)
		exerciseQuery = "SELECT id, name FROM exercise WHERE id=(%s)"
		exerciseResult = execute_query(db_connection, exerciseQuery, data).fetchone()
		selectedMusclesQuery = "SELECT m.id, m.name FROM exercise AS e JOIN exercise_muscle AS em ON e.id=em.exercise_id JOIN muscle AS m ON em.muscle_id=m.id WHERE e.id=(%s)"
		selectedMusclesResult = execute_query(db_connection, selectedMusclesQuery, data).fetchall()
		unselectedMusclesQuery = "SELECT m.id, m.name FROM muscle AS m WHERE m.id NOT IN (SELECT m.id FROM exercise AS e JOIN exercise_muscle AS em ON e.id=em.exercise_id JOIN muscle AS m ON em.muscle_id=m.id WHERE e.id=(%s))"
		unselectedMusclesResult = execute_query(db_connection, unselectedMusclesQuery, data).fetchall()
		return render_template('updateExercise.html', exercise=exerciseResult, selectedMuscles=selectedMusclesResult, unselectedMuscles=unselectedMusclesResult)
	elif request.method == 'POST':
		print('Updating exercise!')
		exercise_id = request.form['exercise_id']
		exercise_name = request.form['exercise_name']
		data = (exercise_id,)
		exerciseNameQuery = "UPDATE exercise SET name=(%s) WHERE id=(%s)"
		execute_query(db_connection, exerciseNameQuery, (exercise_name, exercise_id))
		muscleGroupQuery = "SELECT muscle_id FROM exercise_muscle WHERE exercise_id=(%s)"
		muscleGroupResult = execute_query(db_connection, muscleGroupQuery, data).fetchall()
		for muscle_id in muscleGroupResult:
			muscleDeleteQuery = "DELETE FROM exercise_muscle WHERE muscle_id=(%s) AND exercise_id=(%s)"
			execute_query(db_connection, muscleDeleteQuery, (muscle_id, exercise_id))
		for muscle_id in request.form.getlist('muscleGroups'):
			query = 'INSERT INTO exercise_muscle (exercise_id, muscle_id) VALUES (%s,%s)'
			data = (exercise_id, muscle_id)
			execute_query(db_connection, query, data)
		print('Fetching muscle group and exercise lists')
		muscleGroupQuery = "SELECT id, name FROM muscle"
		muscleGroupResult = execute_query(db_connection, muscleGroupQuery).fetchall()
		exerciseQuery = "SELECT id, name FROM exercise"
		exerciseResult = execute_query(db_connection, exerciseQuery).fetchall()
		return render_template('exerciseCreate.html', muscleGroups=muscleGroupResult, exercises=exerciseResult)

@webapp.route('/delete_exercise', methods=['POST', 'GET'])
def delete_exercise():
	db_connection = connect_to_database()
	print('Deleting exercise!')
	data = (request.args.get('id'),)
	# print('id: ', data)
	# test = "SELECT muscle_id FROM exercise_muscle"
	# result = execute_query(db_connection, test).fetchall()
	# print(result)
	deleteQuery = "DELETE FROM exercise WHERE id=(%s)"
	execute_query(db_connection, deleteQuery, data)
	return redirect(url_for('exerciseCreate'))

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
	print(data)
	execute_query(db_connection, query, data)
	# Run the display query using the user they selected
	query = "SELECT w.id, e.name, w.sets, w.reps, w.weight, w.date, w.user_id FROM `workout` as w INNER JOIN exercise as e ON e.id = w.exercise_id WHERE w.user_id = " + userID + ';'
	exerciseQuery = "SELECT id, name FROM `exercise`;"
	userQuery = "SELECT id, first_name, last_name FROM `user`;"
	result = execute_query(db_connection, query).fetchall()
	exerciseList = execute_query(db_connection, exerciseQuery).fetchall()
	userList = execute_query(db_connection, userQuery).fetchall()
	return render_template('workoutTracking.html', rows=result, exercises=exerciseList, users=userList)

@webapp.route('/update_workout/<int:id>', methods=['POST','GET'])
def update_workout(id):
	db_connection = connect_to_database()
	if request.method == 'GET':
		#query for specific workout
		query = "SELECT id, exercise_id, user_id, sets, reps, weight, date FROM workout WHERE id = %s;" % (id)
		result = execute_query(db_connection, query).fetchone()
		#queries for exercise and name list boxes
		exerciseQuery = "SELECT id, name FROM `exercise`;"
		userQuery = "SELECT id, first_name, last_name FROM `user`;"
		exerciseList = execute_query(db_connection, exerciseQuery).fetchall()
		userList = execute_query(db_connection, userQuery).fetchall()
		return render_template('updateWorkout.html', workout=result, exercises=exerciseList, users=userList)
	elif request.method == 'POST':
		print('Updating workout!')
		workoutID = request.form['workout_id']
		exerciseID = request.form['exerciseName']
		userID = request.form['userName']
		sets = request.form['sets']
		reps = request.form['reps']
		weight = request.form['weight']
		date = request.form['date']	
		query = 'UPDATE workout SET exercise_id=%s, user_id=%s, sets=%s, reps=%s, weight=%s, date=%s WHERE id=%s;'
		data = (exerciseID, userID, sets, reps, weight, date, workoutID)
		print('data: ', data)
		execute_query(db_connection, query, data)
		return redirect(url_for('workoutTracking'))

@webapp.route('/delete_workout/<int:id>', methods=['POST','GET'])
def delete_workout(id):
	db_connection = connect_to_database()	
	query = 'DELETE FROM workout WHERE id=%s;'
	data = (id,)
	execute_query(db_connection, query, data)
	return redirect(url_for('workoutTracking'))