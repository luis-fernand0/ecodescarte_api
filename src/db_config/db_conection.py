import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_conection():
    db_host = os.getenv("HOST")
    db_port = os.getenv("PORTA")
    db_user = os.getenv("USER")
    db_pass = os.getenv("PASS")
    db = os.getenv("DATABASE")

    try:
        conection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            database=db,
            password=db_pass
        )
        return conection
    except Error:
        print(f"Não foi possivel se conectar ao banco, erro: {Error}")
        return None