from database.MySQL.connection import connect_db

class SignupQueries:
    def insert_userdevice_themmode(self,user_device):

        users_accounts_queri = "INSERT INTO users_accounts () VALUES ()"
        appearance_queri = "INSERT INTO appearance (user_id, user_device)VALUES (%s, %s)"

        conn = connect_db()
        with conn.cursor() as cursor:
            cursor.execute(users_accounts_queri)
            user_id = cursor.lastrowid
            cursor.execute(appearance_queri, params=(user_id, users_device))
            conn.commit()