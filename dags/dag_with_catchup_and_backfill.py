from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    "owner":"Shaik Mahammad Ali",
    "retries":5,
    "retry_delay":timedelta(seconds=2)
}


'''
by default the catchup value to true we need to disable  that means False
'''
with DAG(
    dag_id="dag_with_catchup_and_backfill",
    description="dag_with_catchup_and_backfill that is description",
    default_args=default_args,
    start_date=datetime(2024,6,20),
    schedule_interval=timedelta(seconds=4),
    catchup=False
) as dag:
    task1=BashOperator(task_id="task1",
                       bash_command="echo task1 executed" 
                        )
    