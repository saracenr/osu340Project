-- this file contains the data manipulation queries our website will use. The ':' character
-- is used to denote user entered data. 


-- user:

-- get all data from user
SELECT * FROM `user`

-- get all data from user with specified id
SELECT * FROM `user` WHERE `id`=:`id`

-- add new user
INSERT INTO `user` (`first_name`, `last_name`, `date_of_birth`, `weight`, `height`, `gender`, `routine_id`)
VALUES (:`first_name`, :`last_name`, :`date_of_birth`, :`weight`, :`height`, :`gender`, :`routine_id`)

-- change first_name of user with specified id
UPDATE `user` SET `first_name` WHERE `id`=:`id`

-- change first_name of user with specified id
UPDATE `user` SET `last_name` WHERE `id`=:`id`

-- change last_name of user with specified id
UPDATE `user` SET `date_of_birth` WHERE `id`=:`id`

-- change weight_name of user with specified id
UPDATE `user` SET `weight` WHERE `id`=:`id`

-- change height_name of user with specified id
UPDATE `user` SET `height` WHERE `id`=:`id`

-- change gender of user with specified id
UPDATE `user` SET `gender` WHERE `id`=:`id`

-- change routine_id of user with specified id
UPDATE `user` SET `routine_id` WHERE `id`=:`id`


-- workout: 

-- get all data from workout
SELECT * FROM `workout`

-- get all data from workout with specified id
SELECT * FROM `workout` WHERE `id`=:`id`

-- add new workout
INSERT INTO `workout` (`user_id`, `date`, `exercise_id`, `reps`, `sets`, `weight`)
VALUES (:`user_id`, :`date`, :`exercise_id`, :`reps`, :`sets`, :`weight`)

UPDATE `workout` SET `user_id` WHERE `id`=:`id`
UPDATE `workout` SET `date` WHERE `id`=:`id`
UPDATE `workout` SET `data` WHERE `id`=:`id`


-- exercise: 

-- get all data from exercise
SELECT * FROM `exercise`

-- add new exercise
INSERT INTO `exercise` (`name`)
VALUES (:name)


-- routine:

-- get all data from routine
SELECT * FROM `routine`

-- get all data from routine with specified id
SELECT * FROM `routine` WHERE `id`=:`id`

-- add new routine
INSERT INTO `routine` (`name`)
VALUES (:`routine`)


-- routine_exercise:

-- get all data from routine_exercise
SELECT * FROM `routine_exercise`

-- get all data from routine_exercise with specified id
SELECT * FROM `routine_exercise` WHERE `id`=:`id`

-- add new routine_exercise pairing
INSERT INTO `routine_exercise` (`routine_id`, `exercise_id`, `day_of_the_week`, `sets`, `reps`)
VALUES (:`routine_id`, :`exercise_id`, :`day_of_the_week`, :`sets`, :`reps`)


-- exercise_muscle:

-- get all data from exercise_muscle
SELECT * FROM `exercise_muscle`

-- get all data from exercise_muscle with specified id
SELECT * FROM `exercise_muscle` WHERE `id`=:`id`

INSERT INTO `exercise_muscle` (`exercise_id`, `muscle_id`)
VALUES (:`exercise_id`, :`muscle_id`)


-- muscle:

SELECT * FROM `muscle`
SELECT * FROM `muscle` WHERE `id`=:`id`
INSERT INTO `muscle` (`name`)
VALUES (:`name`)
