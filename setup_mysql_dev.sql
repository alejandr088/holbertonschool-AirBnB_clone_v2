-- Creates a db if not exists with the given name.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a user if not exists with the given name & password in the localhost.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the user specified, on the db specified, and in all the tables in the localhost.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege to the user & db specified.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';