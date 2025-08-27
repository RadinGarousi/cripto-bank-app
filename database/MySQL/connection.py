import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="crypto_bank",
        autocommit=False
    )