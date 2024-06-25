from airflow.decorators import dag,task
from datetime import datetime,timedelta

default_args={
    "owner":"shaik mahammad ali",
    "retries":5,
    "retry_delay": timedelta(seconds=2)
}

@dag(
        dag_id="dag_with_taskflow_api",
        default_args=default_args,
        start_date=datetime(2024,6,20),
        schedule_interval="0 4 * * *"
        
)
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {"first_name":"Shaik","last_name":"Mahammad Ali"}
    
    @task()
    def get_age():
        return 26
    
    @task()
    def greet(first_name,last_name,age):
        print(f"Hello World! My name is {first_name} {last_name} and Iam {age} old!")
    
    name=get_name()
    age=get_age()

    greet(first_name=name["first_name"],last_name=name["last_name"],age=age)

greet_dag_obj=hello_world_etl()

