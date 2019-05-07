DROP TABLE IF EXISTS `exercise_muscle`;
DROP TABLE IF EXISTS `workout`;
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `routine_exercise`;
DROP TABLE IF EXISTS `routine`;
DROP TABLE IF EXISTS `muscle`;


CREATE TABLE `routine` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `exercise`;
CREATE TABLE `exercise` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `exercise` (`name`) VALUES ('bench press'), ('pullup');


CREATE TABLE `user` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`first_name` varchar(255) NOT NULL,
	`last_name` varchar(255) NOT NULL,
	`date_of_birth` date,
	`weight` int,
	`height` int, -- height is stored in inches
	`gender` varchar(255),
	`routine_id` int(11), 
	PRIMARY KEY (`id`),
	CONSTRAINT `user_fk1` FOREIGN KEY (`routine_id`) REFERENCES `routine` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user` (`first_name`, `last_name`, `date_of_birth`, `weight`, `height`, `gender`) VALUES ('George', 'Costanza', '1959-04-01', 230, 67, 'male'), ('Elaine', 'Benes', '1962-01-29', 63, 119, 'female');


CREATE TABLE `workout` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`user_id` int(11) NOT NULL,
	`date` date,
	`exercise_id` int(11) NOT NULL,
	`reps` int(11) NOT NULL,
	`sets` int(11) NOT NULL DEFAULT 1, 
	`weight` int(11),
	PRIMARY KEY (`id`),
	CONSTRAINT `workout_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
	CONSTRAINT `workout_fk2` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `workout` (`user_id`, `date`, `exercise_id`, `reps`, `sets`, `weight`) VALUES (1, '2019-05-03', 1, 8, 1, 45), (1, '2019-05-03', 2, 4, 2, 35);


CREATE TABLE `muscle` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `muscle` (`name`) VALUES ('shoulders'), ('chest'), ('lower back'), ('upper back'), ('forearms'), ('biceps'), ('triceps'), ('lower legs'), ('upper legs');


CREATE TABLE `routine_exercise` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`routine_id` int(11) NOT NULL,
	`exercise_id` int(11) NOT NULL,
	`day_of_the_week` date,
	`sets` int(11) NOT NULL,
	`reps` int(11) NOT NULL,
	PRIMARY KEY (`id`),
	CONSTRAINT `routine_exercise_fk1` FOREIGN KEY (`routine_id`) REFERENCES `routine` (`id`),
	CONSTRAINT `routine_exercise_fk2` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `exercise_muscle` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`exercise_id` int(11) NOT NULL,
	`muscle_id` int(11) NOT NULL,
	PRIMARY KEY (`id`),
	CONSTRAINT `exercise_muscle_fk1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`),
	CONSTRAINT `exercise_muscle_fk2` FOREIGN KEY (`muscle_id`) REFERENCES `muscle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `exercise_muscle` (`exercise_id`, `muscle_id`) VALUES (1, 1), (1, 3), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7);





