CREATE DATABASE attendence;

USE attendence;

CREATE TABLE StudentAttendence (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
	room VARCHAR(50),
    date DATETIME
);



INSERT INTO StudentAttendence (name, room, date)
VALUES ('John Doe', 'Room A101', '2024-07-02 09:00:00');

SELECT * FROM StudentAttendence