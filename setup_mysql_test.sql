-- Creates a db if not exists with the given name.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a user if not exists with the given name & password in the localhost.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to the user specified, on the db specified, and in all the tables in the localhost.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to the user & db specified.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';