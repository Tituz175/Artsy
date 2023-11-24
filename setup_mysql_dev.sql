-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS artsy_dev_db;
CREATE USER IF NOT EXISTS 'artsy_dev'@'localhost' IDENTIFIED BY 'artsy_dev_pwd';
GRANT ALL PRIVILEGES ON `artsy_dev_db`.* TO 'artsy_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'artsy_dev'@'localhost';
FLUSH PRIVILEGES;


CREATE TABLE IF NOT EXISTS artsy_dev_db.users (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NULL,
    bio VARCHAR(128) NULL
);


CREATE TABLE IF NOT EXISTS artsy_dev_db.posts (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    user_id VARCHAR(60) NOT NULL,
    title VARCHAR(60) NOT NULL,
    description VARCHAR(128) NOT NULL,
    media_link VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    likes INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES artsy_dev_db.users(id)
)
