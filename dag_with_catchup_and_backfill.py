from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    "owner":"Shaik Mahammad Ali",
    "retries":5,
    "retry_delay":timedelta(seconds=2)
}

with DAG() as dag:
    