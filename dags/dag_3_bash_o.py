from airflow import DAG
from airflow.orerators.bash import BashOperator
from datetime import datetime


with DAG(dag_id="Bash_Operator",
         description="Segundo Operador",
         start_date= datetime(2023, 4, 17),
         schedule_interval="0 12 * * *") as dag:
    
    t1 = BashOperator(task_id="task_3", 
                    bash_command="echo 'Los quiero'")

    t1