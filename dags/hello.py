try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator,BashOperator
    from datetime import datetime
    import pandas as pd

except Exception as ex:
    print("error   {}".format(ex))


# create task
def function1():
    print("Hello...")
    return "Hello..."


# Following are defaults which will be used by Airflow
default_args = {
    'owner': 'Dilip',
    'depends_on_past': False,
    'start_date': datetime(2021, 4, 15),
    'email': ['dlpkmr98@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# create dag
dag = DAG('hello', default_args=default_args)

#Use the PythonOperator to execute Python callables.
function1 = PythonOperator(
    task_id="function1",
    python_callable=function1,
    dag=dag
)

#Use the BashOperator to execute bash command
t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello World from Task 1"',
    dag=dag)
