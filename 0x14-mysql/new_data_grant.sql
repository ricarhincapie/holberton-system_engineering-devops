CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (
	id INT, 
	name VARCHAR(256)
);
INSERT INTO nexus6 (id, name) VALUES (1, 'Leon');
GRANT SELECT ON *.* TO holberton_user@localhost;
SHOW GRANTS FOR holberton_user@localhost;
SELECT * FROM nexus6;
