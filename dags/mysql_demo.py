import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow_db',    
   # 'start_date': airflow.utils.dates.days_ago(2),
    #'end_date': datetime(),
    #'depends_on_past': False,
    #'email': ['test@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    #'retries': 1,
    'retry_delay': timedelta(minutes=5),
    }

dag_mysql = DAG(
    'mysql_demo',
    # default_args=args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@daily',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='use case of mysql operator in airflow',catchup = False
)

create_sql_query = """ CREATE TABLE airflow_db.employee(empid int, empname VARCHAR(25), salary int); """

create_table = MySqlOperator(sql=create_sql_query, task_id="CreateTable", mysql_conn_id="mysql_conn", dag=dag_mysql)

insert_sql_query = """ INSERT INTO airflow_db.employee(empid, empname, salary) VALUES(1,'VAMSHI',30000),(2,'chandu',50000); """

insert_data = MySqlOperator(sql=insert_sql_query, task_id="InsertData", mysql_conn_id="mysql_conn", dag=dag_mysql)

# setting the order for running the task

create_table >> insert_data

if __name__ == "__main__":
    dag_mysql.cli()