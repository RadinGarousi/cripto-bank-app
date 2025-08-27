import mysql.connector

connect_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="crypto_bank"
)

cursor = connect_database.cursor()

# cursor.execute("CREATE DATABASE crypto_bank")   #create database file

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users_accounts(
    id INT AUTO_INCREMENT,
    phone_number VARCHAR(20) UNIQUE,
    birthday_date DATE,
    national_code VARCHAR(10) UNIQUE,
    username VARCHAR(30) UNIQUE,
    password VARCHAR(50) UNIQUE,
    location VARCHAR(100),
    register_date DATETIME,
    PRIMARY KEY(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appearance(
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL UNIQUE,
    them_mode VARCHAR(6) NOT NULL DEFAULT 'system',
    user_device VARCHAR(7) NOT NULL,
    user_language VARCHAR(50),
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users_accounts(id)
)
""")