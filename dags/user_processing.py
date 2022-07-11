from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


from datetime import datetime

with DAG('user_processing',start_date=datetime(2022,1,1), 
        schedule_interval='@daily', catchup=False) as dag:

        create_table = PostgresOperator(
            task_id='create_table',
            postgres_conn_id='postgres',
            sql ='''
            CREATE TABLE IF NOT EXISTS users(
                users_id INT NOT NULL PRIMARY KEY,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
            '''
        );
        populate_customer = PostgresOperator(
            task_id='populate_customer',
            postgres_conn_id='postgres',
            sql='''
                INSERT INTO airflow_db.customers  VALUES(1,'Mathew','Johnson','Nigeria',mat_jon','m@th3w','jonhmat@gmail.com');
            '''
        );
create_table >> populate_customer