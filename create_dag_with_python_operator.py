from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args={
    'owner':"shaik mahammad ali",
    "retries":5,
    "retry_delay":timedelta(minutes=5)

}
def task1_function( age,ti):
    # name=ti.xcom_pull(task_ids="get_name")
    first_name=ti.xcom_pull(task_id="get_name",key="first_name")
    last_name=ti.xcom_pull(task_id="get_name",key="last_name")

    # print(f"Hello world! My name is {name} and {age} old! ")

    print(f"Hello world! My name is {first_name} {last_name} and {age} old! ")



# def get_name():
#     return "shaik mahammad ali"

def get_name(ti):
    ti.xcom_push(key="first_name",value="Shaik")
    ti.xcom_push(key="last_name",value="Mahammad Ali")






with DAG(
    dag_id="our_dag_with_python_operator_v1",
    default_args=default_args,
    start_date=datetime(2024,6,25,5),
    schedule_interval='@daily'

) as dag :
    
    task1=PythonOperator(task_id="task1_function",
                         python_callable=task1_function,
                         op_kwargs={
                                    "age":26
                                    }
                         )
    
    task2=PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )
    
    task2>> task1