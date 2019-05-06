SELECT * FROM user

INSERT INTO user (first_name, last_name, date_of_birth, weight, height, gender, routine_id)
VALUES (:first_name, :last_name, :date_of_birth, :weight, :height, :gender, :routine_id)

SELECT * FROM workout

INSERT INTO workout (user_id, `date`, exercise_id, reps, sets, weight)
VALUES (:user_id, :`date`, :exercise_id, :reps, :sets, :weight)

SELECT * FROM exercise

INSERT INTO exercise (name)
VALUES (:name)

SELECT * FROM routine

INSERT INTO routine (name)
VALUES (:routine)

SELECT * FROM routine_exercise

INSERT INTO routine_exercise (routine_id, exercise_id, day_of_the_week, sets, reps)
VALUES (:routine_id, :exercise_id, :day_of_the_week, :sets, :reps)

SELECT * FROM exercise_muscle

INSERT INTO exercise_muscle (exercise_id, muscle_id)
VALUES (:exercise_id, :muscle_id)

SELECT * FROM muscle

INSERT INTO muscle (name)
VALUES (:name)
