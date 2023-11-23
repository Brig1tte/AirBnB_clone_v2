-- Check if the database hbnb_dev_db already exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbnb_dev_db';

-- If it does not exist, create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user hbnb_dev already exists
SELECT USER FROM mysql.user WHERE USER = 'hbnb_dev';

-- If it does not exist, create the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- If the database or user already exists, the script must not fail
