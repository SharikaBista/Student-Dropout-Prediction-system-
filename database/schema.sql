CREATE DATABASE student_dropout_db;
USE student_dropout_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    attendance FLOAT,
    gpa FLOAT,
    engagement FLOAT,
    financial_status VARCHAR(50)
);

CREATE TABLE predictions (
    prediction_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    risk_score FLOAT,
    risk_level VARCHAR(20),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20)
);

