from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args={
    'owner':"shaik mahammad ali",
    "retries":5,
    "retry_delay":timedelta(minutes=2)
}

with DAG(
    dag_id="our_first_dag",
    description="This is our first dag that I write",
    start_date=datetime(2024,6,24,5),
    schedule_interval='daily',
    default_args=default_args

) as dag:
    '''
    dag_id: str : it is an id of an dag
    description : str : it is an detail description of an dag
    start_date : datetime obj : it a time start to the DAG on which day and which time last parameter is time 
    schedule_interval: how frequently we need to the DAG is it daily or dayby day
    default_args= its a have details of owner and how many times retry has to done and after how many minutes later retry has to initiate after if we have any failure in DAG 
    
    '''
    
    task1=BashOperator(task_id="first_task",
                       bash_command="echo hello world, this is the first task",
                       
                       )
    task2= BashOperator(task_id="second_task",
                        bashcommand="echo hey. Iam task2 and will be running after task1 is done"
                    )
    task3= BashOperator(task_id="third_task",
                        bash_command="echo hey , Iam task3 I will be runing parallely with task2 and running after task1"
                        )

    task1.set_downstream(task2)

    # task1 >> task2
    # task1.set_downstream([task2,task3])
    # task1>>[task2,task3]

