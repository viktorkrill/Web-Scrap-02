-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hitch_job_offers;
CREATE USER IF NOT EXISTS 'user1'@'holberton.cm8wxkustwc4.us-east-1.rds.amazonaws.com' IDENTIFIED BY 'GG8nDrzqWkP!aapgDsYrfw.p';
GRANT ALL PRIVILEGES ON `hitch_job_offers`.* TO 'user1'@'holberton.cm8wxkustwc4.us-east-1.rds.amazonaws.comost';
GRANT SELECT ON `performance_schema`.* TO 'user1'@'holberton.cm8wxkustwc4.us-east-1.rds.amazonaws.com';
FLUSH PRIVILEGES;
