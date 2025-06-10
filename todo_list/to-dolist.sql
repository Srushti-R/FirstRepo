CREATE DATABASE todo_db;
USE todo_db;

CREATE TABLE tasks(
id INT auto_increment PRIMARY KEY ,
title VARCHAR(200) NOT NULL,
status ENUM('Pending', 'Completed') DEFAULT 'Pending'
);



 




