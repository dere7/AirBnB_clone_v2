-- Creates database hbnb_dev_db and user hbnb_dev
-- and grants some privileges
-- Create the hbnb_test_db table if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the hbnb_dev user if it doesn't exist with the password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Let the new user be able to use the server
GRANT USAGE ON *.* TO 'hbnb_dev' @'localhost';
-- Let the new user view the performance_schema table
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev' @'localhost';
-- Let the new user view and modify the hbnb_test_db table
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev' @'localhost';