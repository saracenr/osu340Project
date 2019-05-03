DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`first_name` varchar(255) NOT NULL,
	`last_name` varchar(255) NOT NULL,
	`date_of_birth` date,
	`weight` int,
	`height` int, -- inches?
	`gender` varchar(255),
	`routine_id` int(11), 
	PRIMARY KEY (`id`),
	FOREIGN KEY (`routine_id`) REFERENCES `routine` (`id`)
)

LOCK TABLES `user` WRITE;
INSERT INTO `user` VALUES ('George', 'Costanza', '1959-04-01', 230, 67, 'male'), ('Elaine', 'benes', '1962-01-29', 63, 119, 'female');
UNLOCK TABLES;



DROP TABLE IF EXISTS `workout`;
CREATE TABLE `workout` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`user_id` int(11) NOT NULL,
	`date` date,
	`exercise_id` int(11) NOT NULL,
	`reps` int(11) NOT NULL,
	`sets` int(11) NOT NULL DEFAULT 1, 
	`weight` int(11),
	PRIMARY KEY (`id`),
	FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
	FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`)
)

LOCK TABLES `workout` WRITE;
INSERT INTO `workout` VALUES (1, '2019-05-03', 1, 8, 1, 45), (1, '2019-05-03', 2, 4, 2, 35);
UNLOCK TABLES;



DROP TABLE IF EXISTS `exercise`;
CREATE TABLE `exercise` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
)

LOCK TABLES `exercise` WRITE;
INSERT INTO `exercise` VALUES ('bench press'), ('pullup');
UNLOCK TABLES;

DROP TABLE IF EXISTS `routine`;
CREATE TABLE `routine` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)

)

-- LOCK TABLES `routine` WRITE;
-- INSERT INTO `routine` VALUES (), (), ();
-- UNLOCK TABLES;



DROP TABLE IF EXISTS `routine_exercise`;
CREATE TABLE `routine_exercise` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`routine_id` int(11) NOT NULL,
	`exercise_id` int(11) NOT NULL,
	`day_of_the_week` date,
	`sets` int(11) NOT NULL,
	`reps` int(11) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`routine_id`) REFERENCES `routine` (`id`),
	FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`)
)

-- LOCK TABLES `routine_exercise` WRITE;
-- INSERT INTO `routine_exercise` VALUES (), (), ();
-- UNLOCK TABLES;



DROP TABLE IF EXISTS `exercise_muscle`;
CREATE TABLE `exercise_muscle` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`exercise_id` int(11) NOT NULL,
	`muscle_id`, int(11) NOT NULL,
	PRIMARY KEY (`id`)
	FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`),
	FOREIGN KEY (`muscle_id`) REFERENCES `muscle` (`id`)
)

LOCK TABLES `exercise_muscle` WRITE;
INSERT INTO `exercise_muscle` VALUES (1, 1), (1, 3), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7);
UNLOCK TABLES;



DROP TABLE IF EXISTS `muscle`;
CREATE TABLE `muscle` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
)

LOCK TABLES `muscle` WRITE;
INSERT INTO `muscle` VALUES ('pectoralis major'), ('biceps brachii'), ('triceps brachii'), ('brachialis'), ('brachioradialis'), ('deltoid'), ('trapezius'), ('teres major');
UNLOCK TABLES;

