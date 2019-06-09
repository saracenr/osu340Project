-- This file contains the data manipulation queries our website will use. The '%' and ':' characters
-- are used to denote user entered data. 


-- user:

SELECT * FROM `user`;
SELECT * FROM `user` WHERE `id`=:`id`;
SELECT id, first_name, last_name FROM `user`;
-- get data for specifc user:
SELECT u.id, u.first_name, u.last_name, u.date_of_birth, u.weight, u.height, u.gender, r.name FROM user AS u INNER JOIN routine as r ON r.id = u.routine_id;


INSERT INTO `user` (`first_name`, `last_name`, `date_of_birth`, `weight`, `height`, `gender`, `routine_id`)
VALUES (:`first_name`, :`last_name`, :`date_of_birth`, :`weight`, :`height`, :`gender`, :`routine_id`);

UPDATE `user` SET `first_name` WHERE `id`=:`id`;
UPDATE `user` SET `last_name` WHERE `id`=:`id`;
UPDATE `user` SET `date_of_birth` WHERE `id`=:`id`;
UPDATE `user` SET `weight` WHERE `id`=:`id`;
UPDATE `user` SET `height` WHERE `id`=:`id`;
UPDATE `user` SET `gender` WHERE `id`=:`id`;
UPDATE `user` SET `routine_id` WHERE `id`=:`id`;
UPDATE user SET first_name=%s, last_name=%s, date_of_birth=%s, weight=%s, height=%s, gender=%s, routine_id=%s WHERE id=%s;

DELETE FROM `user` WHERE `id`=:`id`;


-- workout: 

SELECT * FROM `workout`;
SELECT * FROM `workout` WHERE `id`=:`id`;
-- get exercise and workout data for first user in database: 
SELECT w.id, e.name, w.sets, w.reps, w.weight, w.date, w.user_id FROM `workout` as w INNER JOIN exercise as e ON e.id = w.exercise_id WHERE w.user_id = 1;
-- get exercise and workout data for specifc user
SELECT w.id, e.name, w.sets, w.reps, w.weight, w.date, w.user_id FROM `workout` as w INNER JOIN exercise as e ON e.id = w.exercise_id WHERE w.user_id =(%s);
INSERT INTO workout (user_id, exercise_id, sets, reps, weight, date) 
VALUES (%s,%s,%s,%s,%s,%s);

UPDATE `workout` SET `user_id` WHERE `id`=:`id`;
UPDATE `workout` SET `date` WHERE `id`=:`id`;
UPDATE `workout` SET `exercise_id` WHERE `id`=:`id`;
UPDATE `workout` SET `reps` WHERE `id`=:`id`;
UPDATE `workout` SET `sets` WHERE `id`=:`id`;
UPDATE `workout` SET `weight` WHERE `id`=:`id`;
UPDATE workout SET exercise_id=%s, user_id=%s, sets=%s, reps=%s, weight=%s, date=%s WHERE id=%s;

DELETE FROM `workout` WHERE `id`=:`id`;


-- exercise: 

SELECT * FROM `exercise`;
SELECT * FROM `exercise` WHERE `id`=:`id`;
SELECT id, name FROM `exercise`;
SELECT id, first_name, last_name FROM `user`;
-- get muscles used in specific exercise:
SELECT m.id, m.name FROM exercise AS e JOIN exercise_muscle AS em ON e.id=em.exercise_id JOIN muscle AS m ON em.muscle_id=m.id WHERE e.id=(%s);
-- get all muscles not used by specific exercise
SELECT m.id, m.name FROM muscle AS m WHERE m.id NOT IN (SELECT m.id FROM exercise AS e JOIN exercise_muscle AS em ON e.id=em.exercise_id JOIN muscle AS m ON em.muscle_id=m.id WHERE e.id=(%s))

INSERT INTO `exercise` (`name`)
VALUES (:`name`);

UPDATE `exercise` SET `name` WHERE `id`=:`id`;

DELETE FROM `exercise` WHERE `id`=:`id`;


-- routine:

SELECT * FROM `routine`;
SELECT * FROM `routine` WHERE `id`=:`id`;
SELECT id, name FROM `routine`;

INSERT INTO `routine` (`name`)
VALUES (:`routine`);

UPDATE `routine` SET `name` WHERE `id`=:`id`;

DELETE FROM `routine` WHERE `id`=:`id`;


-- routine_exercise:

SELECT * FROM `routine_exercise`;
SELECT * FROM `routine_exercise` WHERE `id`=:`id`;
-- get data for all routines and order by routine_id in ascending order:
SELECT re.id, r.name, e.name, re.sets, re.reps, re.day_of_the_week FROM `routine_exercise` as re INNER JOIN exercise as e ON e.id = re.exercise_id INNER JOIN routine AS r ON r.id = re.routine_id ORDER BY re.id ASC;
-- get data for specific routine:
SELECT re.id, r.name, e.name, re.sets, re.reps, re.day_of_the_week FROM `routine_exercise` as re INNER JOIN exercise as e ON e.id = re.exercise_id INNER JOIN routine AS r ON r.id = re.routine_id WHERE r.id = %s;
SELECT id, routine_id, exercise_id, sets, reps, day_of_the_week FROM routine_exercise WHERE id = %s;

INSERT INTO `routine_exercise` (`routine_id`, `exercise_id`, `day_of_the_week`, `sets`, `reps`)
VALUES (:`routine_id`, :`exercise_id`, :`day_of_the_week`, :`sets`, :`reps`);

UPDATE `routine_exercise` SET `routine_id` WHERE `id`=:`id`;
UPDATE `routine_exercise` SET `exercise_id` WHERE `id`=:`id`;
UPDATE `routine_exercise` SET `day_of_the_week` WHERE `id`=:`id`;
UPDATE `routine_exercise` SET `sets` WHERE `id`=:`id`;
UPDATE `routine_exercise` SET `reps` WHERE `id`=:`id`;
-- update data of specific routine
UPDATE routine_exercise SET routine_id=%s, exercise_id=%s, sets=%s, reps=%s, day_of_the_week=%s WHERE id=%s;

DELETE FROM `routine_exercise` WHERE `id`=:`id`;


-- exercise_muscle:

SELECT * FROM `exercise_muscle`;
SELECT * FROM `exercise_muscle` WHERE `id`=:`id`;
SELECT muscle_id FROM exercise_muscle WHERE exercise_id=(%s);

INSERT INTO `exercise_muscle` (`exercise_id`, `muscle_id`)
VALUES (:`exercise_id`, :`muscle_id`);

UPDATE `exercise_muscle` SET `exercise_id` WHERE `id`=:`id`;
UPDATE `exercise_muscle` SET `muscle_id` WHERE `id`=:`id`;

DELETE FROM `exercise_muscle` WHERE `id`=:`id`;
-- delete specific muscle from specific exercise
DELETE FROM exercise_muscle WHERE muscle_id=(%s) AND exercise_id=(%s);


-- muscle:

SELECT * FROM `muscle`;
SELECT * FROM `muscle` WHERE `id`=:`id`;
SELECT id, name FROM muscle;

INSERT INTO `muscle` (`name`)
VALUES (:`name`);

UPDATE `muscle` SET `name` WHERE `id`=:`id`;

DELETE FROM `muscle` WHERE `id`=:`id`;