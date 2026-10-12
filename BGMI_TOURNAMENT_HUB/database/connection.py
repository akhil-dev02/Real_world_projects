import mysql.connector as SQLC
def DatabaseConnection():
    try:
        db_config=SQLC.connect(
            host = "localhost",
            user =  "root",
            password = "root",
            database =  "Bgmi_Tournament_Hub"
        
        
        )
        return db_config
    except Exception as e:
        print(f"Something wrong in database/connection.py:{e}")
        return None
