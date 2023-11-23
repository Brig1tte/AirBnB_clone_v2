-- Check if the database hbnb_dev_db already exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbnb_test_db';

-- If it does not exist, create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if the user hbnb_dev already exists
SELECT USER FROM mysql.user WHERE USER = 'hbnb_test';

-- If it does not exist, create the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- If the database or user already exists, the script must not fail
