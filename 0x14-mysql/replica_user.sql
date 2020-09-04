-- Script to create replica user in the master
-- and giving it the permision to REPLICATE SLAVE
-- Key: the % means 'from any host'.
CREATE USER replica_user@% IDENTIFIED BY 'replica_user';
GRANT REPLICATION SLAVE ON *.* TO replica_user@%;
GRANT SELECT ON mysql.user TO holberton_user@localhost;

