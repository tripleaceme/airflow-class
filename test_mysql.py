import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'airflow_user',
    password = 'airflow_user',
    db = 'airflow_db',
    auth_plugin='mysql_native_password')

print(mydb)