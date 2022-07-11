## Lecture Notes
# Always do this when you add a new task to your DAG so as to prevent error.
- To access your DAGS via the airflow cli:
 -- docker-compose ps
 -- docker exec -it airflow-class_airflow-scheduler_1/ bin/bash
 ##### Step 2 allows you to access that particular scheduler path and enables you to use AirFlow CLI 
 -- airflow -h
 ### That shows you all the commands you can use in the AirFlow CLI which can be used on a particular DAG or task
 ### Type airflow tasks test unique_dag_id unique_task_id date_you_are_test_for
 -- airflow tasks test user_processing create_table 2022-02-02

## WORKED WELL FOR MY POSTGRES DATABASE BUT HAVING CONNECTION ISSUES WITH MYSQL

This guy even laid a tutorial about setting up a DAG from scratch [here](https://www.projectpro.io/recipes/use-mysqloperator-airflow-dag#mcetoc_1g4ilqejoh) but still getting error !

This is the error `MySQLdb._exceptions.OperationalError: (2002, "Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)")`

DAG is just a Python file used to organize tasks and set their execution context. DAGs do not perform any actual computation. Instead, tasks are the element of Airflow that actually "do the work" we want to be performed. And it is your job to write the configuration and organize the tasks in specific orders to create a complete data pipeline.