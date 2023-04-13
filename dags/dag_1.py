from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id="jeffer_se_va",
         description="Se va para ecuador",
         schedule_interval="0 12 * * *") as dag:
    
    t1 = EmptyOperator(task_id="task_1")

    t1