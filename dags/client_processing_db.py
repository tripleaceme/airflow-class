from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

from datetime import datetime

with DAG('client_processing_db', start_date=datetime(2022, 1, 1),schedule_interval='@daily', catchup=False) as dag:
 
    create_customer = MySqlOperator(
        task_id='create_customer',
        mysql_conn_id='mysql_conn',
        sql='''
            CREATE TABLE IF NOT EXISTS customers (
                users_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        '''
    );
    create_attendance = MySqlOperator(
        task_id='create_attendance',
        mysql_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS staff (
                users_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        '''
    );
    create_product = MySqlOperator(
        task_id='create_product',
        mysql_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS product (
                users_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        '''
    );