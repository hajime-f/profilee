CREATE DATABASE IF NOT EXISTS profilee_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'profilee_user'@'%' IDENTIFIED BY 'Ktsmk35F';
GRANT ALL PRIVILEGES ON profilee_db.* TO 'profilee_user'@'%';
FLUSH PRIVILEGES;
