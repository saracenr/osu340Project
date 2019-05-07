-- this file contains the data manipulation queries our website will use. The ':' character
-- is used to denote user entered data. 


-- user:

SELECT * FROM `user`
SELECT * FROM `user` WHERE `id`=:`id`

INSERT INTO `user` (`first_name`, `last_name`, `date_of_birth`, `weight`, `height`, `gender`, `routine_id`)
VALUES (:`first_name`, :`last_name`, :`date_of_birth`, :`weight`, :`height`, :`gender`, :`routine_id`)

UPDATE `user` SET `first_name` WHERE `id`=:`id`
UPDATE `user` SET `last_name` WHERE `id`=:`id`
UPDATE `user` SET `date_of_birth` WHERE `id`=:`id`
UPDATE `user` SET `weight` WHERE `id`=:`id`
UPDATE `user` SET `height` WHERE `id`=:`id`
UPDATE `user` SET `gender` WHERE `id`=:`id`
UPDATE `user` SET `routine_id` WHERE `id`=:`id`
DELETE FROM `user` WHERE `id`=:`id`


-- workout: 

SELECT * FROM `workout`
SELECT * FROM `workout` WHERE `id`=:`id`

INSERT INTO `workout` (`user_id`, `date`, `exercise_id`, `reps`, `sets`, `weight`)
VALUES (:`user_id`, :`date`, :`exercise_id`, :`reps`, :`sets`, :`weight`)

UPDATE `workout` SET `user_id` WHERE `id`=:`id`
UPDATE `workout` SET `date` WHERE `id`=:`id`
UPDATE `workout` SET `exercise_id` WHERE `id`=:`id`
UPDATE `workout` SET `reps` WHERE `id`=:`id`
UPDATE `workout` SET `sets` WHERE `id`=:`id`
UPDATE `workout` SET `weight` WHERE `id`=:`id`

DELETE FROM `workout` WHERE `id`=:`id`


-- exercise: 

SELECT * FROM `exercise`
SELECT * FROM `exercise` WHERE `id`=:`id`

INSERT INTO `exercise` (`name`)
VALUES (:`name`)

UPDATE `exercise` SET `name` WHERE `id`=:`id`

DELETE FROM `exercise` WHERE `id`=:`id`


-- routine:

SELECT * FROM `routine`
SELECT * FROM `routine` WHERE `id`=:`id`

INSERT INTO `routine` (`name`)
VALUES (:`routine`)

UPDATE `routine` SET `name` WHERE `id`=:`id`

DELETE FROM `routine` WHERE `id`=:`id`


-- routine_exercise:

SELECT * FROM `routine_exercise`
SELECT * FROM `routine_exercise` WHERE `id`=:`id`

INSERT INTO `routine_exercise` (`routine_id`, `exercise_id`, `day_of_the_week`, `sets`, `reps`)
VALUES (:`routine_id`, :`exercise_id`, :`day_of_the_week`, :`sets`, :`reps`)

UPDATE `routine_exercise` SET `routine_id` WHERE `id`=:`id`
UPDATE `routine_exercise` SET `exercise_id` WHERE `id`=:`id`
UPDATE `routine_exercise` SET `day_of_the_week` WHERE `id`=:`id`
UPDATE `routine_exercise` SET `sets` WHERE `id`=:`id`
UPDATE `routine_exercise` SET `reps` WHERE `id`=:`id`

DELETE FROM `routine_exercise` WHERE `id`=:`id`


-- exercise_muscle:

SELECT * FROM `exercise_muscle`
SELECT * FROM `exercise_muscle` WHERE `id`=:`id`

INSERT INTO `exercise_muscle` (`exercise_id`, `muscle_id`)
VALUES (:`exercise_id`, :`muscle_id`)

UPDATE `exercise_muscle` SET `exercise_id` WHERE `id`=:`id`
UPDATE `exercise_muscle` SET `muscle_id` WHERE `id`=:`id`

DELETE FROM `exercise_muscle` WHERE `id`=:`id`


-- muscle:

SELECT * FROM `muscle`
SELECT * FROM `muscle` WHERE `id`=:`id`

INSERT INTO `muscle` (`name`)
VALUES (:`name`)

UPDATE `muscle` SET `name` WHERE `id`=:`id`

DELETE FROM `muscle` WHERE `id`=:`id`