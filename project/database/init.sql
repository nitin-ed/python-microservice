-- init.sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin_123';

CREATE DATABASE auth_db;

GRANT ALL PRIVILEGES ON auth.* TO 'admin'@'localhost';

USE auth_db;

CREATE TABLE IF NOT EXISTS User (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO User(email, password) VALUES ('admin@example.com', '1234');
