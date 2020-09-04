CREATE USER holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* to holberton_user@localhost;
FLUSH PRIVILEGES;
