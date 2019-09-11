# cs340-project
Project Outline This project will be a website that allows users to log their workouts. The workouts will be stored in a database and users will be able to access this information at a later date. 
 
## Database Outline 
 
### Entities
#### User 
* First Name: Stored by VARCHAR, cannot be blank ○ Last Name: Stored by VARCHAR, cannot be blank 
* Age (could be derived from DoB): Age of the user stored by INT, possibly derived from date of birth 
* Weight: weight of user stored by INT, cannot be blank ○ Height: Height of user stored by INT, cannot be blank 
* Gender: Gender of user stored by VARCHAR, Options are Male, Female, Other. Can be blank 
* Date of Birth: date of birth stored by DATE ○ I.D. Primary Key:  I.D. of each user, used as primary key Auto-Increment number 
 
 
 
#### Workout: This will be the meat of the tables, where we will store each workout that a user inputs  
* I.D. Primary Key: ID for each workout, used as a primary key, Auto-increment number 
* User I.D.:  The user I.D. for a particular user to be able to track their own workout, number ○ Date:  Stores the date the exercise was done that the user inputs,  defaults as today’s date, stored as DATE  
* Exercise I.D. : The exercise I.D. for a particular exercise. Number 
* Reps:  The number of reps for the exercise, cannot be 0, INT 
* Sets:  The number of sets for the exercise, cannot be 0, INT 
* Weight:  The weight used for the exercise if applicable, can be empty. INT 
 
 
#### Exercise 
* I.D. Primary Key: ID for each exercise, used as primary key, Auto-increment 
* Name: The name of the exercise stored as a VARCHAR 

#### Routine 
* I.D. Primary Key: ID for each routine, used as primary key, Auto-increment ○ Name:  The name of the routine stored as a VARCHAR 
 
#### Muscle  
* I.D. Primary Key: Auto-increment number ○ Name of the muscle:  Name of the muscle stored by VARCHAR 
 
 
 
 
### Relationships 
* Users perform workouts - A workout is the exercise, weight lifted, reps performed at that weight, and sets that a user performs. A user performs one or more workouts but a 
workout can only be performed by one user. The User and Workout entities are in a one-to-many relationship.  
* Users have up to one routine - A user has can have zero to one routine.  It will tell the user what exercises they should do and when. A routine can have multiple users that use the routine.  They are in a one to many relationship 
* Workouts consist of one exercise - A workout consists of one exercise and exercises can be part of one or more workouts. The Workout and Exercise entities are in a one-to-many relationship.  
* Routines consist of one or more exercises - A routine consists of one or more exercises and an exercise can be a part of many routines.  The routine and exercises are in a many-to-many relationship. 
* Exercises engage muscles - An exercise works out one or more muscles and a muscle can be worked by one or more exercises. The Exercise and Muscle entities are in a many-to-many relationship. 
 
 
 
