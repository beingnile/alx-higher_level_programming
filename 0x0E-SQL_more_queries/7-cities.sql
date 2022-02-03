-- Creates the database hbtn_0d_usa and the table cities
-- The database and the table are created if they don't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
