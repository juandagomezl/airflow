from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id="jeffer_se_va",
         description="Se va para ecuador",
         start_date= datetime(2023, 4, 17),
         schedule_interval="0 12 * * *") as dag:
    
    t1 = EmptyOperator(task_id="task_1")

    t1