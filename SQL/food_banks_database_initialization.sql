SHOW databases;
USE tp;
SHOW tables;

CREATE TABLE food_banks
(
id INT unsigned NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
street VARCHAR(255),
city VARCHAR(255),
state VARCHAR(255),
zip NUMERIC(5),
phone VARCHAR(255),
website VARCHAR(255),
PRIMARY KEY (id)
);