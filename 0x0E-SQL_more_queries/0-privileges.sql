-- Lists all privileges of the MySQL users user_0d_1
-- and user_0d_2 on a server
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
