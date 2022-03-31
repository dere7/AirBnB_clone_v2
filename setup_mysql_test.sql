-- Creates database hbnb_test_db and user hbnb_test
-- and grants some privileges
-- Create the hbnb_test_db table if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create the hbnb_test user if it doesn't exist with the password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Let the new user be able to use the server
GRANT USAGE ON *.* TO 'hbnb_test' @'localhost';
-- Let the new user view the performance_schema table
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test' @'localhost';
-- Let the new user view and modify the hbnb_test_db table
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test' @'localhost';
