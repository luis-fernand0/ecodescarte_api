import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_host = os.getenv("HOST")
db_port = os.getenv("PORTA")
db_user = os.getenv("USER")
db_pass = os.getenv("PASS")

conection = mysql.connector(
    host=db_host,
    user=db_user,
    password=db_pass
)